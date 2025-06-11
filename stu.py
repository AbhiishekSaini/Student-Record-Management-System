from abc import ABC, abstractmethod

# Abstract Class (Abstraction)
class Person(ABC):
    def __init__(self, name, age):
        self.name = name              # Public
        self._age = age               # Protected

    @abstractmethod
    def show_details(self):
        pass


# Student class (Inheritance + Encapsulation + Overriding)
class Student(Person):
    def __init__(self, name, age, roll, marks):
        super().__init__(name, age)
        self.__roll = roll            # Private
        self.__marks = marks         

    def show_details(self):           # Polymorphism: overrides abstract method
        print(f"Name: {self.name}, Age: {self._age}, Roll No: {self.__roll}, Marks: {self.__marks}")

    def get_marks(self):              # Encapsulation (getter)
        return self.__marks

    def set_marks(self, marks):       # Encapsulation (setter)
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

    def get_roll(self):               # Accessor for roll (optional)
        return self.__roll

    def __del__(self):                # Destructor
        print(f"Student object for {self.name} deleted")


# Record Manager class
class RecordManager:
    def __init__(self):
        self.records = []

    def add_student(self, name, age, roll, marks):
        student = Student(name, age, roll, marks)
        self.records.append(student)
        print(f"Student {name} (Roll No: {roll}) added successfully!")

    def display_all(self):
        print("\n--- Student Records ---")
        for student in self.records:
            student.show_details()

    def update_marks(self, roll, new_marks):
        for student in self.records:
            if student.get_roll() == roll:
                student.set_marks(new_marks)
                print(f"Marks updated for Roll No: {roll}")
                return
        print("Student not found.")

    def delete_student(self, roll):
        for student in self.records:
            if student.get_roll() == roll:
                self.records.remove(student)
                del student
                print(f"Student with Roll No {roll} deleted.")
                return
        print("Student not found.")

# 50 Sample Students
sample_students = [
    ("Abhishek", 20, 101, 87), ("Pankaj", 21, 102, 91), ("Sujal", 22, 103, 76), ("Tarun", 20, 104, 88),
    ("Ravi", 23, 105, 95), ("Neha", 21, 106, 84), ("Priya", 22, 107, 78), ("Ritu", 20, 108, 90),
    ("Karan", 24, 109, 73), ("Anjali", 21, 110, 85), ("Vivek", 20, 111, 92), ("Simran", 22, 112, 89),
    ("Rohit", 23, 113, 65), ("Manish", 22, 114, 75), ("Tina", 21, 115, 94), ("Nikhil", 20, 116, 68),
    ("Preeti", 23, 117, 80), ("Raj", 21, 118, 72), ("Ramesh", 24, 119, 81), ("Suresh", 20, 120, 88),
    ("Aman", 22, 121, 77), ("Deepak", 23, 122, 90), ("Meena", 21, 123, 83), ("Sunil", 22, 124, 79),
    ("Gaurav", 20, 125, 86), ("Harsh", 24, 126, 82), ("Divya", 22, 127, 67), ("Sheetal", 21, 128, 93),
    ("Aarti", 23, 129, 74), ("Vipin", 20, 130, 69), ("Ankita", 22, 131, 95), ("Sonia", 21, 132, 70),
    ("Hemant", 23, 133, 64), ("Arun", 24, 134, 85), ("Mona", 20, 135, 87), ("Bhavna", 22, 136, 91),
    ("Rajan", 21, 137, 89), ("Yash", 23, 138, 82), ("Komal", 20, 139, 90), ("Lalit", 24, 140, 86),
    ("Sneha", 21, 141, 84), ("Ajay", 22, 142, 75), ("Varun", 23, 143, 88), ("Naina", 20, 144, 73),
    ("Chetan", 24, 145, 77), ("Bhavesh", 21, 146, 79), ("Kavita", 23, 147, 94), ("Parul", 22, 148, 68),
    ("Shivani", 20, 149, 92), ("Dev", 24, 150, 81)
]

# Main Execution
if __name__ == "__main__":
    manager = RecordManager()

    # Load sample students
    for name, age, roll, marks in sample_students:
        manager.add_student(name, age, roll, marks)

    # Display All Students
    manager.display_all()
