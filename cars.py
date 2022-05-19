import sqlite3

connection = sqlite3.connect('List_of_the_Cars')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE if not exists cars(manufacturer text, model text, color text, release_date integer)''')

def full_list():
    cursor.execute("SELECT * FROM cars")
    return cursor.fetchall()

def add_car():
    print("INSERT NEW CAR INFO:")
    manufacturer = input("Manufacturer: ")
    model = input("Model: ")
    color = input("Color: ")
    release_date = input("Release date: ")

    with connection:
        cursor.execute(f"INSERT INTO cars VALUES('{manufacturer}', '{model}', '{color}', '{release_date}')")
    print("CAR HAS BEEN ADDED SUCCESSFULLY!")

def update_car():
    print("INSERT CURRENT INFO:")
    current_manufacturer = input("Current manufacturer: ")
    current_model = input("Current model: ")
    current_color = input("Current color: ")
    current_release_date = input("Current release date: ")

    print("INSERT UPDATED INFO:")
    new_manufacturer = input("New manufacturer: ")
    new_model = input("New model: ")
    new_color = input("New color: ")
    new_release_date = input("New release date: ")

    with connection:
        cursor.execute(f"""UPDATE cars SET manufacturer = '{new_manufacturer}', model = '{new_model}', color = '{new_color}', release_date = '{new_release_date}' 
                    WHERE manufacturer = '{current_manufacturer}' AND model = '{current_model}' AND color = '{current_color}' AND release_date = '{current_release_date}'""")
    print("CAR HAS BEEN UPDATED SUCCESSFULLY!")

def remove_car():
    print("PLEASE ENTER CAR INFO WHICH YOU WANT TO BE REMOVED:")
    manufacturer = input("Manufacturer: ")
    model = input("Model: ")
    color = input("Color: ")
    release_date = input("Release date: ")

    with connection:
        cursor.execute(f"""DELETE from cars WHERE manufacturer = '{manufacturer}' AND model = '{model}' AND color = '{color}' AND release_date = '{release_date}'""")
    print("CAR HAS BEEN DELETED SUCCESSFULLY!")

print("WELCOME TO THE GARAGE!")
print("1) Show Full List of the Cars, 2) Insert New Car, 3) Update Current Car Info, 4) Remove Car from the List")
choice = int(input("PLEASE ENTER PREFERRED NUMBER: "))

if choice == 1:
    all_cars = full_list()
    print("ALL CARS:")
    print(all_cars)

elif choice == 2:
    insert = add_car()
    print(insert)

elif choice == 3:
    update = update_car()
    print(update)

elif choice == 4:
    delete = remove_car()
    print(delete)

else:
    print("ERROR!!!")

connection.commit()

connection.close()