import  pandas as pd
from  matplotlib import pyplot as plt
data = pd.read_csv('peach_demo1.CSV')
Box1=data["Apricot"]
Box2=data["Peach"]
fig1, (ax1,ax2)= plt.subplots(nrows=1,ncols=2,sharey=True)
ax1.plot(linestyle="--",alpha=0.3)
ax1.boxplot(
    Box1,
    patch_artist=True,
    showmeans=True,  # 显示均值点
    whis=8,
    widths=0.2,  # 箱体宽度
    boxprops={'color': 'black', 'facecolor': '#FFDF00'},  # 设置箱体属性
    flierprops={'marker': 'o', 'mfc': 'red', 'color': 'black'},  # 设置异常值属性
    meanprops={'marker': '+', 'mfc': 'black'},  # 设置均值点属性
    medianprops={'ls': '--', 'color': 'orange'},  # 设置中位数属性
    whiskerprops={'ls': '--', 'mfc': 'red', 'color': 'black'},
)
ax2.plot(linestyle="--",alpha=0.3)
ax2.boxplot(
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
ax1.legend()
ax1.set_title('Apricot')
# ax1.set_ylabel('')
ax2.legend()
ax2.set_title('Peach')
# ax2.set_xlabel('Ages')
# ax2.set_ylabel('')
plt.tight_layout()
plt.show()
