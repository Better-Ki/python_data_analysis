# 数据清洗，过滤掉不符合规则的数据
# 丢弃票价为空的记录
# 丢弃票价为0、平均折扣率不为0、总飞行公里数大于0的记录
import pandas as pd

datafile = './data/air_data.csv'
cleanfile = './tmp/data_cleaned.xls'
decresefile = './tmp/data_decrese.xls'

data = pd.read_csv(datafile, encoding='utf-8')
data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()] #notnull后记得加 '()'
index1 = data['SUM_YR_1'] != 0
index2 = data['SUM_YR_2'] != 0
index3 = (data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0) #三个规则
data = data[index1 | index2 | index3]
data.to_excel(cleanfile)

#建立LRFMC模型，只保留6个属性
data1 = data[['LOAD_TIME', 'FFP_DATE', 'LAST_TO_END', 'FLIGHT_COUNT', 'SEG_KM_SUM', 'avg_discount']]
data1.to_excel(decresefile)