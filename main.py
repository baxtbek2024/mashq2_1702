class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

r = Rectangle(3, 4)
print(r.area()) 

#2-misol
class User:
    role = "member"

    def __init__(self, username):
        self.username = username

u1 = User("a")
u2 = User("b")
print(u1.role, u2.role)

User.role = "vip"
print(u1.role, u2.role)

#3-misol
class User:
    def __init__(self, username):
        self.username = username

u1 = User("alim")
u2 = User("sara")
u1.username = "alim007"
print(u1.username)  
print(u2.username)  

#4-misol
class Good:
    def __init__(self):
        self.items = []

g1 = Good()
g2 = Good()
g1.items.append(1)
print(g2.items) 
