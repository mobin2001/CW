class URLHandler:
    def __init__(self) -> None:
        pass

    @classmethod
    def parse_url(cls,addres):
        addreslist = addres.split(":")
        domain = addreslist[1][2:].split("/")
        return addreslist[0], domain[0],domain[1],domain[2]
    
url = URLHandler()
print(url.parse_url("https://www.techtarget.com/searchnetworking/definition/URL"))