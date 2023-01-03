# 使用神经网络算法预测销量的高低

import pandas as pd

filename = 'E:/dataAnalysisFile/24064925aueh/DataAndCode/chapter5/demo/data/sales_data.xls'
data = pd.read_excel(filename, index_col=u'序号') #导入数据

# 数据是类别标签，要将其转换为数据
# 用‘1’表示好，高，是 ‘0’表示坏，否，低
data[data==u'好'] = 1
data[data==u'是'] = 1
data[data==u'高'] = 1
data[data != 1] = 0
x = data.iloc[:, :3].values.astype(int)
y = data.iloc[:, 3].values.astype(int)
