from pydoc import plain


class Matrix:
    def __init__(self,r1,r2,r3,r4):
        self.r1=r1
        self.r2=r2
        self.r3=r3
        self.r4=r4

    def __add__(self, other):
        return Matrix(self.r1+other.r1,self.r2+other.r2,self.r3+other.r3,self.r4+other.r4)

    def __mul__(self, other):
        return Matrix(self.r1*other.r1 + self.r2*other.r3,self.r1*other.r2 + self.r2*other.r4,self.r3*other.r1 + self.r4*other.r3,self.r3*other.r2 + self.r4*other.r4)

    def __str__(self):
        return f"| {self.r1} {self.r2} | \n| {self.r3} {self.r4} |"

    def __repr__(self):
        return f"Matrix(r1={self.r1}, r2={self.r2}, r3={self.r3}, r4={self.r4})"


m=Matrix(1,2,3,4)
m2=Matrix(5,6,7,8)
print(m)
m3=m*m2
m4=m3+m
print('\n')
print(m3)
print('\n')
print(m4)

print(repr(m))