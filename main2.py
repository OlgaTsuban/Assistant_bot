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
    
#write error
def print_error(message):
    print("Error: " , message)
    
#the main function
def main():
 #dictionary with the commands
    commands = {
        "hello": lambda: print("How can I help you?\n"),
        "good bye": lambda: print("Good bye!"),
        "close": lambda: print("Good bye!"),
        "exit": lambda: print("Good bye!"),
        "show all": lambda: print(show_all_contacts()),
        "add": lambda: print(add_contact(user_devided[1], user_devided[2])) if len(user_devided) == 3 else print_error("write name and phone."),
        "change": lambda: print(change_phone(user_devided[1], user_devided[2])) if len(user_devided) == 3 else print_error("write name and phone."),
        "phone": lambda: print(get_phone(user_devided[1])) if len(user_devided) == 2 else print_error("write name."),
    }
    while True:
        user_input = input("Write command \t")
        user_devided = user_input.split(maxsplit=2)
        result_text = ""
        for char in user_input:
            if char != " ":
                result_text += char.lower()
            else: break
            
        if result_text in commands:
            commands[result_text]()
            if result_text in ["close", "exit"]:
                break
        elif user_input.lower() in commands:
            commands[user_input.lower()]()
            if user_input.lower() == "good bye":
                break
        else:
            print("Invalid command. Use 'hello', 'add', 'change', 'phone', 'show all', 'good bye', 'close', or 'exit'")
    
if __name__ == '__main__':
    main()

