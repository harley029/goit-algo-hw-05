from colorama import Fore, Style

# функція виводу іʼмя у відповідях боту
def name_out (name:str):
    return f"{Fore.LIGHTBLUE_EX}{name.capitalize()}{Fore.RESET}"

# декоратор    
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Будь ласка, введить імʼя та номер телефону."
        except KeyError:
            return "Іʼмя не знайдено."
        except IndexError:
            return f"{Fore.RED}Error:{Fore.RESET} Невірна кількість аргументів."
    return inner

# функція обробки вводу від користувача
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# функція додавання контакту до списку    
@input_error
def add_contact(args, contacts):
    # перевірка наявності вірної кількості аргументів
        name, phone = args
        # перевірка існування імені в списку перед його додаванням до нього з наступною обробкою
        if name in contacts:
            warn = input(f"{Fore.YELLOW}Warning:{Fore.RESET} The contact {name_out(name)} is already exist. Overwrite? (y/n) ")
            comnd, *argum = parse_input(warn)
            if comnd in ["yes", "y"]:
                contacts[name] = phone
                return f"Contact {name_out(name)} is changed."
            else: 
                return f"Contact {name_out(name)} is not changed."
        contacts[name] = phone
        return f"Contact {name_out(name)} is added." 

# функція виводу номеру телефону за імʼям контакту
def show_phone(args, contacts):
    name=args[0]
    if name in contacts:
        return contacts[name]
    return f"Contact {name_out(name)} Not found"
# Варіант з лекції:
# return contacts[name] if name in contacts.keys() else 'Not found' 

# функція зміни номеру телефону контакту

@input_error
def change_phone(args, contacts):
    # перевірка наявності вірної кількості аргументів
        name=args[0]
        # Перевірка наявності імені в списку перед його зміною
        if name in contacts:
            contacts[name]=args[1]
            return f"Contact {name_out(name)} changed"
        return f'{Fore.YELLOW}Warning:{Fore.RESET} Contact {name_out(name)} is not found'

# функція виводу всіх контактів    
def all_contacts(contacts):
    if contacts == {}:
        return f"{Fore.YELLOW}Warning:{Fore.RESET}Contacts list is empty."
    else:
        return f"{contacts}"

def main():
    contacts = {}
    print(f"{Fore.GREEN}Welcome to the assistant bot!{Fore.RESET}")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            print(f"{Fore.GREEN}Good bye!{Fore.RESET}")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        else:
            print(f"{Fore.RED}Error:{Fore.RESET} Невірна команда.")

if __name__ == "__main__":
    main()
    