from datetime import datetime

name=input("Enter your name:")
#LISTS of items
lists='''
Rice        Rs 20/Kg
Sugar       Rs 30/Kg
salt        Rs 20/Kg
Oil         Rs 80/liter
Paneer      Rs 110/Kg
Maggi       Rs 50/Kg
Boost       Rs 85/each
colagate    Rs 85/each
Cashew nuts Rs 500/Kg
'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilists=[]
qlist=[]
plist=[]

#rates for itens
items={'rice':20,
'sugar':30,
'salt':20,
'oil':80,
'paneer':110,
'maggie':50,
'boost':90,'colagate':85,
'cashewnuts':500}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quanitity=int(input("Enter your quanitity:"))
        if item in items.keys():
            price=quanitity*(items[item])
            pricelist.append((item,quanitity,items,price))
            totalprice+=price  
            ilists.append(item) 
            qlist.append(quanitity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice            
        else:
            print("sorry your entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"kasulu supermarket",25*"=")
            print(28*" ","wanparthy")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quanitity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',8*'5*',ilists[i],3*' ',qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount','Rs',totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalalAmount','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting")
            print(75*"-")

