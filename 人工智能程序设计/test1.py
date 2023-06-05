class 


class Rect():
    def __init__(self, w,
                 h):
        self.width = w;
        self.height=h;

    def area(self):
        return self.width * self.height

class Square(Rect):
    def __init__(self,l):
        self.width=l;
        self.height=l;






r1=Rect(10,20)
print(r1.area())
r8=Square(4)
print(r8.area())
