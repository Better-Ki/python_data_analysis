import pandas as pd

catering_sale = 'E:/dataAnalysisFile/24064925aueh/DataAndCode/chapter3/demo/data/catering_sale.xls'
data = pd.read_excel(catering_sale, index_col=u'日期') #读取数据，指定“日期”为索引列
print(data)
print(data.describe())

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei'] #正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #正常显示负号

plt.figure() #建立图像

p = data.boxplot(return_type='dict') #画箱线图
x = p['fliers'][0].get_xdata()  #'files'即为异常值的标签
y = p['fliers'][0].get_ydata()
y.sort() #从小到大排序

for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]),
                     xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]),
                     xytext=(x[i] + 0.08, y[i]))
plt.show()
