# 雷达图的绘制
import pandas as pd

datafile = './tmp/kmeansresults.xls'

data = pd.read_excel(datafile)

data1 = data[['labels', 'ZL', 'ZR', 'ZF', 'ZM', 'ZC']]

subset = data1.round(3)
subset.to_excel('./tmp/testradar.xls')
data = subset.values


