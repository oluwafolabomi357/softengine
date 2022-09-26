class House:
    def __init__(self, name, form, window):
        self.window = window
        self.form = form
        self.name = name
    def show(self):
        return f"{self.name} is a {self.form} with {self.window} windows"
house1 = House("house1", "bungalow", "4")
house_1 = house1.show()
print(house_1)

house2 = House("house2", "duplex", "5")
house_2 = house2.show()
print(house_2)

house3 = House("house3", "decker", "6")
house_3 = house3.show()
print(house_3)

house4 = House("house4", "storey", "7")
house_4 = house4.show()
print(house_4)

house5 = House("house5", "skyscrapper", "10")
house_5 = house5.show()
print(house_5)
            

        

            
        
