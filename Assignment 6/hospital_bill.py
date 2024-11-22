class Bill:
    
    def __init__(self, bill_id, patient_name):
        self.__bill_id = bill_id        
        self.__patient_name = patient_name  
        self.__bill_amount = 0  

    
    def calculate_bill_amount(self, consultation_fees, quantity_list, price_list):
        total_medicine_cost = 0
        for i in range(len(quantity_list)):
            total_medicine_cost += quantity_list[i] * price_list[i]  
        
        
        self.__bill_amount = consultation_fees + total_medicine_cost

    
    def get_bill_id(self):
        return self.__bill_id

    def get_patient_name(self):
        return self.__patient_name

    def get_bill_amount(self):
        return self.__bill_amount


if __name__ == "__main__":
    
    bill1 = Bill(101, "John Doe")

    
    consultation_fees = 500  
    quantity_list = [2, 1, 4] 
    price_list = [100, 150, 200] 

   
    bill1.calculate_bill_amount(consultation_fees, quantity_list, price_list)

    
    print("Bill ID:", bill1.get_bill_id())
    print("Patient Name:", bill1.get_patient_name())
    print("Total Bill Amount:", bill1.get_bill_amount())
