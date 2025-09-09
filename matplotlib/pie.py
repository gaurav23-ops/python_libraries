import matplotlib.pyplot as plt

brands = ["apple ","oneplus","nokia","redmi"]
x = [20,22,21,3]
ex = [0,0,0,0.1]
plt.pie(x ,labels = brands , explode=ex , autopct="% .f")
plt.show()