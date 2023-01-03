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

from sklearn.manifold import TSNE
tsne = TSNE()
tsne.fit_transform(data_zs)  #进行数据降维

tsne = pd.DataFrame(tsne.embedding_, index=data_zs.index) #转换数据格式
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 不同的类别使用不用的颜色和样式绘图
d = tsne[r[u'聚类类别'] == 0]
plt.plot(d[0], d[1], 'r.')

d = tsne[r[u'聚类类别'] == 1]
plt.plot(d[0], d[1], 'go')

d = tsne[r[u'聚类类别'] == 2]
plt.plot(d[0], d[1], 'b*')

plt.show()
