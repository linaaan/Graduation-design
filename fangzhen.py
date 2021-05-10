import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import HetEnv
import matplotlib.pyplot as plt
from scipy import interpolate

BATCH_SIZE = 32        # 样本数量
LR = 0.1                   # 学习率
EPSILON = 0.1               # greed policy
GAMMA = 0.9                    # reward discount
MEMORY_CAPACITY = 1000     # 记忆回访机制的记忆库容量
TARGET_REPLACE_ITER = 100       # 目标网络的更新频率
env = HetEnv.Env_AL_HetNet()          # 高移动性环境
N_ACTIONS = 6           # 环境的动作数量
N_STATES = 2              # 环境的状态参数数


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(N_STATES, 32)
        self.fc1.weight.data.normal_(0, 0.1)
        self.fc2 = nn.Linear(32, 32)
        self.fc2.weight.data.normal_(0, 0.1)
        self.fc3 = nn.Linear(32, 32)
        self.fc3.weight.data.normal_(0, 0.1)
        self.fc4 = nn.Linear(32, 32)
        self.fc4.weight.data.normal_(0, 0.1)
        self .out = nn.Linear(32, N_ACTIONS)
        self.out.weight.data.normal_(0, 0.1)

    def forward(self, x):
        # 定义foward函数，输入为x
        x1 = F.relu(self.fc1(x))
        x2 = F.relu(self.fc2(x1))
        x3 = F.relu(self.fc3(x2))
        x4 = F.relu(self.fc4(x3))
        actions_value = self.out(x4)
        return actions_value


class DQN(nn.Module):
    def __init__(self):
        super(DQN, self).__init__()
        self.eval_net, self.target_net = Net(), Net()
        # 利用NET建立两个神经网络。evalnet是估计值，targetnet是目标值
        self.learn_step_counter = 0
        # 目标网络用
        self.memory_counter = 0
        self.memory = np.zeros((MEMORY_CAPACITY, N_STATES*2+2))
        # 初始化记忆回访库，一行（待定）代表一个transition，但是在同一个时间需要获取到3个SBS的状态 ** 需要建立3个神经网络，并列运行
        self.optimizer = torch.optim.Adam(self.eval_net.parameters(), lr=LR)
        # 使用adam优化器（梯度）
        self.loss_func = nn.MSELoss()
        # 使用均方损失函数
        self.q1 = []
        self.q2 = []
        self.q3 = []
        self.q1num = 0
        self.q2num = 0
        self.q3num = 0

    def choose_action(self, x):
        # t = env.tcon  t是此时的时间，x是状态

        if np.random.uniform(0, 1) > EPSILON:
            # 贪婪算法
            actions_value = self.eval_net.forward(x)
            actions_value = torch.unsqueeze(actions_value, 0)
            # 获得前向传播估计值,所有Q值
            action = torch.max(actions_value, 1)[1]
            # 输出每一行最大值的索引（1）是每行【1】是只返回每个索引，并转化为numpy ndarray形式
            action = action.item() + 1
            # 输出action的第一个数，即最大的那个的索引 **
        else:
            action = np.random.randint(1, 6)
            # 这里action随机等于一个数，应该也是索引(0, 或1) （N ACTIONS =   ）**
        return action

    def store_transition(self, s, a, r, s_):
        # 定义记忆存储函数，这里输入为一个transition
        transition = np.hstack((s, [a, r], s_))
        # 在水平方向上拼接数组，每行和每行拼在一起
        index = self.memory_counter % MEMORY_CAPACITY
        # 获取要transition置入第几行
        self.memory[index, :] = transition
        # 置入transition
        self.memory_counter += 1

    def learn(self, sbs):
        # 定义学习函数，记忆库存满后便开始学习
        # 目标网络参数更新
        if self.learn_step_counter % TARGET_REPLACE_ITER == 0:
            # 最开始触发一次，然后每100步触发一次
            self.target_net.load_state_dict(self.eval_net.state_dict())
            # 讲评估网络的参数赋值给目标网络
            # print('赋值')
        self.learn_step_counter += 1
        # 学习步数加1

        # 抽取记忆库中的批数据***但对于多个SBS每次抽取的数据数量可能不同
        sample_index = np.random.choice(MEMORY_CAPACITY, BATCH_SIZE)
        # 在【0，1000】内随机抽取32个数
        b_memory = self.memory[sample_index, :]
        # 抽取32个索引对应的32个transition，存入b——memory
        b_s = torch.FloatTensor(b_memory[:, :N_STATES])
        # 将32个s（状态）抽出，转为32bit floating point形式，并存储在b——s中，b——s 32行 N_STATES列
        b_a = torch.LongTensor(b_memory[:, N_STATES:N_STATES+1].astype(int))
        # 将32个a抽出，转为64-bit integer (signed)形式，并存储到b_a中 (之所以为LongTensor类型，是为了
        # 方便后面torch.gather的使用)，b_a为32行1列
        b_r = torch.FloatTensor(b_memory[:, N_STATES+1:N_STATES+2])
        # 将32个r抽出，转为32-bit floating point形式，并存储到b_s中，b_r为32行1列
        b_s_ = torch.FloatTensor(b_memory[:, -N_STATES:])
        # 将32个s_抽出，转为32-bit floating point形式，并存储到b_s中，b_s_为32行N_STATES列

        # 获取32个transition的评估值和目标值，并利用损失函数和优化器进行评估网络参数更新
        q_eval = self.eval_net(b_s).gather(1, b_a-1)
        # eval_net(b_s)通过评估网络输出32行每个b_s对应的一系列动作值，一行对应所有的，然后.gather(1, b_a)代表
        # 对每行对应索引b_a的Q值提取进行聚合,gather函数1是按照列进行
        # 分配，按照b_a的索引从列进行取值,b_a里的是行动的索引，对应行动
        q_next = self.target_net(b_s_).detach()
        # q_next不进行反向传递误差，所以detach；q_next表示通过目标网络输出32行每个b_s_对
        # 应的一系列动作值
        # q_target = (1-LR)*q_eval+LR*(b_r + GAMMA * q_next.max(1)[0].view(BATCH_SIZE, 1))
        q_target = b_r + GAMMA * q_next.max(1)[0].view(BATCH_SIZE, 1)
        # q_next.max(1)[0]表示只返回每一行的最大值，不返回索引(长度为32的一维张量)；.view()表
        # 示把前面所得到的一维张量变成(BATCH_SIZE, 1)的形状；最终通过公式得到目标值
        loss = self.loss_func(q_eval, q_target)
        if sbs == 1:
            sum = 0
            qz = q_eval.detach().numpy()
            for i in range(32):
                sum += qz[i]
            lop = sum/32
            self.q1.append(lop)
            self.q1num += 1
        if sbs == 2:
            sum = 0
            qz = q_eval.detach().numpy()
            for i in range(32):
                sum += qz[i]
            lop = sum/32
            self.q2.append(lop)
            self.q2num += 1
        if sbs == 3:
            sum = 0
            qz = q_eval.detach().numpy()
            for i in range(32):
                sum += qz[i]
            lop = sum/32
            self.q3.append(lop)
            self.q3num += 1
        # if self.learn_step_counter % 20 == 0:
        #     print(loss)
        # # 求出损失函数

        self.optimizer.zero_grad()
        # 清空上一步的梯度
        loss.backward()
        # 误差反向传播，更新参数
        self.optimizer.step()
        # 更新评估网络的所有参数


