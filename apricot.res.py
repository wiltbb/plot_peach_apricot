import  pandas as pd
from  matplotlib import pyplot as plt
from  matplotlib import  ticker
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
# import matplotlib.texmanager as texmanager
# 设置画布大小
plt.rcParams['figure.figsize'] = (12,13.5)
# plt.rcParams['axes.facecolor'] = 'lightgrey'
data = pd.read_csv('peach.CSV')
data2 = pd.read_csv('apricot.CSV')
Box1 = data["Apricot"]
Box2 = data["Peach"]
Box3 = data2["Apricot"]
Box4 = data2["Peach"]
plt.grid(linestyle="",alpha=0)
plt.grid(True)

#
plt.subplots(1,2,sharey=True)
ax1 = plt.subplot(1,2,1)
plt.boxplot([Box1,Box2],
            patch_artist=True,
            showmeans=True,  # 显示均值点
            whis=6,
            widths=0.5,  # 箱体宽度
            boxprops={'color': 'black', 'facecolor': 'white'},  # 设置箱体属性
            flierprops={'marker': 'o', 'mfc': 'red', 'color': 'black'},  # 设置异常值属性
            meanprops={'marker': '+', 'mfc': 'black'},  # 设置均值点属性
            medianprops={'ls': '--', 'color': 'black'},  # 设置中位数属性
            whiskerprops={'ls': '--', 'mfc': 'white', 'color': 'black'},
)
plt.rcParams['font.family']=['Times New Roman']
plt.ylabel("Proportion (%)",fontsize=25,fontweight="bold")
plt.yticks([0.2,0.30,0.40,0.50,0.60,0.70,0.80],['$20$','$30$','$40$','$50$','$60$','$70$','$80$'])
plt.yticks(fontsize=22)
plt.title('P. persica',fontsize=27,fontweight="bold",fontdict={'style':'italic'})
plt.xticks([1,2],['$P. armeniaca$','$P. persica$'],fontsize=25,font={'style':'italic'})

ax2 = plt.subplot(1,2,2)
plt.boxplot([Box3,Box4],
            patch_artist=True,
            showmeans=True,  # 显示均值点
            whis=6,
            widths=0.75,  # 箱体宽度
            boxprops={'color': 'black', 'facecolor': 'white'},  # 设置箱体属性
            flierprops={'marker': 'o', 'mfc': 'red', 'color': 'black'},  # 设置异常值属性
            meanprops={'marker': '+', 'mfc': 'black'},  # 设置均值点属性
            medianprops={'ls': '--', 'color': 'black'},  # 设置中位数属性
            whiskerprops={'ls': '--', 'mfc': 'white', 'color': 'black'},
)
plt.title('P. armeniaca',fontsize=27,fontweight="bold",fontdict={'style':'italic'})
plt.xticks([1,2],['$P. armeniaca$','$P. persica$'],fontsize=25,font={'style':'italic'})


plt.show()
plt.savefig('a.pdf')
