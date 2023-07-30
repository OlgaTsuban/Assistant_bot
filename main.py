#this dictionary contains name(names) and phone number(numbers)
phone_book = {}

#checks the errors in the functions
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Error: Invalid input. Please enter name and phone number."
        except IndexError:
            return "Error: Invalid input. Please enter name and phone number."
    return inner

#using the function can add new contact
@input_error
def add_contact(name, phone):
    if name in phone_book:
        raise ValueError
    phone_book[name]= phone
    return f"Contact {name} with phone {phone} has been added."
    
#using the function can modify the contact
@input_error
def change_phone(name, phone):
    if name not in phone_book:
        raise KeyError
    else:
        phone_book[name] = phone
        return f"Phone number for {name} has been changed to {phone}."
    
#using the function can get a phone if have a name
@input_error
def get_phone(name):
    if name not in phone_book:
        raise KeyError
    return (f"{name}'s phone number is {phone_book[name]}.")

#this show all contacts
@input_error
def show_all_contacts():
    if not phone_book:
        raise ValueError
    result = "Contacts:\n"
    for name, phone in phone_book.items():
        result += f"{name}: {phone}\n"
    return result

#the main function
def main():
    while True:
        user_input = input("Write command \t")
        user_devided = user_input.split(maxsplit=2)
        result_text = ""
        for char in user_input:
            if char != " ":
                result_text += char.lower()
            else: break
        if result_text == "hello":
            print("How can I help you? \n")
        elif user_input.lower() in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif user_input.lower() == 'show all':
            print(show_all_contacts())
        elif result_text == 'add':
            if len(user_devided) < 3:
                print("Error: write name and phone.")
            else:
                print(add_contact(user_devided[1], user_devided[2]))
        elif result_text == 'change':
            if len(user_devided) < 3:
                print("Error: write name and phone.")
            else:
                print(change_phone(user_devided[1], user_devided[2]))
        elif result_text == 'phone':
            if len(user_devided) < 2:
                print("Error: write name.")
            else:
                print(get_phone(user_devided[1]))
        else:
            print("Invalid command. Use 'hello', 'add', 'change', 'phone', 'show all', 'good bye', 'close', or 'exit'")

 
if __name__ == '__main__':
    main()
