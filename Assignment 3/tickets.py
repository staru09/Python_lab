def generate_ticket_numbers(src, dest, passenger_count):
    airline = "AI"
    src_code = src[:3].upper()  
    dest_code = dest[:3].upper()  
    starting_number = 101

    ticket_numbers = []
    for i in range(passenger_count):
        ticket_number = f"{airline}:{src_code}:{dest_code}:{starting_number + i}"
        ticket_numbers.append(ticket_number)

    return ticket_numbers[-5:]

src = input("Enter the source city: ")
dest = input("Enter the destination city: ")
passenger_count = int(input("Enter the number of passengers: "))

ticket_numbers = generate_ticket_numbers(src, dest, passenger_count)
print("Generated Ticket Numbers:")
for ticket in ticket_numbers:
    print(ticket)
