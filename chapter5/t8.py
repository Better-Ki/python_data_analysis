# 使用 K—Means 算法聚类消费行为特征

import numpy as np
import pandas as pd

#参数初始化
inputfile = 'E:/dataAnalysisFile/24064925aueh/DataAndCode/chapter5/demo/data/consumption_data.xls'  #销量及其他数据
k = 3 #聚类类别
threhold = 2 #离散点阈值
iteration = 500 #聚类循环的次数

data = pd.read_excel(inputfile, index_col='Id')  #读取数据
data_zs = 1.0*(data - data.mean())/data.std()  #数据标准化

from sklearn.cluster import KMeans
model = KMeans(n_clusters=k, max_iter=iteration) #分为k类
model.fit(data_zs)  #开始聚类

#标准化数据及其类别
r = pd.concat([data_zs, pd.Series(model.labels_, index=data.index)], axis=1)
#每个样本对应的类别
r.columns = list(data.columns) + [u'聚类类别']  #重命名表头
norm = []
for i in range(k):  #逐一处理
    norm_tmp = r[['R', 'F', 'M']][r[u'聚类类别'] == i] - model.cluster_centers_[i]
    norm_tmp = norm_tmp.apply(np.linalg.norm, axis=1)  #求出绝对距离
    norm.append(norm_tmp/norm_tmp.median())  #求相对距离并添加
norm = pd.concat(norm)  #合并

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

norm[norm <= threhold].plot(style='go') #正常点
discrete_points = norm[norm > threhold] #离群点
discrete_points.plot(style='ro')

for i in range(len(discrete_points)): #离群点做标记
    id = discrete_points.index[i]
    n = discrete_points.iloc[i]
    plt.annotate('(%s, %.2f)' %(id, n), xy=(id, n), xytext=(id, n))
plt.xlabel('编号')
plt.ylabel('相对距离')
plt.show()
