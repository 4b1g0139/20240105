class Luggage : #行李的類別
    def __init__(self,lid,weight,goairport,arriveairport,lname) :  #行李的建構子(目前的self，輸入行李的ID，輸入行李的重量，輸入行李出發機場，輸入行李目的地機場，輸入行李所屬旅客姓名)
        self.lid = lid                           #目前的self.輸入行李的ID
        self.weight = weight                   #目前的self.輸入行李的重量
        self.goairport = goairport             #目前的self.輸入行李出發機場
        self.arriveairport = arriveairport     #目前的self.輸入行李目的地機場
        self.lname = lname                       #目前的self.輸入行李所屬旅客姓名

l1=Luggage('ABCDE','10kg','臺南機場','桃園國際機場','黃子奇') #建立行李物件1(l1)，呼叫行李的建構子
print("行李的ID:",l1.lid)                                   #印出l1行李的ID
print("行李的重量:",l1.weight)                              #印出l1行李的重量
print("行李出發機場:",l1.goairport)                         #印出l1行李出發機場
print("行李目的地機場:",l1.arriveairport)                   #印出l1行李目的地機場
print("行李所屬旅客姓名:",l1.lname)                         #印出l1行李所屬旅客姓名

print("--------------------------")
class 登機證 :
    def __init__(self,name,id,time,number,seat,luggage,exit) : #登機證的建構子(目前的self，輸入旅客姓名，輸入登機證編號，輸入登機時間，輸入登機門編號，輸入座位位置，輸入行李件數，輸入行李出口)
        self.name = name                          #目前的self.輸入旅客姓名
        self.id = id                              #目前的self.輸入登機證編號
        self.time = time                          #目前的self.輸入登機時間
        self.number = number                      #目前的self.輸入登機門編號
        self.seat = seat                          #目前的self.輸入座位位置
        self.luggage = luggage                    #目前的self.輸入行李件數
        self.exit = exit                          #目前的self.輸入行李出口

b1=登機證('黃子奇','SA-25','9:00','1','G-2','1','E1')   #建立登機證物件1(b1)，呼叫登機證的建構子
print("旅客姓名:",b1.name)             #印出b1旅客姓名
print("登機證編號:",b1.id)             #印出b1登機證編號
print("登機時間:",b1.time)             #印出b1登機時間
print("登機門編號:",b1.number)         #印出b1登機門編號
print("座位位置:",b1.seat)             #印出b1座位位置
print("行李件數:",b1.luggage)          #印出b1行李件數
print("行李出口:",b1.exit)             #印出b1行李出口