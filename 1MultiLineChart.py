import datetime
import pandas as pd 
import matplotlib.pyplot as plt 
#Baca dataser
dataset = pd.read_csv('data.csv')
#Buat kolom baru yg bertipe datetime dalam format '%Y-%m'
dataset['order_month'] = dataset['order_date'].apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
#Buat kolom GMV
dataset['gmv'] = dataset['item_price']*dataset['quantity']

#Buat Multi-Line Chart
dataset.groupby(['order_month','brand'])['gmv'].sum().unstack().plot()
plt.title('GMV Bulanan Tahun 2019 - Rincian berdasarkan Merek',loc='center', pad=30,fontsize=20, color='blue')
plt.xlabel('Bulan Pemesanan', fontsize=15)
plt.ylabel('Jumlah Total (dalam miliar)', fontsize=15)
plt.grid(color='darkgray',linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.gcf().set_size_inches(10,5)
plt.tight_layout()
plt.savefig('monthly_gmv.png', quality=95)
plt.show()