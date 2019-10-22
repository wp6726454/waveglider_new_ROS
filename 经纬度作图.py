import matplotlib.pyplot as plt
file=open("C:\\Users\\user\\Desktop\\经纬度.json",'r')
lon=[]
lat=[]
with file as file_obj:
    lines=file_obj.readlines()
for line in lines:
    line=line.rstrip()
    line=line.split(',')
    lat_data=line[-1].replace("]","")
    lon_data=line[0].replace("[","")
    lon.append(lon_data)
    lat.append(lat_data)
del lon[0]
del lat[0]
lon_plot=[]
lat_plot=[]
for num in lon:
    lon_plot.append(float(num))
for num in lat:
    lat_plot.append(float(num))
print(lon_plot)
print(lat_plot)
x1=121.44207
y1=31.03170
plt.plot(lon_plot,lat_plot)
plt.plot(x1,y1,'ro',markersize=15)
plt.xlabel('Longitude(°)')
plt.ylabel('Latitude(°)')
ax=plt.gca()
ax.get_xaxis().get_major_formatter().set_useOffset(False)
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

