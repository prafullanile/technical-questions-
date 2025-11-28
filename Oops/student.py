# Create a class Student that:
# Stores name, roll number, and marks of 3 subjects with subject name
# Has methods to calculate:
# Total marks
# Average marks
# Display details


class student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.subject = subject

    def total_marks(self):
        return sum(self.subject.values())

    def average_marks(self):
        return sum(self.subject.values()) / len(self.subject)

    def show(self):
        print(f"name of student is {self.name}")
        print(f"roll_no of student is {self.rollno}")

        print("marks")
        for subject,mark in self.subject.items():
            print(f"{subject} is {mark}")

        print(f"total marks in subject is {self.total_marks()}")


        print(f"average marks of 3 subject are {self.average_marks()}")

subject={
    'python':88,
    'sql':78,
    'Ml':81
}

s = student("prafull", 38, [88, 78, 81])

s.show()


class student:
	def __init__(self, name, marks):
		self.name = name
		self.marks = marks

	def __add__(self, other):
		return self.marks + other.marks


s1 = student("chetan", 70)
s2 = student("prafull",80)

total_marks = s1 + s2

print("total marks is s1 and s2 is !", total_marks)