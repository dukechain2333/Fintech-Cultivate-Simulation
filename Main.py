#  @author ZHChain
#  @File:Main.py
#  @createTime 2021/05/03 04:18:03

from DataCollector import *
from Student import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(8, 6))
ax1 = Axes3D(fig)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
dc = DataCollector()
dc.runStudent(1000, 40)
data = np.load('data.npy', allow_pickle=True)


def transitTime():
    newData = []
    for d in data:
        s = []
        for i in range(len(d)):
            tmp = [d[i, 0], d[i, 1], i]
            s.append(tmp)
        newData.append(s)

    return np.array(newData)


def drawPicture(i):
    label = 'timestep {0}'.format(i)
    newData = transitTime()
    for s in range(len(newData)):
        ax1.plot3D(newData[s][:, 0], newData[s][:, 2], newData[s][:, 1])
        # ax1.plot3D(newData[s][i, 0], newData[s][i, 2], newData[s][i, 1])
        # ax1.plot3D(newData[i][:, 0], newData[i][:, 2], newData[i][:, 1])
    ax1.set_ylabel('时间')
    ax1.set_xlabel('金融能力')
    ax1.set_zlabel('计算机能力')
    ax1.grid(True)
    ax1.view_init(10, 50)
    fig.savefig('Simulation.png')
    plt.show()
    return ax1


if __name__ == '__main__':
    drawPicture(1)
