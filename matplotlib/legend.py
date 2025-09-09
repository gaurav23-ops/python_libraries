import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[10,20,10,30,12,15]
y1=[20,10,20,30,15,25]
plt.figure(figsize=[5,3])
plt.plot(x,y,color= "red" ,label= "male")
plt.plot(x,y1,color= "black",label= "female")
plt.legend()
plt.show()