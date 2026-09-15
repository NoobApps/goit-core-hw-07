from book import AddressBook
from record import Record


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Already exists, update if needed"
    else:
        contacts[name] = phone
        return 'Contact added.'

def change_contact(args, contacts):
    name, phone= args
    contacts[name]=phone
    return "Contact updated"

def get_phone(args,contacts):
    name = args[0]
    if name in contacts:
            return contacts.get(name)
    else:
        return "Not Found"

def get_all(args,contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print (contacts)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command=="change":
            print(change_contact(args,contacts))
        elif command=="phone":
            print(get_phone(args,contacts))
        elif command=="all":
            print(get_all(args,contacts))

        else:
            print("Invalid command.")
        

if __name__ == "__main__":
    main()


# book = AddressBook()
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# book.add_record(john_record)
# john_record.remove_phone("1234567890")
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)
# john = book.find("John")
# john.edit_phone("5555555555", "1231231234")
# # book.delete('jj')
# print(book)