import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,2,100)
fig,axs=plt.subplots(2,2) # 2 satır 2 sütunluk bölüm oluşturduk.Yani 4 tane grafik oluşturduk.
fig.suptitle("grafik başlığı")

axs[0,0].plot(x,x,color="red") # ayrı ayrı 4 farklı grafik oluşturduk 
axs[0,1].plot(x,x**2,color="blue")
axs[1,0].plot(x,x**3,color="green")
axs[1,1].plot(x,x**4,color="yellow")
plt.show()