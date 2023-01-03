#统计作图函数

# plot
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 2*np.pi, 50)
# y = np.sin(x)
#
# plt.plot(x, y, 'bp--')  #控制图像格式为蓝色带星虚线，显示正弦曲线
# plt.show()

# pie
# import matplotlib.pyplot as plt
#
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'  #定义标签
# sizes = [15, 30, 45, 10]   #每一块的比例
# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']  #每一块的颜色
# explode = (0, 0.1, 0, 0)    #突出显示
#
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# plt.axis('equal') #显示为园
# plt.show()

# hist
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.random.rand(1000)
# plt.hist(x, 10)
# plt.show()

# boxplot
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
# x = np.random.rand(1000)
# D = pd.DataFrame([x, x+1]).T  #构造两列的dataframe
# D.plot(kind='box')
# plt.show()

# plot(logx=True) / plot(logy=True) 对数图形
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# x = pd.Series(np.exp(np.arange(20)))    #原始数据
# x.plot(label=u'原始数据图', legend=True)
# plt.show()
# x.plot(logy=True, label=u'对数数据图', legend=True)
# plt.show()

# plot(yerr=error) 误差条形图
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

error = np.random.rand(10) #定义误差列
y = pd.Series(np.sin(np.arange(10))) #均值数据列
y.plot(yerr=error) #绘制误差图
plt.show()