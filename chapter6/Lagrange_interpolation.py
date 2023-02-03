# 拉格朗日插值法

import pandas as pd
from scipy.interpolate import lagrsange

#初始化参数
inputfile = './data/missing_data.xls'
outputfile = './tmp/missing_data_processed.xls'

#读入数据
data = pd.read_excel(inputfile, header=None)

#自定义列向量插值函数
#s 为列向量， n为被插值的位置， k为取前后的数据个数
def ployinterp_column(s, n, k=5):
    y = s.reindex(list(range(n-k, n)) + list(range(n+1, n+1+k))) #取空值处前后各五个
    y = y[y.notnull()]  #剔除空值
    return lagrange(y.index, list(y))(n)  #最后的括号就是我们要插值的n

for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]: #如果为空即插值
            data[i][j] = ployinterp_column(data[i], j)
data.to_excel(outputfile)
print('success!')
