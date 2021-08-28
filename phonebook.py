# Phonebook database management program using Command Line
"""
This program maintains a database of names and phone numbers in a csv
file called myphones.csv.  It is run from the command line and is menu
driven.

"""
#To check existance of file
import os
#To work with CSV file
import csv


phones = [] #Global variable list storing list phone data from csv and updated data 
name_pos = 0
phone_pos = 1
phone_header = [ 'Name', 'Phone Number'] #Header for displaying data

def proper_menu_choice(which):
    """
    Checks whether choice is valid or not.
    And returns True if it is valid otherwise False
    which: user choice
    """
    if not which.isdigit():
        print ("'" + which + "' needs to be the number of a phone!")
        return False
    which = int(which)
    if which < 1 or which > len(phones):
        print ("'" + str(which) + "' needs to be the number of a phone!")
        return False
    return True
    
def reorder_phones():
    """
    Sorts the data present in phones with their names.
    """
    global phones       # this insures that we use the one at the top
    phones.sort()

def delete_phone(which):
    """
    Delete the data present at given position in phonebook.
    which: position at which data is to be deleted
    """
    if not proper_menu_choice(which):
        return
    which = int(which)

    del phones[which-1]
    print( "Deleted phone #", which)

def edit_phone(which):
    """
    Edit or update the data at given position.
    which: position at which data is to be updated/edited.
    """
    if not proper_menu_choice(which):
        return
    which = int(which)
        
    phone = phones[which-1]
    print("Enter the data for a new phone. Press <enter> to leave unchanged.")
    
    print(phone[name_pos])
    newname = input("Enter phone name to change or press return: ")
    if newname == "":
        newname = phone[name_pos]
        
    print(phone[phone_pos])    
    newphone_num = input("Enter new phone number to change or press return: ")
    if newphone_num == "":
        newphone_num = phone[phone_pos]
            
    phone = [newname, newphone_num]
    phones[which-1] = phone

  
def save_phone_list():
    """
    Save the data frome the phones into csv file i.e myphones.csv
    """
    f = open("myphones.csv", 'w', newline='')
    for item in phones:
        csv.writer(f).writerow(item)
    f.close()
  
def load_phone_list():
    """
    Load all data present in myphones.csv to phones.
    """
    if os.access("myphones.csv",os.F_OK):
        f = open("myphones.csv")
        for row in csv.reader(f):
            phones.append(row)
        f.close()

def show_phones():
    """
    Shows/prints the data from the phones(all list elements) to screen using showphone function.
    """
    show_phone(phone_header, "")
    index = 1
    for phone in phones:
        show_phone(phone, index)
        index = index + 1
    print()

def show_phone(phone, index):
    """
    Print the data i.e phone_name and phone_no. from list with proper index with formeted string.
    phone: list of name and no. from phones list
    index: index position (index in list + 1)
    """
    outputstr = "{0:>3}  {1:<20}  {2:>16}"
    print(outputstr.format(index, phone[name_pos], phone[phone_pos]))

def create_phone():
    """
    Creates new entry in phonebook.
    """
    print("Enter the data for a new phone:")
    newname = input("Enter name: ")
    newphone_num = input("Enter phone number: ")
    phone = [newname,newphone_num]
    phones.append(phone)
    
def menu_choice():
    """ Find out what the user wants to do next. """
    print("Choose one of the following options?")
    print("   s) Show")
    print("   n) New")
    print("   d) Delete")
    print("   e) Edit")
    print("   q) Quit")
    print("   r) Reorder")
    choice = input("Choice: ")    
    if choice.lower() in ['n','d', 's','e', 'q','r']:
        return choice.lower()
    else:
        print(choice +"?")
        print("Invalid option")
        return None


def main_loop():
    """
    Infinite loop which starts with loading data from csv and ends with saving the data back in csv.
    Ends when user choose to end.
    """
    
    load_phone_list()
    
    while True:
        choice = menu_choice()
        if choice == None:
            continue
        if choice == 'q':
            print( "Exiting...")
            break     # jump out of while loop
        elif choice == 'n':
            create_phone()
        elif choice == 'd':
            which = input("Which item do you want to delete? ")
            print("which is ", which)
            delete_phone(which)
        elif choice == 's':
            show_phones()
        elif choice == 'e':
            which = input("Which item do you want to edit? ")
            print("which is ", which)
            edit_phone(which)
        elif choice == 'r':
            reorder_phones()
        else:
            print("Invalid choice.")
            
    save_phone_list()
    

# The following makes this program start running at main_loop() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()