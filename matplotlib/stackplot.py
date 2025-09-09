import matplotlib.pyplot as plt

days =[1,2,3,4,5,6,7]

nop1 =[100,20,10,30,10,40,50]
nop2 =[20,40,20,30,50,40,50]
nop3 =[30,30,30,30,10,40,50]
plt.stackplot(days , nop1,nop2,nop3,colors= ["red","black","yellow"],labels= ["week1","week2","week3"])
plt.legend()
plt.show()