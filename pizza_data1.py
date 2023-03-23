import pandas as pd
# function to import data from any csv file
def import_data():
    filename = input("Enter file name: ")
    try:
        data = pd.read_csv(filename)
        print("File imported successfully!")
        return data
    except FileNotFoundError:
        print("File not found! Please re-enter")
        return None

def show_data(data):
    if data is None:
        print("No data to show!")
        return
    rows = int(input("Enter the number of rows to display: "))
    cols = int(input("Enter the number of columns to display: "))
    print(data.iloc[:rows, :cols])
# function to remove blank/null values from data
def remove_blanks(data):
    if data is None:
        print("No data to remove blanks from!")
        return
    choice = input("Are you sure you want to remove all blank values? (yes/no): ")
    if choice.lower() == "yes":
        print("Processing data...")
    data.dropna(inplace=True)
    data.to_csv('pizza_data(fixed).csv', index=False)
    print("Remove successfully!")
    return data

# function to remove blank/null values from data
def exit_program():
    choice = input("Are you sure you want to exit? (y/n) ")
    if choice.lower() == "y":
        print("Goodbye!")
        exit()
    elif choice.lower() == "n":
        return
    else:
        print("Invalid choice!")
        exit_program()

while True:
    print("\nWelcome to the Python Dashboard!")
    print("* 1. Import data       *")
    print("* 2. Show data         *")
    print("* 3. Remove blanks     *")
    print("* 4. Exit              *")
    print("It made by Group 1.If you want full code, please contact us because it's free!!!")

    choice = input("Please enter your choice (1-4): ")
    if choice == "1":
        data = import_data()
    elif choice == "2":
        show_data(data)
    elif choice == "3":
        print("Processing data...")
        data = remove_blanks(data)
    elif choice == "4":
        exit_program()
    else:
        print("Invalid choice! Please select again")
