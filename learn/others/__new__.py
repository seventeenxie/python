class A(object):
    def __init__(self,a,b):
        print(self.a)
        print("init is running")
    def __new__(cls,a,b):
        cls.a=a
        cls.b=b
        print("__new__is running")
        return  object.__new__(cls)

a=A("ssssssa","a")
