# pasta grafiği

import matplotlib.pyplot as plt

goal_types='Penaltı','Kaleye atılan şut','Serbest vuruş'

goals=[12,35,7]
colors=['y','r','b']
plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.05,0.05,0.05))
plt.show()
# shadow gölgelendirmeye yarar
#expolde bölgeler arası boşluğu ayarlar