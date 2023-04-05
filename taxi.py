taxies=4
stops=["a","b","c","d","e","f"]
initial_stop="a"
driver_list=[[0 for i in range(taxies)]for j in range(taxies)]
cab_details=[{"TaxiName":"Taxi1","TaxiID":2,"TaxiLocation":"a"},{"TaxiName":"Taxi2","TaxiID":2,"TaxiLocation":"a"},{"TaxiName":"Taxi3","TaxiID":3,"TaxiLocation":"a"}]
loc=0
def cabs():
    pass
def home():
    print("thanks")
def user():
    print("Welcome ")
    print("1.book taxi")
    n=int(input("Enter your choice:"))
    if n==1:
        book()

        
def book():
    n1=input("Enter your name:")    
    l1=input("Enter your location:")
    l2=input("Enter your destination:")
    t1=int(input("Enter your time:"))
    for i in cab_details:
        if i["TaxiLocation"]==l1:
            print("Yes")
            print("taxi"+ i["TaxiName"]+"booked")
            i["TaxiLocation"]=l2
            home()
            break
    else:
        check_cars(l1,available_list)

        
available_list=[]
def check_cars(l1,available_list):
    z=len(stops)
    for i in range(len(stops)):
        if stops[i]==l1:
            loc=stops.index(stops[i])
            print(loc)
    for j in range(len(stops)):
        if j!=loc:

            a=abs(loc-j)
            if a<=z:
                p=a,stops[j]
                available_list.append(p)
                a=z
    x=min(available_list)
    print(available_list)
    if available_list.count(x[0])>1:
        check_revenue()
    else:
        print(x)
    
def check_revenue():
    print("COde more")
user()



class cab:
    cp="A"
    ft=6
    er=0
stp=['A','B','C','D','E','F']
cl=[]
for i in range(4):
    c=cab()
    cl.append(c)
def booking():
    pp=input("pp: ")
    dp=input("dp: ")
    pt=int(input("pt: "))
    cout=0
    for i in cl:
        cout+=1
        if(i.cp==pp) and (i.ft<=pt) and (pt<=24):
            i.ft=pt+(stp.index(dp)-stp.index(pp))
            i.cp=dp
            i.er=i.er+(200*stp.index(dp)-200*stp.index(pp))
            print("cab booked your cab num is "+str(cout))
            home()
        elif(i.cp!=pp) and (i.ft<=pt) and (pt<=24) and (stp.index(i.cp)+i.ft<=pt):
            i.ft=pt+(stp.index(dp)-stp.index(pp))
            i.cp=dp
            i.er=i.er+(200*stp.index(dp)-200*stp.index(pp))
            print("cab booked your cab num is "+str(cout))
            home()
        else:
            pass
    else:
        print("all cab is full")
        home()
def cabdetail():
    cout=0
    for i in cl:
        cout+=1
        print("cab num "+str(cout)+" er: "+str(i.er)+" cp: "+i.cp+" ft: "+str(i.ft))
    home()
def home():
    print("1 to book,2 to cabd,3 to exit")
    n=int(input("enter here: "))
    if(n==1):
        booking()
    elif(n==2):
        cabdetail()
    else:
        quit()
home()