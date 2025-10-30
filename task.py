class PersonalInfo:
    def _init_(self, name, age, city, hobbies):
        self.name = name
        self.age = age
        self.city = city
        self.hobbies = hobbies

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print(f"Hobbies: {', '.join(self.hobbies)}")
def main():
    name = input("Enter name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")
    hobbies = input("Enter hobbies (comma separated): ").split(",")

    manager = PersonalInfo(name, age, city, hobbies)
    manager.display()
main()