class Person : #人的類別
    def __init__ (self,name,weight,tall) : #人的建構子 (目前的self，輸入人的姓名，輸入人的體重，輸入人的身高)
        self.name = name    #目前的self.輸入人的姓名
        self.weight = weight  #目前的self.輸入人的體重
        self.tall = tall    #目前的self.輸入人的身高

p1=Person('黃子奇','61kg','172cm') #建立人物件1(p1)，呼叫人的建構子
print("姓名:",p1.name)      #印出p1的姓名
print("體重:",p1.weight)     #印出p1的體重
print("身高:",p1.tall)      #印出p1的身高
