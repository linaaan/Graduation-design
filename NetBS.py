import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import HetEnv


device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")
print(device)
# 超参数
BATCH_SIZE = 32  # 样本数量
LR = 0.1  # 学习率
EPSILON = 0.1  # greed policy
GAMMA = 0.9  # reward discount
MEMORY_CAPACITY = 1000  # 记忆回访机制的记忆库容量
TARGET_REPLACE_ITER = 100  # 目标网络的更新频率
env = HetEnv.Env_AL_HetNet()  # 高移动性环境
N_ACTIONS = 6  # 环境的动作数量 up 暂时认为每个小区内所有的ue都执行一套up
N_STATES = 2  # 环境的状态参数数目
N_learn = 15


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


dqn1 = DQN()
dqn2 = DQN()
dqn3 = DQN()
j = 0
tk1 = []
tk2 = []
tk3 = []
i = 0
for i in range(N_learn):
    # N_learn 个 episode 循环
    print('<<<<<<<<Episode: %s' % i)
    print(tk1)
    print(tk2)
    print(tk3)
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

    # 重置环境
    episode_reward_sum1 = 0
    episode_reward_sum2 = 0
    episode_reward_sum3 = 0
    done = 0
    # 初始化该循环对应的episode的总奖励
    while True:
        # 开始一个episode
        a1 = dqn1.choose_action(s1)
        a2 = dqn2.choose_action(s2)
        a3 = dqn3.choose_action(s3)

        # 输入该步对应的状态s，选择动作

        s1, a1, r1, snext1 = env.step(a1, 1)
        # 执行动作，获得反馈***在配置训练环境的时候需要着重注意到step函数，输出为什么再分析
        s1_ = torch.from_numpy(np.array(snext1))
        s1_ = s1_.float()
        dqn1.store_transition(s1, a1, r1, s1_)
        # 存储样本
        episode_reward_sum1 += r1
        # 逐步加上一个episode内每个step的reward
        s1 = s1_
        # 更新状态

        s2, a2, r2, snext2 = env.step(a2, 2)
        # 执行动作，获得反馈***在配置训练环境的时候需要着重注意到step函数，输出为什么再分析
        s2_ = torch.from_numpy(np.array(snext2))
        s2_ = s2_.float()
        dqn2.store_transition(s2, a2, r2, s2_)
        # 存储样本
        episode_reward_sum2 += r2
        # 逐步加上一个episode内每个step的reward
        s2 = s2_
        # 更新状态

        s3, a3, r3, snext3 = env.step(a3, 3)
        # 执行动作，获得反馈***在配置训练环境的时候需要着重注意到step函数，输出为什么再分析
        s3_ = torch.from_numpy(np.array(snext3))
        s3_ = s3_.float()
        dqn3.store_transition(s3, a3, r3, s3_)
        # 存储样本
        episode_reward_sum3 += r3
        # 逐步加上一个episode内每个step的reward
        s3 = s3_
        # 更新状态

        if dqn1.memory_counter > MEMORY_CAPACITY:
            # 如果累计的transition数量超过了记忆库的固定容量1000
            # 开始学习 (抽取记忆，即32个transition，并对评估网络参数进行更新，
            # 并在开始学习后每隔100次将评估网络的参数赋给目标网络)
            dqn1.learn(1)
            dqn2.learn(2)
            dqn3.learn(3)

        if done > MEMORY_CAPACITY+N_learn:
            # 如果done为True
            print('sbs1_episode%s---reward_sum: %s' % (i, round(episode_reward_sum1, 2)))
            tk1.append(round(episode_reward_sum1, 2))
            print('sbs2_episode%s---reward_sum: %s' % (i, round(episode_reward_sum2, 2)))
            tk2.append(round(episode_reward_sum2, 2))
            print('sbs1_episode%s---reward_sum: %s' % (i, round(episode_reward_sum3, 2)))
            tk3.append(round(episode_reward_sum3, 2))
            break  # ***具体怎么结束这个episode具体分析

        done += 1

print(tk1)
print(tk2)
print(tk3)

torch.save(dqn1, "DQN1.pth")
torch.save(dqn2, "DQN2.pth")
torch.save(dqn3, "DQN3.pth")

q1 = np.transpose(dqn1.q1).flatten()

q2 = np.transpose(dqn2.q2).flatten()

q3 = np.transpose(dqn3.q3).flatten()

np.save('q1num.npy', dqn1.q1num)
np.save('q2num.npy', dqn2.q2num)
np.save('q3num.npy', dqn3.q3num)

np.save('q1.npy', q1)
# np.save('4q1.npy', q1) 在神经元是4的时候储存q值
# np.save('64q1.npy', q1) 在神经元是64的时候储存q值

np.save('q2.npy', q2)
np.save('q3.npy', q3)
np.save('reward1', tk1)
np.save('reward2', tk2)
np.save('reward3', tk3)
