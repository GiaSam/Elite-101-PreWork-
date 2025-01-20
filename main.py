# Chatbot-Project
print("Hello! Welcome to the Sundown Bracelets Chatbot. Please look for the answers to any questions you")
print ("may have here before attempting to direct them to management. :) ")
name = input ("Please enter your name - ")
age = input ("Please enter your age - ")
print("------------------")
menu_options = [' Bracelet Catalog', ' Bracelet Prices', ' Customization', ' Gifts', ' Shipping', ' Exit']
for options in menu_options:
   print(options)
def user_selection():
    in_use = True
user_choice = (input("How can we help you?: "))
if user_choice == "Bracelet Catalog": #Show user bracelets on sale
    print("Bracelet Catalog")
if user_choice == "Bracelet Prices": # show the prices of bracelets on sale
    print("Bracelet Prices")
if user_choice == "Customization": #Take user to customization page
    print("Customization")
if user_choice == "Gifts": #Take user to gifts page
    print("Gifts")
if user_choice == "Shipping": #Take user to page going over shipping details
    print("Shipping")
if user_choice == "Exit": #
    print("Exiting Sundown Bracelets Chatbot...thanks for visiting!")
in_use = False
