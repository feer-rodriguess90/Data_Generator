import random

# list of informations
names = ["Mariah Leah", "Joshua Leah", "Alex Leah", "John Leah", "Kath Leah"]
emails = ["mariah.leah@email.com", "joshua.leah@email.com", "alex.leah@email.com", "john.leah@email.com", "kath.leah@email.com"]
phones = ["(51) 99898-9797", "(51) 99797-9898", "(51) 99696-9898", "(11) 99595-8585", "(11) 998686-8585"]
cities = ["Porto Alegre", "Florianopolis", "Caxias do Sul", "Sao Paulo", "Campinas"]
states = ["RS", "SC", "RS", "SP", "SP"]

def menu():
    print('Welcome to Test Data Generator - to end the program , type \"STOP\"')
    print('-' * 60)
    print("Choose one or more options separated by commas.")
    print('[1] - Name')
    print('[2] - E-mail')
    print('[3] - Phone')
    print('[4] - City')
    print('[5] - State')


def generate_random_data(choices):
    result = []
    for choice in choices:
        if choice == 1:
            result.append(random.choice(names))
        elif choice == 2:
            result.append(random.choice(emails))
        elif choice == 3:
            result.append(random.choice(phones))
        elif choice == 4:
            result.append(random.choice(cities))
        elif choice == 5:
            result.append(random.choice(states))
        else: 
            result.append("invalid choice")     
    return result
    
def save_to_file(data):
    with open('datas.txt', 'a') as file:
        for item in data:
            file.write(str(item) + '\n')

if __name__ == "__main__":
    while True:
        menu()
        user_input = input("Type one or more options(comma-separated): ")
        print('-' * 60)

        if user_input.upper() == 'STOP':
            print("Exiting the program.")
            break

        try:
            user_choices = [int(choice) for choice in user_input.split(',')]
            random_data = generate_random_data(user_choices)
            

            save_option = input("Do you want to save this information to a file? (y/n)").lower()
            if save_option == 'y':
                save_to_file(random_data)
                print("Successfully saved in the file 'datas.txt'")
            
            print(random_data)

        except ValueError:
            print("Invalid input. Please enter a number or \"STOP\".")