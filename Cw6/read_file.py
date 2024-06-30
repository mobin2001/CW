
class FileHandler:
    def __init__(self) -> None:
        pass

    @classmethod    
    def read_file(cls,file_location):
        with open(file_location,"r") as fp:
            fp = fp.readlines()
            # return fp
            return fp
        
f1 = FileHandler()
print(f1.read_file("C:/Users/1/Desktop/CW\Cw6/test.txt"))        