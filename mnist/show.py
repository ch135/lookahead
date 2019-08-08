# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 9:42
# @Author  : chenhao
# @FileName: show.py
# @Software: PyCharm
# @Desc: txt文件绘画成曲线图
import numpy as np
import matplotlib.pyplot as plt


def show(path):
    y = []
    x = np.linspace(0, 10, 10)
    index = line = data = 0
    color = ['r', 'k', 'y', 'c', 'm', '#FFEE00', 'b', 'g', '#FF00FF']
    label = ''
    type = [':', ':', '', '', ':', ':', ':', ':', ':']
    with open(path, "r") as file:
        messages = file.readlines()
        for message in messages:
            if not 'Epoch' in message:
                if y != []:
                    plt.plot(x, y, color=color[index], label=label)
                    y = []
                    index += 1
                label = message
            else:
                line += 1
                data += float(message.split()[-1])
                if line % 94 == 0:
                    y.append(data/94)
                    data = 0
    plt.legend(loc=0)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.savefig('result.jpg')
    plt.show()


if __name__ == '__main__':
    show('loss.txt')
