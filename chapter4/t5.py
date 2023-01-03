# 主成分分析降维代码

import pandas as pd

inputfile = 'E:/dataAnalysisFile/24064925aueh/DataAndCode/chapter4/demo/data/principal_component.xls'
outputfile = './tmp/principal_component.xls'  #输出路径

data = pd.read_excel(inputfile, header=None) #读入数据

from sklearn.decomposition import PCA

pca = PCA()
pca.fit(data)
print(pca.components_) #返回模型的各个向量特征
print(pca.explained_variance_ratio_) #返回各个成分各自的方差百分比

#接代码清单

pca = PCA(3)
pca.fit(data)
low_id = pca.transform(data) #降低维度
pd.DataFrame(low_id).to_excel(outputfile)
pca.inverse_transform(low_id) #必要时可以使用inverse——transfrom()函数来复原数据
