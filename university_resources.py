from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Style, init

init(autoreset=True)  # Enable color resets

class Resource:
    _id_counter = 1

    def __init__(self, name, r_type):
        self.id = Resource._id_counter
        Resource._id_counter += 1
        self.name = name
        self.type = r_type
        self.booked = False
        self.last_action_time = None

    def book(self):
        if self.booked:
            return f"{Fore.RED}{self.name} is already booked.{Style.RESET_ALL}"
        self.booked = True
        self.last_action_time = datetime.now()
        return f"{Fore.GREEN}{self.name} successfully booked at {self.last_action_time.strftime('%Y-%m-%d %H:%M:%S')}.{Style.RESET_ALL}"

    def release(self):
        if not self.booked:
            return f"{Fore.YELLOW}{self.name} is not booked.{Style.RESET_ALL}"
        self.booked = False
        self.last_action_time = datetime.now()
        return f"{Fore.GREEN}{self.name} booking released at {self.last_action_time.strftime('%Y-%m-%d %H:%M:%S')}.{Style.RESET_ALL}"

class University:
    def __init__(self):
        self.resources = []
        self.populate_resources()

    def populate_resources(self):
        # Lecture Halls
        for i in range(1, 51):
            self.resources.append(Resource(f"Lecture Hall {i}", "Lecture Hall"))

        # Labs
        labs = ["Biochem Lab", "Physics Lab", "Chemistry Lab", "Computer Lab", "Robotics Lab"]
        for lab in labs:
            self.resources.append(Resource(lab, "Lab"))

        # Sports Facilities
        sports = ["Basketball Court", "Football Ground", "Tennis Court", "Badminton Court"]
        for sport in sports:
            self.resources.append(Resource(sport, "Sports"))

        # Auditoriums
        for i in range(1, 4):
            self.resources.append(Resource(f"Auditorium {i}", "Auditorium"))

    def display_resources(self):
        table = PrettyTable(["ID", "Name", "Type", "Status", "Last Action"])
        for res in self.resources:
            status = f"{Fore.RED}Booked{Style.RESET_ALL}" if res.booked else f"{Fore.GREEN}Available{Style.RESET_ALL}"
            last_action = res.last_action_time.strftime('%Y-%m-%d %H:%M:%S') if res.last_action_time else "N/A"
            table.add_row([res.id, res.name, res.type, status, last_action])
        print(table)

    def search_by_type(self, r_type):
        filtered = [res for res in self.resources if res.type.lower() == r_type.lower()]
        if not filtered:
            print(f"No resources found for type '{r_type}'.")
            return
        table = PrettyTable(["ID", "Name", "Type", "Status"])
        for res in filtered:
            status = f"{Fore.RED}Booked{Style.RESET_ALL}" if res.booked else f"{Fore.GREEN}Available{Style.RESET_ALL}"
            table.add_row([res.id, res.name, res.type, status])
        print(table)

    def book_resource(self, res_id):
        for res in self.resources:
            if res.id == res_id:
                print(res.book())
                return
        print(f"Resource with ID {res_id} not found.")

    def release_resource(self, res_id):
        for res in self.resources:
            if res.id == res_id:
                print(res.release())
                return
        print(f"Resource with ID {res_id} not found.")

def main():
    uni = University()
    while True:
        print("\n--- University Resource Management ---")
        print("1. View all resources")
        print("2. Search resources by type")
        print("3. Book a resource by ID")
        print("4. Release a resource by ID")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            uni.display_resources()
        elif choice == "2":
            r_type = input("Enter resource type: ")
            uni.search_by_type(r_type)
        elif choice == "3":
            try:
                res_id = int(input("Enter resource ID to book: "))
                uni.book_resource(res_id)
            except ValueError:
                print("Invalid input. Enter a number.")
        elif choice == "4":
            try:
                res_id = int(input("Enter resource ID to release: "))
                uni.release_resource(res_id)
            except ValueError:
                print("Invalid input. Enter a number.")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
