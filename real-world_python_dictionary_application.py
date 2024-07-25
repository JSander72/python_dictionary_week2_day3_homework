# Resturant Menu

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Soda": 1.99, "Coffee": 2.49}

restaurant_menu["Main Course"]["Steak"] = 17.99

del restaurant_menu["Starters"]["Bruschetta"]

print(restaurant_menu) 

# Customer Service Ticket Tracker

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket():
    ticket_id = f"Ticket{len(service_tickets) + 1}" 
    customer_name = input("Enter customer name: ")
    issue_description = input("Enter issue description: ")
    service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
    print(f"Ticket {ticket_id} opened successfully.")

def close_ticket():
    ticket_id = input("Enter ticket ID to close: ")
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = "closed"
        print(f"Ticket {ticket_id} closed successfully.")
    else:
        print(f"Ticket {ticket_id} not found.")

def display_tickets(status_filter=None):
    print("\nCustomer Service Tickets:")
    for ticket_id, ticket_info in service_tickets.items():
        if status_filter is None or ticket_info["Status"] == status_filter:
            print(f"{ticket_id}: {ticket_info}")

while True:
    print("\nSelect an action:")
    print("1. Open a new ticket")
    print("2. Close a ticket")
    print("3. Display all tickets")
    print("4. Display open tickets")
    print("5. Display closed tickets")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        open_ticket("open a ticket")
    elif choice == '2':
        close_ticket("close a ticket")
    elif choice == '3':
        display_tickets("all tickets")
    elif choice == '4':
        display_tickets("open")
    elif choice == '5':
        display_tickets("closed")
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")

