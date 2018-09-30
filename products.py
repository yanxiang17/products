# 記帳程式
# 輸入商品及價格,建立二維清單
# 存取二維清單

# 讀取檔案
import os

products = []
if os.path.isfile('products.csv'): # 檢查檔案
	print('yeah! 找到檔案了!')
	with open('products.csv', 'r', encoding = 'UTF-8') as f:
		for line in f:
			if '商品, 價格' in line:
				continue # 繼續
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到檔案......')

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = []
	p.append(name)
	p.append(price)		#p = [name, price]
	products.append(p)		#products.append([name, price])

# 印出所有購買記錄
for p in products:
	print(p[0], '的價格是:', p[1])		#印清單項目

# 寫入檔案
with open ('products.csv', 'w', encoding = 'UTF-8') as f:
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')