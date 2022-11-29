
'''
 Variabe Use
 Precedance 
'''

Items = {
      "Mango" :20,
      "Phone" : 700,
     "Shampoo" : 10,
      "Rice" : 30,
      "Dal" : 8.5
}

itemlist = dict()
for item in Items:
    print (Items)

hasItem=True
while (hasItem):
    print("Enter the items name you want to buy:")
    item = input ()
    item_price = input ("Enter the item price :")
    #convert to number
    item_price=int(item_price)
    hasitem = input("Want to buy another (yes):")
                  
    if( hasitem == "yes"):
       hasitem = True
    else:
         hasitem = False
    itemlist[Items] = item_price

m=" " *3 + "Name" + " " *3 + "+" + " " *3 +"Cost" + " " *3 + " " *3 +"+" "GST" +" " *3
print (m)
print ("-"*len(m))
total =0
for item in itemlist:
    gst=items.get(item)
#price = cost (1+gst)
#cost = price / (1+gst)

    gst=gst/100
    cost = itemlist[item] / (1+gst)
    print (item +" " * 3 + "+" + " " *3 +
str(int(cost) )+ " " *3 + "+" + " " *3 +
str (float(gst*100) )+"%")
price=cost+(1+gst)
total = total + price

print("-"*len(m))
print( "Total" + " " * 3 +  "+" + " " * 9 + str(int(total)) + "rupees")
      
