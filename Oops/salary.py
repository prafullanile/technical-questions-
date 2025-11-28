# Create a class Employee that stores name, position, and base salary.
# → Add a method to calculate the net salary after adding a bonus and deducting tax.



class Employ:

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def calculate_net_salary(self, bonus, tax):
        gross_salary = self.salary + bonus
        tax_amount = gross_salary * (tax / 100)
        net_salary = gross_salary - tax_amount
        return net_salary


em1 = Employ("Prafulla", "Jr. Developer", 50000)
net = em1.calculate_net_salary(bonus=10000, tax=10)
print(f"Net Salary: ₹{net}")

