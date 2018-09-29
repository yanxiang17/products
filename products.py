#輸入商品及價格,建立二維清單
#存取二維清單
products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = []
	p.append(name)
	p.append(price)		#p = [name, price]
	products.append(p)		#products.append([name, price])
print(products)		#印清單形式

for p in products:
	print(p)		#印清單形式
	print(p[0], '價格是:', p[1])		#印清單項目