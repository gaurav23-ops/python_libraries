import matplotlib.pyplot as plt

x =["days1","days2","days3","days4","days5"]
y =[30,40,25,20,50]

plt.step(x, y, where="mid", label="Step Line")

# Overlay markers using plot
plt.plot(x, y, "o", label="Data Points")  # 'o' is the marker style
plt.show()