dqn1 = torch.load("DQN1.pth")
dqn2 = torch.load("DQN2.pth")
dqn3 = torch.load("DQN3.pth")

# ------------------------------------------仿真------------------------------------------------

# 不同基站Q值收敛情况对比仿真---------------------------------------------------------------------

q1 = np.load('q1.npy')
q2 = np.load('q2.npy')
q3 = np.load('q3.npy')
q1num = np.load('q1num.npy')
q2num = np.load('q2num.npy')
q3num = np.load('q3num.npy')


kt = len(q1)
x1 = np.linspace(0, q1num, kt)
z1 = np.polyfit(x1, q1, 7)
p1 = np.poly1d(z1)
yvals = p1(x1)


kt = len(q2)
x2 = np.linspace(0, q2num, kt)
z2 = np.polyfit(x2, q2, 7)
p2 = np.poly1d(z2)
yvalm = p2(x2)


kt = len(q3)
x3 = np.linspace(0, q3num, kt)
z3 = np.polyfit(x3, q3, 7)
p3 = np.poly1d(z3)
yvalt = p3(x3)

fig1 = plt.figure(1)

ax11 = fig1.add_subplot(3, 1, 1)
ax12 = fig1.add_subplot(3, 1, 2)
ax13 = fig1.add_subplot(3, 1, 3)
ax11.plot(x1, yvals)
ax12.plot(x2, yvalm)
ax13.plot(x3, yvalt)
ax11.plot(x1, yvals, label='sbs1', color='blue')
ax12.plot(x2, yvalm, label='sbs2', color='red')
ax13.plot(x3, yvalt, label='sbs3', color='green')
ax11.set_xlabel('Learning iterations')
ax11.set_ylabel('Q-Value')
ax12.set_xlabel('Learning iterations')
ax12.set_ylabel('Q-Value')
ax13.set_xlabel('Learning iterations')
ax13.set_ylabel('Q-Value')
ax11.legend()
ax12.legend()
ax13.legend()
plt.suptitle('The Q-value convergence speed comparison in terms of different small cell base')
plt.show()

