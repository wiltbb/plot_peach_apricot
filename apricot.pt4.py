import  pandas as pd
from  matplotlib import pyplot as plt
from  matplotlib import  ticker
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
# 设置画布大小
plt.rcParams['figure.figsize'] = (12,13.5)
plt.rcParams['axes.facecolor'] = 'lightgrey'
data = pd.read_csv('peach.CSV')
data2 = pd.read_csv('apricot.CSV')
Box1 = data["Apricot"]
Box2 = data["Peach"]
Box3 = data2["Apricot"]
Box4 = data2["Peach"]
fig1, (ax1,ax2)= plt.subplots(nrows=1,ncols=2,sharey=True)
ax1.boxplot(
    [Box1,Box2],
    patch_artist=True,
    showmeans=True,  # 显示均值点
    whis=6,
    widths=0.5,  # 箱体宽度
    boxprops={'color': 'black', 'facecolor': 'green'},  # 设置箱体属性
    flierprops={'marker': 'o', 'mfc': 'red', 'color': 'black'},  # 设置异常值属性
    meanprops={'marker': '+', 'mfc': 'black'},  # 设置均值点属性
    medianprops={'ls': '--', 'color': 'orange'},  # 设置中位数属性
    whiskerprops={'ls': '--', 'mfc': 'red', 'color': 'black'},
)

ax2.boxplot(
    [Box3,Box4],
    patch_artist=True,
    showmeans=True,  # 显示均值点
    whis=6,
    widths=0.75,  # 箱体宽度
    boxprops={'color': 'black', 'facecolor': 'magenta'},  # 设置箱体属性
    flierprops={'marker': 'o', 'mfc': 'red', 'color': 'black'},  # 设置异常值属性
    meanprops={'marker': '+', 'mfc': 'black'},  # 设置均值点属性
    medianprops={'ls': '--', 'color': 'orange'},  # 设置中位数属性
    whiskerprops={'ls': '--', 'mfc': 'red', 'color': 'black'},
)

plt.show()
plt.savefig('a.pdf')