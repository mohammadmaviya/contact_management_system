#contact management system
contacts = {}

while True:
    
    print("\nContact Book App")
    print("1. Create contct")
    print("2. View contact")
    print("3. Update contact")
    print("4. Search contact")
    print("5. Count contact")
    print("6. Delete contact")
    print("7. Exit")

    choice = int(input("Enter your choice = "))
    print()

    if choice == 1:
        name = input("Enter name = ")
        if name in contacts:
            print(f"contact name {name} is already exists!")
        else: 
            age = input("Enter age = ")
            email = input("Enter email = ")
            mobile = input("Enter mobile number = ")
            contacts[name] = {"age" : int(age), "email" : email, "mobile" : int(mobile)}
            print(f"Contact name {name} has been created!")

    elif choice == 2:
            for name, detail in contacts.items():
                 print(f"Name : {name}")
                 print(f"Age : {detail['age']}")
                 print(f"Email : {detail['email']}")
                 print(f"Mobile No. : {detail['mobile']}")
                 print()

    elif choice == 3:
        name = input("Enter contact name to update = ")

        if name in contacts:
            new_age = int(input("Enter new age = "))
            new_email = input("Enter email = ")
            new_mobile = int(input("Enter mobile number = "))

            contacts[name]['age'] = new_age
            contacts[name]['email'] = new_email
            contacts[name]['mobile'] = new_mobile
            print(f"Contact name {name} has been updated!")
        else:
            print(f"Name : {name} not found in contact list!")

    elif choice == 4:
        search_name = input("Enter contact name to search = ")

        for name, detail in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Name : {search_name}")
                print(f"Age : {detail['age']}")
                print(f'email : {detail['email']}')
                print(f"mobile : {detail['mobile']}")

            else:
                print("name is not found!")

    elif choice == 5:
        print("Total contacts is ",len(contacts))

    elif choice == 6:
        name = input("Enter name of contact to delete = ")
        if name in contacts:
            del contacts[name]
            print(f"contact {name} is deleted successful!")

        else:
            print("contact not found in contact list!")

    elif choice == 7:
        break

    else: 
        print("invalid input")