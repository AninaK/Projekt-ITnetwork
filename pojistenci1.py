class InsuredPerson:
    def __init__(self, name, surname, age, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.surname}, Age: {self.age}, Phone: {self.phone}"

class InsuranceDatabase:
    def __init__(self):
        self.insured_people = []

    def add_person(self, person):
        self.insured_people.append(person)

    def display_all(self):
        if self.insured_people:
            for person in self.insured_people:
                print(person)
        else:
            print("No insured persons in the database.")

    def find_by_name(self, name, surname):
        found = [person for person in self.insured_people if person.name.lower() == name.lower() and person.surname.lower() == surname.lower()]
        return found

class UserInterface:
    @staticmethod
    def get_non_empty_input(prompt):
        while True:
            user_input = input(prompt)
            if user_input.strip():  # Ensure the input is not empty
                return user_input
            else:
                print("Input cannot be empty. Please try again.")

    @staticmethod
    def get_age_input(prompt):
        while True:
            try:
                age = int(input(prompt))
                if age > 0:  # Valid age (must be a positive integer)
                    return age
                else:
                    print("Age must be a positive number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number for age.")

    @staticmethod
    def get_phone_input(prompt):
        while True:
            phone = input(prompt)
            if phone.isdigit() and len(phone) == 9:  # Validate phone number (10 digits)
                return phone
            else:
                print("Please enter a valid 9-digit phone number.")

    @staticmethod
    def show_menu():
        print("\nInsurance Client Database")
        print("1. Add Insured Person")
        print("2. Display All Insured People")
        print("3. Search Insured Person by Name and Surname")
        print("4. Exit")

    @staticmethod
    def show_search_results(results):
        if results:
            for person in results:
                print(person)
        else:
            print("No matching insured person found.")

class InsuranceApp:
    def __init__(self):
        self.database = InsuranceDatabase()

    def run(self):
        while True:
            UserInterface.show_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':  # Add insured person
                name = UserInterface.get_non_empty_input("Enter name: ")
                surname = UserInterface.get_non_empty_input("Enter surname: ")
                age = UserInterface.get_age_input("Enter age: ")
                phone = UserInterface.get_phone_input("Enter phone number: ")
                person = InsuredPerson(name, surname, age, phone)
                self.database.add_person(person)
                print("Data byla uložena.")

            elif choice == '2':  # Display all insured people
                self.database.display_all()

            elif choice == '3':  # Search for insured person by name and surname
                name = UserInterface.get_non_empty_input("Enter name to search: ")
                surname = UserInterface.get_non_empty_input("Enter surname to search: ")
                results = self.database.find_by_name(name, surname)
                UserInterface.show_search_results(results)

            elif choice == '4':  # Exit the program
                print("Exiting the program...")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = InsuranceApp()
    app.run()