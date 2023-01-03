# 使用K-Means算法聚类分析消费行为特征数据

import pandas as pd

inputfile = 'E:/dataAnalysisFile/24064925aueh/DataAndCode/chapter5/demo/data/consumption_data.xls' #销量及其他属性数据
outputfile = 'data_type.xls' #保存结果的文件名

k = 3  # 聚类的类别
iteration = 500  # 聚类的最大循环次数
data = pd.read_excel(inputfile, index_col='Id')  # 读取数据
data_zs = 1.0 * (data - data.mean())/data.std() #数据标准化

from sklearn.cluster import KMeans

model = KMeans(n_clusters=k, max_iter=iteration) #聚类为3 最大次数为500
model.fit(data_zs)

# 简单打印结果
r1 = pd.Series(model.labels_).value_counts()  #统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_)  #找出聚类中心
r = pd.concat([r2, r1], axis=1)  #横向连接(0是纵向)，得到聚类中心对应的类别下的数目
r.columns = list(data.columns) + [u'类别数目'] #重命名表头
print(r)  #详细输出原始数据及其类别

r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)
r.columns = list(data.columns) + [u'聚类类别']
r.to_excel(outputfile)  #保存结果

# 绘制聚类后的概率密度图
def density_plot(data): #自定义作图函数
  import matplotlib.pyplot as plt
  plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
  plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
  p = data.plot(kind='kde', linewidth = 2, subplots = True, sharex = False)
  [p[i].set_ylabel(u'密度') for i in range(k)]
  plt.legend()
  return plt
pic_output = './tmp/pd_' #概率密度图文件名前缀
for i in range(k):
  density_plot(data[r[u'聚类类别']==i]).savefig(u'%s%s.png' %(pic_output, i))