


'''
 Variable use
 Precedance
'''

items = {
    'Mango' : 18,
    'Phone' : 18,
    'Shampoo' : 12,
    'Rice' : 5,
    'Dal':2.5
}

itemList = dict()
for item in items:
    print( item )

hasItem = True
while( hasItem ):
    print('Enter the items name you want to buy: ')
    item = input()
    item_price = input('Enter Item price: ')
#convert to number
    item_price = int( item_price )
    hasItem = input('Want to buy another(yes): ')
    if( hasItem == 'yes'):
        hasItem = True
    else:
        hasItem = False
    itemList[item] = item_price

m = " " * 3 + "Name" + " " * 3 + "+" + " " * 3 + "Cost" + " " * 3 + " " * 3 + "+" + "GST" + " " * 3
print(m)
print('-'*len(m))
total = 0
for item in itemList:
    gst = items.get(item) 
# price = cost (1 + gst)
# cost = price / ( 1 + gst )

    gst = gst / 100
    cost =  itemList[item] / ( 1 + gst )
    print( item + " " * 3 + "+" + " " * 3 + str(int(cost)) + " " * 3 + "+" + " " * 3 + str(float(gst*100)) + "%")
    price = cost + (1+gst)
    total = total + price

print('-'*len(m))
print( " Total" + " " * 3 + "+" + " " * 9 + str(int(total)) + " rupees")