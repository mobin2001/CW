class Temperature:
    def __init__(self,temperature):
        self.temperature = temperature

    def celsius_to_fahrenheit(self):
        return (self.temperature * (9/5)) + 32
    
    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * (5/9)
    
    @classmethod
    def fahrenheit_to_celsiuss(cls,fahrenheat):
        return 
        