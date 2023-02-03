# 标准差标准化
import pandas as pd

datafile = './data/zscoredata.xls'
zscoredfile = './tmp/zscoreddata.xls'  # 标准差化后的数据存储路径文件

# 标准化处理
data = pd.read_excel(datafile)
data = (data - data.mean(axis=0))/(data.std(axis=0))  #简洁的完成标准化变换
data.columns = ['Z' + i for i in data.columns]  #表头重命名
data.to_excel(zscoredfile, index=False)