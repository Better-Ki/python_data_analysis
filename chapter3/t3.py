# 菜品盈利数据帕累托图

from __future__ import print_function
import pandas as pd

dish_profit = 'E:/dataAnalysisFile/24064925aueh/DataAndCode/chapter3/demo/data/catering_dish_profit.xls'    #餐饮盈利数据
data = pd.read_excel(dish_profit, index_col=u'菜品名')
data = data[u'盈利'].copy()
# data.sort(ascending=False)
# AttributeError: 'Series' object has no attribute 'sort'
# Series.sort_index(ascending=True) 根据索引返回已排序的新对象
# 换成下面这样就可以了
data.sort_index(ascending=False)

import matplotlib.pyplot as plt  #导入图像库

plt.rcParams['font.sans-serif'] = ['SimHei']  #中文显示
plt.rcParams['axes.unicode_minus'] = False  #负号显示

plt.figure()    #创建画布
data.plot(kind='bar')
plt.ylabel(u'盈利（元）')

p = 1.0*data.cumsum()/data.sum()
p.plot(color='r', secondary_y=True, style='-o', linewidth=2)
plt.annotate(format(p[6], '.4%'), xy=(6, p[6]), xytext=(6*0.9, p[6]*0.9),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2")) #添加注释，即85%处的标记
plt.ylabel(u'盈利（比例）')
plt.show()
