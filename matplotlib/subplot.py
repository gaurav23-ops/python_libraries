import matplotlib.pyplot as plt
x =[1,2,3,4,5,6]
y =[20,30,20,40,25,20]
plt.subplot(1,2,1)
plt.plot(x,y)


x =[2,5,3,4,5,6]
y =[30,20,40,40,25,20]
plt.subplot(2,2,2)
plt.plot(x,y)


x =[6,2,3,5,5,6]
y =[10,30,50,30,25,20]
plt.subplot(2,3,2)
plt.plot(x,y)
plt.show()