def calculate_bill(gems, prices, purchase_list):
    total_bill = 0
    
    for gem, quantity in purchase_list.items():
        if gem in gems:
            total_bill += prices[gems.index(gem)] * quantity
        else:
            return -1

    if total_bill > 30000:
        total_bill *= 0.95
    
    return total_bill


gems = ["Ruby", "Emerald", "Sapphire", "Diamond", "Opal"]
prices = [5000, 7000, 6000, 10000, 4000]


purchase_list = {}
while True:
    gem = input("Enter the gem name (or 'done' to finish): ")
    if gem.lower() == 'done':
        break
    quantity = int(input(f"Enter the quantity for {gem}: "))
    purchase_list[gem] = quantity

bill_amount = calculate_bill(gems, prices, purchase_list)

if bill_amount == -1:
    print("One or more gems are not available in the store.")
else:
    print(f"The total bill amount is: Rs.{bill_amount}")
