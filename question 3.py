students = {
    "Tavonga": 78,
    "Tatenda": 85,
    "Tawanda": 92,
    "Tapiwa": 67,
    "Takunda": 74
}

print("Students and their marks:")
for name, mark in students.items():
    print(f"{name}: {mark}")

highest_student = max(students, key=students.get)
print(f"\nThe student with the highest mark is {highest_student} with {students[highest_student]} marks.")

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}\n")

book1 = Book("House of Hunger", "Dambudzo Marechera", 12.50)
book2 = Book("Nervous Conditions", "Tsitsi Dangarembga", 15.75)

print('Book Details:')
book1.display_details()
book2.display_details()
