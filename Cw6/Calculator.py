class Calculator:
    def __init__(self) -> None:
        pass

    @classmethod
    def add(cls,num1,num2) -> int: 
        return num1 + num2
    @staticmethod
    def add2(num1,num2):
        return num1 + num2
c = Calculator()
print(c.add2(10,2))

print(Calculator.add2(5,27))