# 不同基站的链路满足率仿真------------------------------------------------------------------------------
demDarated = 20*10**7
demDarateu = 5*10**7
dist = -1  # 若是超过需求上限，则减值进行惩罚
BMU = 0.3  # 与环境中的奖励函数阈值相同
BMD = 1.0
env.reset()
s_m1 = env.state1
s_m2 = env.state2
s_m3 = env.state3
s1 = torch.from_numpy(np.array(s_m1))
s2 = torch.from_numpy(np.array(s_m2))
s3 = torch.from_numpy(np.array(s_m3))
s1 = s1.float()
s2 = s2.float()
s3 = s3.float()
i = 0
j = 0
t = 2
k = 2
DQRu1 = 0
DQRd1 = 0
DQRu2 = 0
DQRd2 = 0
DQRu3 = 0
DQRd3 = 0
GRu1 = 0
GRu2 = 0
GRu3 = 0
GRd1 = 0
GRd2 = 0
GRd3 = 0

s11 = s1
s22 = s2
s33 = s3
oct_up1 = 0
oct_down1 = 0
oct_up2 = 0
oct_down2 = 0
oct_up3 = 0
oct_down3 = 0
for t in range(500):
    for i in range(6):
        a1 = dqn1.choose_action(s11)
        a2 = dqn2.choose_action(s22)
        a3 = dqn3.choose_action(s33)
        Rup1 = 0.1*a1
        Rdown1 = 1 - Rup1
        Rup2 = 0.1*a2
        Rdown2 = 1 - Rup2
        Rup3 = 0.1*a3
        Rdown3 = 1 - Rup3
        if env.C_need1[i][0][t] != 'none':
            octu = (demDarateu/float(env.C_need1[i][0][t]))*Rup1/10
            if octu > BMU:
                DQRu1 += dist
            else:
                DQRu1 += octu
            oct_up1 = octu
        if env.C_need1[i][1][t] != 'none':
            octd = (demDarated/float(env.C_need1[i][1][t]))*Rdown1/10
            if octd > BMD:
                DQRd1 += dist
            else:
                DQRd1 += octd
            oct_down1 = octd
        if env.C_need2[i][0][t] != 'none':
            octu = (demDarateu/float(env.C_need2[i][0][t]))*Rup2/10
            if octu > BMU:
                DQRu2 += dist
            else:
                DQRu2 += octu
            oct_up2 = octu
        if env.C_need2[i][1][t] != 'none':
            octd = (demDarated/float(env.C_need2[i][1][t]))*Rdown2/10
            if octd > BMD:
                DQRd2 += dist
            else:
                DQRd2 += octd
            oct_down2 = octd
        if env.C_need3[i][0][t] != 'none':
            octu = (demDarateu/float(env.C_need3[i][0][t]))*Rup3/10
            if octu > BMU:
                DQRu3 += dist
            else:
                DQRu3 += octu
            oct_up3 = octu
        if env.C_need3[i][1][t] != 'none':
            octd = (demDarated/float(env.C_need3[i][1][t]))*Rdown3/10
            if octd > BMD:
                DQRd3 += dist
            else:
                DQRd3 += octd
            oct_down3 = octd
        s_m1 = [oct_up1, oct_down1]
        s_m2 = [oct_up2, oct_down2]
        s_m3 = [oct_up3, oct_down3]
        s11 = torch.from_numpy(np.array(s_m1))
        s22 = torch.from_numpy(np.array(s_m2))
        s33 = torch.from_numpy(np.array(s_m3))
        s11 = s11.float()
        s22 = s22.float()
        s33 = s33.float()

