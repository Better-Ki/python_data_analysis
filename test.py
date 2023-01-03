# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.linspace(0, 10, 1000)
# y = np.sin(x) + 1
# z = np.cos(x**2) + 1
#
# plt.rcParams['font.sans-serif']= ['SimHei']
# plt.figure(figsize=(8, 4))
# plt.plot(x, y, label='$\sin x+1$',color='red', linewidth=2)
# plt.plot(x, z, 'b--', label='$\cos x^2+1$')
# plt.xlabel('Time(s)')
# plt.ylabel('Volt')
# plt.title('一个简单的例子')
# plt.ylim(0, 2.2)
# plt.legend()
# plt.show()

# import pandas as pd
#
# s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# d = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
# d2 = pd.DataFrame(s)
# print(d.head())
# d.describe()
# # pd.read_excel('data.xls')
# # pd.read_csv('data.csv', encoding='utf-8')

# from statsmodels.tsa.stattools import  adfuller as ADF
# import numpy as np
# ADF(np.random.rand(100))

from sklearn import datasets, svm


iris = datasets.load_iris()
print(iris.data.shape)

clf = svm.LinearSVC()
clf.fit(iris.data, iris.target)
clf.predict([[5.0, 3.6, 1.3, 0.25]])
print(clf.coef_)
