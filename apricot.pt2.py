import  pandas as pd
from  matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
# 设置画布大小
plt.rcParams['figure.figsize'] = (12, 14.5)
data = pd.read_csv('peach.CSV')
data2 = pd.read_csv('apricot.CSV')
Box1 = data["Apricot"]
Box2 = data["Peach"]
Box3 = data2["Apricot"]
Box4 = data2["Peach"]
# plt.grid(linestyle="",alpha=0)
# plt.grid(True)

#
plt.boxplot([Box1,Box2,Box3,Box4],
            patch_artist=True,
            showmeans=True,  # 显示均值点
            whis=6,
            widths=0.75,  # 箱体宽度
            boxprops={'color': 'black', 'facecolor': '#FFDF00'},  # 设置箱体属性
            flierprops={'marker': 'o', 'mfc': 'red', 'color': 'black'},  # 设置异常值属性
            meanprops={'marker': '+', 'mfc': 'black'},  # 设置均值点属性
            medianprops={'ls': '--', 'color': 'orange'},  # 设置中位数属性
            whiskerprops={'ls': '--', 'mfc': 'red', 'color': 'black'},

)



# 设置标题
plt.title('P. persica'+ 'P. armeniaca',fontsize=27,fontweight="bold",fontdict={'style':'italic'})
# # 不显示坐标轴
# plt.axis("off")
# # 不显示x轴刻度

plt.yticks([0.2,0.30,0.40,0.50,0.60,0.70,0.80],['$20$','$30$','$40$','$50$','$60$','$70$','$80$'])
# plt.ylim(0,1)
ax=plt.gca()
ax.set_xticklabels(['P. armeniaca','P. persica','P. armeniaca','P. persica'],fontsize = 25,font={'style':'italic'})

# # 设置字体
plt.rcParams['font.family']=['Times New Roman']
# # 显示百分比
# plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
# 设置字体大小
# plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
# # 设置列名
plt.ylabel("Proportion (%)",fontsize=25,fontweight="bold")
# plt.set_linewidth=('3.0')
# 画一道竖线隔开
# plt.vlines(2.5, 0, 0.85, colors = "black", linestyles = "solid",linewidth=1)
plt.axvline(2.5,color='black')
#
# ymajorLocator = MultipleLocator(0.1)
# ax.yaxis.set_major_locator(ymajorLocator)

plt.savefig("Peach.jpg",dpi=120)
plt.show()