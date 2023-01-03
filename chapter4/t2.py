# 数据规范化

import pandas as pd
import numpy as np

datafile = 'E:/dataAnalysisFile/24064925aueh/DataAndCode/chapter4/demo/data/normalization_data.xls' #参数初始化
data = pd.read_excel(datafile, header=None)

(data - data.min())/(data.max() - data.min()) #最小-最大规范化

(data - data.mean())/data.std() #零均值规范化

data/100**np.ceil(np.log10(data.abs().max())) #小数定标规范化
