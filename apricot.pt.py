import matplotlib.pyplot as plt
import  pandas as pd
data = pd.read_csv("res_115.csv")

plt.subplot(1,2,1)
Box1=data["Apricot"]
# 提取apricot的数据
plt.grid(linestyle="--",alpha=0.3)
plt.boxplot(
            Box1,
            patch_artist=True,
            showmeans=True,    #显示均值点
            whis=8,
            widths=0.2,      #箱体宽度
            boxprops={'color': 'black', 'facecolor': '#FFDF00'},   #设置箱体属性
            flierprops={'marker': 'o', 'mfc': 'red', 'color': 'black'},    #设置异常值属性
            meanprops={'marker': '+', 'mfc': 'black'},      #设置均值点属性
            medianprops={'ls': '--', 'color': 'orange'},      #设置中位数属性
            whiskerprops={'ls': '--', 'mfc': 'red', 'color': 'black'},  #设置触须属性
)
plt.title('Apricot')
plt.xticks([])
# plt.savefig('res_apricot.png',c='c')
# plt.figure()
# plt.show()

plt.subplot(1,2,2)
Box2=data["Peach"]
plt.grid(linestyle="--",alpha=0.3)
plt.boxplot(
            Box2,
            patch_artist=True,
            showmeans=True,
            whis=8,
            widths=0.2,
            boxprops={'color': 'black', 'facecolor': '#2C4096'},
            flierprops={'marker': 'o', 'mfc': 'red', 'color': 'black'},
            meanprops={'marker': '+', 'mfc': 'black'},
            medianprops={'ls': '--', 'color': 'orange'},
            whiskerprops={'ls': '--', 'mfc': 'red', 'color': 'black'}
)
plt.title('Peach')
plt.xticks([])
# plt.figure()


# plt.show()
plt.savefig('res_api.png',c='c')
plt.suptitle('b')
plt.show()