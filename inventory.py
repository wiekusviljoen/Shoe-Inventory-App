#Import modules
from tabulate import tabulate

#Shoe class
class Shoe:
    
    # Constructor to initialize the attributes of the Shoe class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    # Method to get the cost of the shoes
    def get_cost(self):
        return self.cost

    # Method to get the quantity of the shoes
    def get_quantity(self): 
        return self.quantity

    # Method to return a string representation of the Shoe class
    def __str__(self):
        
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

# Initialize an empty list to store shoe objects
shoes_list = []


# Function to read data from the file and create Shoe objects
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as file:
            next(file)  # Skip the header line
            for line in file:
                data = line.strip().split(',')
                country, code, product, cost, quantity = data

                # Create Shoe objects and append to the shoes_list
                shoes_list.append(Shoe(country, code, product, float(cost), int(quantity)))
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Function to capture new shoe data and append it to the list
def capture_shoes(): 
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    try:
        cost = float(input("Enter cost: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input.")
        return

    shoes_list.append(Shoe(country, code, product, cost, quantity))


# Function to view all shoes
def view_all():
    if not shoes_list:
        print("No data available.")
        return

    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    table_data = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoes_list]
    print(tabulate(table_data, headers=headers, tablefmt="pretty"))


# Function to restock shoes and update the quantity in the file
def restock():
    if not shoes_list:
        print("No data available.")
        return

    min_quantity_shoe = min(shoes_list, key=lambda x: x.get_quantity())
    print(f"Lowest stock: {min_quantity_shoe}")

    try:
        add_quantity = int(input("Enter the quantity to restock: "))
        min_quantity_shoe.quantity += add_quantity
        print(f"Updated quantity for {min_quantity_shoe.product}: {min_quantity_shoe.quantity}")

        # Update the quantity in the file
        with open('inventory.txt', 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if min_quantity_shoe.code in line:
                    lines[i] = f"{min_quantity_shoe.country},{min_quantity_shoe.code},{min_quantity_shoe.product},{min_quantity_shoe.cost},{min_quantity_shoe.quantity}\n"

        with open('inventory.txt', 'w') as file:
            file.writelines(lines)

    except ValueError:
        print("Invalid input. Quantity must be an integer.")


# Function to search for a shoe by code and print its details
def search_shoe():
    if not shoes_list:
        print("No data available.")
        return

    search_code = input("Enter the code of the shoe to search: ")
    found_shoe = next((shoe for shoe in shoes_list if shoe.code == search_code), None)

    if found_shoe:
        print("Shoe found:")
        print(found_shoe)
    else:
        print(f"No shoe found with code {search_code}.")


# Function to calculate and print the value per item for each shoe
def value_per_item():
    if not shoes_list:
        print("No data available.")
        return

    for shoe in shoes_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product} - Value per item: {value}")


# Function to find and print the shoe with the highest quantity
def highest_qty():
    if not shoes_list:
        print("No data available.")
        return

    max_quantity_shoe = max(shoes_list, key=lambda x: x.get_quantity())
    print(f"The shoe with the highest quantity is for sale: {max_quantity_shoe}")

# Call the function to read the txt file
read_shoes_data()

# Menu and operations of choosing an option from the menu
while True:
    print("\nMenu:")
    print("1. Capture Shoes")
    print("2. View All Shoes")
    print("3. Restock")
    print("4. Search Shoe")
    print("5. Value per Item")
    print("6. Highest Quantity")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == '1':
            capture_shoes()
        elif choice == '2':
            view_all()
        elif choice == '3':
            restock()
        elif choice == '4':
            search_shoe()
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
