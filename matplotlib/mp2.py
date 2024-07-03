import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,2,100)
plt.plot(x,x,label="linear") 
plt.plot(x,x**3,label="cubic")
plt.xlabel("x label")
plt.ylabel("y label")
plt.legend() # label dediğimiz grafiğin sol üstünde bulunan hangi çubuk hangi renk neyi ifade ediyo.

plt.show()