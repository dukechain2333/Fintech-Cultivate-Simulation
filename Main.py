#  @author ZHChain
#  @File:Main.py
#  @createTime 2021/05/03 04:18:03


from DataCollector import *
from Student import *
import numpy as np

if __name__ == '__main__':
    dc = DataCollector()
    dc.runStudent(2)
    # data = np.load('data.npy', allow_pickle=True)
    # print(data)
