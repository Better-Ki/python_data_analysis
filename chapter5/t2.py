# 使用ID3决策树算法预测销量高低

import pandas as pd

filename = 'E:/dataAnalysisFile/24064925aueh/DataAndCode/chapter5/demo/data/sales_data.xls'
data = pd.read_excel(filename, index_col=u'序号') #导入数据

# 数据是类别标签，要将其转换为数据
# 用‘1’表示好，高，是 ‘-1’表示坏，否，低
data[data==u'好'] = 1
data[data==u'是'] = 1
data[data==u'高'] = 1
data[data != 1] = -1
x = data.iloc[:, :3].values.astype(int)
y = data.iloc[:, 3].values.astype(int)

from sklearn.tree import DecisionTreeClassifier as DTC #建立决策树模型，基于信息熵
dtc = DTC(criterion='entropy')
dtc.fit(x, y) #训练模型

# 导入相关函数，可视化决策树
# 导出的结果是一个dot文件，需要安装Graphviz才能将其转换为pdf或者png格式

from sklearn.tree import export_graphviz
x = pd.DataFrame(x)
with open('tree.dot', 'w') as f:
    f = export_graphviz(dtc, feature_names=x.columns, out_file=f)

