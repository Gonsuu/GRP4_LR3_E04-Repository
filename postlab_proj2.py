class Student:
    def __init__(self, name, grade, age, student_id):
        self.name = name
        self.grade = grade
        self.age = age
        self.student_id = student_id

    def __str__(self):
        return f"Name: {self.name}, Grade: {self.grade}, Age: {self.age}, ID: {self.student_id}"

    def __lt__(self, other):
        return self.name < other.name


def main():
    students = []

    # Read student data from the text file
    with open("students.txt", "r") as file:
        for line in file:
            name, grade, age, student_id = line.strip().split(", ")
            students.append(Student(name, int(grade), int(age), student_id))
    
    # Sort the students by name
    students.sort()

    # Display the sorted list of students
    print("Sorted list of students:")
    for student in students:
        print(student)


# Run the main function
main()
