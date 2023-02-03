# 数据规约与属性构造
import pandas as pd
import numpy as np

datafile = './tmp/data_decrese.xls'
transformedflie = './tmp/data_transformed.xls'
data = pd.read_excel(datafile)

# L = LOAD_TIME - FFP_DATE
# R = LAST_TO_END
# F = FLIGHT_COUNT
# M = SEG_KM_SUM
# C = avg_discount
data['L1'] = pd.to_datetime(data['LOAD_TIME']) - pd.to_datetime(data['FFP_DATE'])# 以纳秒为单位
data['L3'] = data['L1']/np.timedelta64(1, 'M') #将间隔时间转换为以月份为对象
data['L3'] = data['L3'].round(2)
data['LAST_TO_END'] = (data['LAST_TO_END']/30).round(2) #假定每个月是30天，不够精确
data['avg_discount'] = data['avg_discount'].round(2)

data.drop('L1', axis=1, inplace=True) #删除中间变量
data.drop(data.columns[:3], axis=1, inplace=True) #去掉不需要的u'LOAD_TIME', u'FFP_DATE'
data.rename(columns = {'LAST_TO_END':'R','FLIGHT_COUNT': 'F', 'SEG_KM_SUM' : 'M' , 'avg_discount' : 'C', 'L3' : 'L'}, inplace=True)
data.to_excel(transformedflie, index=False)

# LRFMC指标的取值范围
def f(x):
    return pd.Series([x.min(),x.max()], index=['min','max'])
d = data.apply(f)
d.to_excel('./tmp/summary_data.xlsx')