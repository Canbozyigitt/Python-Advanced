import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4]
y=[1,2,3,4]
plt.plot(x,y,"--r")# kırmızı renkte ve parçalı(--) 
plt.axis([0,6,0,20]) # x ve y'nin max ve min değerlerini tutar. Ama x ve y yukarıda belirtilen değerleri alır .Bu sadece son gideceği yeri belirler.
plt.title("Grafik başlığı")
plt.show()  # diyagramı gösterir
