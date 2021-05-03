#  @author ZHChain
#  @File:Scatter.py
#  @createTime 2021/05/03 21:09:03


import numpy as np
import matplotlib.pyplot as plt

data = np.load('data.npy')

finance = []
CS = []

for d in data:
    for i in range(len(d)):
        finance.append(d[i][0])
        CS.append((d[i][1]))

plt.xlabel('Finance Ability')
plt.ylabel('CS Ability')
plt.scatter(finance, CS, s=10)
plt.savefig('Scatter.png')
plt.show()
