# 线损率属性构造

import pandas as pd

inputfile = 'E:/dataAnalysisFile/24064925aueh/DataAndCode/chapter4/demo/data/electricity_data.xls'
outputfile = './tmp/electricity_data.xls'  #输出路径
data = pd.read_excel(inputfile)

data[u'线损率'] = ((data[u'供入电量'] - data['供出电量']) / data[u'供入电量'])

data.to_excel(outputfile, index=False)