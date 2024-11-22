class Apparel:
    counter = 100 

    def __init__(self, price, item_type):
        Apparel.counter += 1
        self.__item_id = f"{item_type[0]}{Apparel.counter}" 
        self.__item_type = item_type
        self.__price = price

    
    def get_item_id(self):
        return self.__item_id

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_item_type(self):
        return self.__item_type

    def calculate_price(self):
       
        service_tax = self.__price * 0.05
        self.__price += service_tax


class Cotton(Apparel):
    def __init__(self, price, discount):
        super().__init__(price, "Cotton")  
        self.__discount = discount

    def get_discount(self):
        return self.__discount

    def calculate_price(self):
        
        super().calculate_price()

       
        discount_amount = self.get_price() * self.__discount
        self.set_price(self.get_price() - discount_amount)

       
        vat = self.get_price() * 0.05
        self.set_price(self.get_price() + vat)


class Silk(Apparel):
    def __init__(self, price):
        super().__init__(price, "Silk")
        self.__points = 0  

    def get_points(self):
        return self.__points

    def calculate_price(self):
       
        super().calculate_price()

        
        if self.get_price() > 10000:
            self.__points = 10 
        else:
            self.__points = 3  

       
        vat = self.get_price() * 0.10
        self.set_price(self.get_price() + vat)

    
    def display_details(self):
        print(f"Item ID: {self.get_item_id()}")
        print(f"Price: {self.get_price()}")
        print(f"Points: {self.get_points()}")



if __name__ == "__main__":
    
    cotton_item = Cotton(300, 0.05)  
    cotton_item.calculate_price()
    print("Cotton Apparel Details:")
    print(f"Item ID: {cotton_item.get_item_id()}")
    print(f"Final Price: {cotton_item.get_price()}")
    print(f"Discount: {cotton_item.get_discount() * 100}%\n")

    
    silk_item = Silk(12000)
    silk_item.calculate_price()
    print("Silk Apparel Details:")
    silk_item.display_details()

    
    silk_item2 = Silk(8000)
    silk_item2.calculate_price()
    print("\nAnother Silk Apparel Details:")
    silk_item2.display_details()
