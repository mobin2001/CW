class MathUtil:
    def __init__(self) -> None:
        pass
    @classmethod
    def prime_number(cls,number):
        count = 0
        for x in range (2,number):
            if number%x==0:
                count +=1

        if count==0:
            return "prime"
        else:
            return "not prime"

n = MathUtil()
print(n.prime_number(7))