with open ( 'data.txt','w') as f1:
    while True:
                   
       product_id=input('Enter the product id: ')
       print(product_id)
       if product_id == '' :
           break
       name=input ('the name of the item: ')
       print(name)
       price=input('Enter the price: ')
       print(price)
       f1.write(product_id + '\n')
       f1.write(name + '\n')
       f1.write(price + '\n')

sum=0
f2= open('data.txt','r') 
product_id=f2.readline()
while product_id != '':
    name=f2.readline()
    price=f2.readline()
    price=price.strip()
    print(price)
    #sum=sum+price
    sum=sum+float(price)
    product_id=f2.readline()
print('Total sum of the prices is ',sum)
f2.close()
