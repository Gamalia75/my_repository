# 3.	Напишіть користувацький клас виключення з функціоналом на свій вибір.
# Викличте його за допомогою інструкції raise.



class SalaryNotInRangeError(Exception):
    def __init__(self, salary, message="Salary is not in (10000, 20000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.salary} -> {self.message}'


salary = int(input("Enter salary amount: "))
if not 10000 < salary < 20000:
    raise SalaryNotInRangeError(salary)
