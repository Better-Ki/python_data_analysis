# k-means 聚类算法
import pandas as pd
from sklearn.cluster import KMeans

inputfile = './data/zscoreddata.xls' #待聚类的数据文件
k = 5 #聚类类别数

data = pd.read_excel(inputfile) #读取数据
kmodel = KMeans(n_clusters=k)

kmodel.fit(data)
print(kmodel.cluster_centers_) #查看聚类中心
print(kmodel.labels_)

demo = pd.DataFrame(kmodel.labels_, columns=['numbers'])
demo1= pd.DataFrame(kmodel.cluster_centers_, columns=data.columns) # 保存聚类中心
demo2= demo['numbers'].value_counts() # 确定各个类的数目
print(demo2)

demo4 = pd.concat([demo2, demo1], axis=1)
demo4.index.name='labels'
demo4.to_excel('./tmp/kmeansresults.xlsx')


