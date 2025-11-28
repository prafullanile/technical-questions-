class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def show(self):
        print(self.brand,self.model)

c=car("toyota", "fortuner")
print(c.brand)
print(c.model)