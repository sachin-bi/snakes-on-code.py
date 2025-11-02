# Method Resolution Order - MRO
# its all about simplyfing the inheritence of the classes


class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")


class D(B, C):
    # def show(self):
        # print("D")
        pass


obj = D()
obj.show()
print(D.mro())
