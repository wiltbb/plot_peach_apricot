import pandas as pd
from matplotlib import pyplot as plt
# import matplotlib.texmanager as texmanager

apricot = pd.read_csv("res_apricot_split_by_chr.csv")
peach = pd.read_csv("res_peach_split_by_chr.csv")

Apricot_Box1 = apricot["chr1"]
Apricot_Box2 = apricot["chr2"]
Apricot_Box3 = apricot["chr3"]
Apricot_Box4 = apricot["chr4"]
Apricot_Box5 = apricot["chr5"]
Apricot_Box6 = apricot["chr6"]
Apricot_Box7 = apricot["chr7"]
Apricot_Box8 = apricot["chr8"]
Apricot_Box9 = apricot["Pp01"]
Apricot_Box10 = apricot["Pp02"]
Apricot_Box11 = apricot["Pp03"]
Apricot_Box12 = apricot["Pp04"]
Apricot_Box13 = apricot["Pp05"]
Apricot_Box14 = apricot["Pp06"]
Apricot_Box15 = apricot["Pp07"]
Apricot_Box16 = apricot["Pp08"]

Peach_Box1 = peach["chr1"]
Peach_Box2 = peach["chr2"]
Peach_Box3 = peach["chr3"]
Peach_Box4 = peach["chr4"]
Peach_Box5 = peach["chr5"]
Peach_Box6 = peach["chr6"]
Peach_Box7 = peach["chr7"]
Peach_Box8 = peach["chr8"]
Peach_Box9 = peach["Pp01"]
Peach_Box10 = peach["Pp02"]
Peach_Box11 = peach["Pp03"]
Peach_Box12 = peach["Pp04"]
Peach_Box13 = peach["Pp05"]
Peach_Box14 = peach["Pp06"]
Peach_Box15 = peach["Pp07"]
Peach_Box16 = peach["Pp08"]

plt.rcParams['figure.figsize'] = (24, 13.5)
plt.grid(linestyle="", alpha=0)
plt.grid(True)
plt.subplots(1, 2, sharey=True)
group1 = [Apricot_Box1, Apricot_Box2, Apricot_Box3, Apricot_Box4, Apricot_Box5, Apricot_Box6, Apricot_Box7, Apricot_Box8,
          Apricot_Box9, Apricot_Box10, Apricot_Box11, Apricot_Box12, Apricot_Box13, Apricot_Box14, Apricot_Box15, Apricot_Box16]
'''colors = ['grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'lightgrey',
          'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey']'''
ax1 = plt.subplot(1, 2, 1)
box = plt.boxplot(group1,
                  patch_artist=True,
                  showmeans=True,  # 显示均值点
                  whis=6,
                  widths=0.5,  # 箱体宽度
                  boxprops={'color': 'black', 'facecolor': 'white'},  # 设置箱体属性
                  flierprops={'marker': 'o', 'mfc': 'red',
                              'color': 'black'},  # 设置异常值属性
                  meanprops={'marker': '+', 'mfc': 'black'},  # 设置均值点属性
                  medianprops={'ls': '--', 'color': 'black'},  # 设置中位数属性
                  whiskerprops={'ls': '--', 'mfc': 'white', 'color': 'black'},
                  )
plt.rcParams['font.family'] = ['Times New Roman']
plt.ylabel("Proportion (%)", fontsize=25, fontweight="bold")
plt.yticks([0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16], [
           '$2$', '$4$', '$6$', '$8$', '$10$', '$12$', '$14$', '$16$'])
plt.yticks(fontsize=22)
# 'P. persica'
plt.title('P. armeniaca', fontsize=27, fontweight="bold",
          fontdict={'style': 'italic'})
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], ['$chr1$', '$chr2$', '$chr3$', '$chr4$', '$chr5$', '$chr6$', '$chr7$', '$chr8$',
                                                                     '$Pp01$', '$Pp02$', '$Pp03$', '$Pp04$', '$Pp05$', '$Pp06$', '$Pp07$', '$Pp08$'])
# '$chr1$','$chr2$','chr3','chr4','chr5','chr6','chr7','chr8','Pp01','Pp02','Pp03','Pp04','Pp05','Pp06','Pp07','Pp08',fontsize=25,font={'style':'italic'}
# for box, color in zip(box['boxes'], colors):
#     box.set_facecolor(color)
# plt.vlines(8.5,0,0.5,colors = 'r',linestyles='dashed')
plt.axvline(8.5,color='black')
font1 = {'size':24,'weight':'bold','style':'italic'}
plt.xlabel("     P. armeniaca                    P. persica          ",loc='center',fontdict=font1,labelpad=2)

plt.axvspan(8.5,16.5,facecolor='grey',alpha = 0.5)



ax2 = plt.subplot(1, 2, 2)
group2 = [Peach_Box1, Peach_Box2, Peach_Box3, Peach_Box4, Peach_Box5, Peach_Box6, Peach_Box7, Peach_Box8,
          Peach_Box9, Peach_Box10, Peach_Box11, Peach_Box12, Peach_Box13, Peach_Box14, Peach_Box15, Peach_Box16]
box2 = plt.boxplot(
    group2,
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
# 'P. armeniaca'
plt.title('P. persica', fontsize=27, fontweight="bold",
          fontdict={'style': 'italic'})
# plt.xticks([1,2],['$P. armeniaca$','$P. persica$'],fontsize=25,font={'style':'italic'})
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], ['$chr1$', '$chr2$', '$chr3$', '$chr4$', '$chr5$', '$chr6$', '$chr7$', '$chr8$',
                                                                     '$Pp01$', '$Pp02$', '$Pp03$', '$Pp04$', '$Pp05$', '$Pp06$', '$Pp07$', '$Pp08$'])

# for box, color in zip(box2['boxes'], colors):
#     box.set_facecolor(color)
plt.axvline(8.5,color='black')
font1 = {'size':24,'weight':'bold','style': 'italic'}
plt.xlabel("     P. armeniaca                    P. persica          ",loc='center',fontdict=font1,labelpad=2)
plt.axvspan(8.5,16.5,facecolor='grey',alpha = 0.5)





plt.show()
# 
# plt.savefig('split_by_chr.pdf')
