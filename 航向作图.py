import matplotlib.pyplot as plt
file=open("C:\\Users\\user\\Desktop\\航向.json",'r')
phid=[]
phit=[]
with file as file_obj:
    lines=file_obj.readlines()
for line in lines:
    line=line.rstrip()
    line=line.split(',')
    phid_data=line[-1].replace("]","")
    phit_data=line[1]
    phid.append(phid_data)
    phit.append(phit_data)
print(phid)
print(phit)
phid_plot=[]
phit_plot=[]
for num in phid:
    phid_plot.append(float(num))
for num in phit:
    phit_plot.append(float(num))
plt.plot(phid_plot,'r',label='phid')
plt.plot(phit_plot,'b',label='phit')
plt.xlabel('Time(s)')
plt.ylabel('Course(rad)')
plt.legend(bbox_to_anchor=(1,0),#图例边界框起始位置
                 loc="lower right",#图例的位置
                 ncol=1,#列数
                 mode="None",#当值设置为“expend”时，图例会水平扩展至整个坐标轴区域
                 borderaxespad=0,#坐标轴和图例边界之间的间距
                 shadow=False,#是否为线框添加阴影
                 fancybox=True)#线框圆角处理参数
plt.show()
