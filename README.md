This project implements a fully functional online shopping cart system in Python. It demonstrates object-oriented programming (OOP) concepts including classes, objects, attributes, methods, encapsulation, lists, and modular program structure.
The program allows a user to:
Add items to the shopping cart
Remove items
Modify item quantities
View item descriptions
View the full shopping cart with totals
Quit from a menu-driven interface
This README describes the project structure, program behavior, and setup instructions.
📁 Project Files
File	Description
shopping_cart.py	Main Python program containing all classes and the menu system
README.md	Project documentation (this file)
🧱 Program Architecture
1. ItemToPurchase Class
Represents a single item the customer wants to buy.
Attributes:
item_name
item_description
item_price
item_quantity
Methods:
print_item_cost()
print_item_description()
2. ShoppingCart Class
Stores multiple ItemToPurchase objects.
Attributes:
customer_name
current_date
cart_items (list)
Methods include:
add_item()
remove_item()
modify_item()
get_num_items_in_cart()
get_cost_of_cart()
print_total()
print_descriptions()
3. Menu System
The main program includes a text-based menu:
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
The menu repeats until the user chooses q to quit.
▶️ Running the Program
1. Save the file
Save the program as:
shopping_cart.py
2. Run in Terminal
cd ~/Desktop
python3 shopping_cart.py
3. Follow the prompts
Example start:
Enter customer's name:
John Doe
Enter today's date:
November 29, 2025
Then the menu will appear.
📝 Example Output
OUTPUT SHOPPING CART
John Doe's Shopping Cart - November 29, 2025
Number of Items: 3
Milk 1 @ $5 = $5
Bread 2 @ $3 = $6
Total: $11
📸 Screenshots Included in Submission
Your submission document includes screenshots of:
Program start (customer name & date)
Adding an item
Removing an item
Modifying quantity
Viewing descriptions
Viewing full cart output
Quitting the program
💻 Technologies Used
Python 3.x
Object-Oriented Programming (OOP)
Terminal / Command Line
📚 Learning Objectives Demonstrated
Class design and instantiation
Constructor use
Using lists to store objects
Writing reusable methods
Input validation and program flow control
Building a complete interactive application
✔ Status
Project Completed Successfully
Meets all requirements for Portfolio Project Milestones 1, 2, and Final.
