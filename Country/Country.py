def display_menu():
    print("Command Menu")
    print(" view --> View country name")
    print(" add --> Add a country")
    print(" delete --> Delete a country")
    print(" exit --> Exit the program")

def prepopulate_dictionary():
    return {
        "US": "United States", "CAN": "Canada", "AUS": "Australia"
    }

def view_country(country_dict):
    print("Country codes:")
    for key in country_dict:
        print(key)
    user_input = input("Enter a country code: ")
    if user_input in country_dict:
        print("Country:", country_dict[user_input])
    else:
        print("Invalid country code!")

def add_country(country_dict):
    country_code = input("Enter a country code: ")
    country_name = input("Enter the country name: ")
    if country_code in country_dict:
        print("Country code already exists!")
    else:
        country_dict[country_code] = country_name
        print( country_name +" was added. ")

def delete_country(country_dict):
    country_code = input("Enter a country code: ")
    if country_code in country_dict:
        del country_dict[country_code]
        print(country_code +" was deleted.")
    else:
        print("Invalid country code!")

def main():
    country_dict = prepopulate_dictionary()
    display_menu()
    while True:
        
        choice = input("\nCommand: ")
        
        if choice == "view":
            view_country(country_dict)
        elif choice == "add":
            add_country(country_dict)
        elif choice == "delete":
            delete_country(country_dict)
        elif choice == "exit":
            print("Exiting program.")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