sk1 = s1
sk2 = s2
sk3 = s3
oct_up1 = 0
oct_down1 = 0
oct_up2 = 0
oct_down2 = 0
oct_up3 = 0
oct_down3 = 0
for k in range(800):
    Rup = 0.4
    Rdown = 0.6
    for j in range(6):
        if env.C_need1[j][0][k] != 'none':
            octu = (demDarateu/float(env.C_need1[j][0][k]))*Rup/10
            if octu > BMU:
                GRu1 += dist
            else:
                GRu1 += octu
            oct_up1 = octu
        if env.C_need1[j][1][k] != 'none':
            octd = (demDarated/float(env.C_need1[j][1][k]))*Rdown/10
            if octd > BMD:
                GRd1 += dist
            else:
                GRd1 += octd
            oct_down1 = octd
        if env.C_need2[j][0][k] != 'none':
            octu = (demDarateu/float(env.C_need2[j][0][k]))*Rup/10
            if octu > BMU:
                GRu2 += dist
            else:
                GRu2 += octu
            oct_up2 = octu
        if env.C_need2[j][1][k] != 'none':
            octd = (demDarated/float(env.C_need2[j][1][k]))*Rdown/10
            if octd > BMD:
                GRd2 += dist
            else:
                GRd2 += octd
            oct_down2 = octd
        if env.C_need3[j][0][k] != 'none':
            octu = (demDarateu/float(env.C_need3[j][0][k]))*Rup/10
            if octu > BMU:
                GRu3 += dist
            else:
                GRu3 += octu
            oct_up3 = octu
        if env.C_need3[j][1][k] != 'none':
            octd = (demDarated/float(env.C_need3[j][1][k]))*Rdown/10
            if octd > BMD:
                GRd3 += dist
            else:
                GRd3 += octd
            oct_down3 = octd
        s_m1 = [oct_up1, oct_down1]
        s_m2 = [oct_up2, oct_down2]
        s_m3 = [oct_up3, oct_down3]
        sk1 = torch.from_numpy(np.array(s_m1))
        sk2 = torch.from_numpy(np.array(s_m2))
        sk3 = torch.from_numpy(np.array(s_m3))
        sk1 = sk1.float()
        sk2 = sk2.float()
        sk3 = sk3.float()

print(DQRu1, DQRd1, DQRu2, DQRd2, DQRu3, DQRd3)
print(GRu1, GRu2, GRu3, GRd1, GRd2, GRd3)

plt.figure(2)

DQNdata = [DQRu1+DQRd1+1600, DQRu2+DQRd2+1600, DQRu3+DQRd3+1600]
COSdata = [GRu1+GRd1+1600, GRu2+GRd2+1600, GRu3+GRd3+1600]
x1 = [1, 4, 7]
x2 = [2, 5, 8]
plt.bar(x1, DQNdata, 1, color='black', label='DQN')
plt.bar(x2, COSdata, 1, color='red', label='Convention')
plt.xticks([1, 4.5, 8], ['small cell base station1', 'small cell base station2', 'small cell base station3'])
plt.ylabel('Oct')
plt.legend()
plt.title('Oct Comparison')
plt.show()

# 奖励曲线--------------------------------------------------------------------------------------
reward1 = np.load('reward1.npy')
reward2 = np.load('reward2.npy')
reward3 = np.load('reward3.npy')
yy = reward1
xx = np.arange(0, 15, 1)
xnew = np.arange(0, 14, 0.01)
func = interpolate.interp1d(xx, yy, kind='cubic')
ynew = func(xnew)
z = np.polyfit(xnew, ynew, 8)
p = np.poly1d(z)
yu = p(xnew)
ymean = 0
for i in range(1200):
    ymean += yu[i+100]
ymean = ymean/1200

plt.figure(3)

plt.plot(xnew, yu, color='blue', label='Reward Curve')
plt.axhline(ymean, color='r', linestyle='-.', label='Convergence Value')
plt.legend()
plt.xlabel('Learning Count')
plt.ylabel('Reward')
plt.title('Reward curve during DQN training')
plt.show()

# 神经网络不同神经元收敛情况对比-----------------------------------------------------------
q41 = np.load('4q1.npy')
q641 = np.load('64q1.npy')

kt = len(q1)
x1 = np.linspace(0, q1num, kt)
z1 = np.polyfit(x1, q1, 5)
p1 = np.poly1d(z1)
yvals = p1(x1)

kt = len(q41)
x41 = np.linspace(0, q1num, kt)
z41 = np.polyfit(x41, q41, 5)
p41 = np.poly1d(z41)
y41 = p41(x41)

kt = len(q641)
x641 = np.linspace(0, q1num, kt)
z641 = np.polyfit(x641, q641, 5)
p641 = np.poly1d(z641)
y641 = p641(x641)

plt.figure(figsize=(15, 5))
plt.plot(x1, yvals, color='blue', label='Number of units = 32')
plt.plot(x41, y41, color='red', label='Number of units = 4')
plt.plot(x641, y641, color='black', label='Number of units = 64')
plt.xlabel('Learning count')
plt.ylabel('reward')
plt.title('The Q-value convergence speed comparison in terms of different number of units in each hidden layer')
plt.legend()
plt.show()
