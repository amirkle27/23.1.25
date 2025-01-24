from abc import ABC, abstractmethod
from typing import override, Counter
from datetime import datetime

class Employee(ABC):
    @abstractmethod
    def __init__(self, employee_id: str, name: str, address: str, age: int, year_of_birth = None):
        self.employee_id = employee_id
        self.name = name
        self. address = address
        self.age = age
        self.year_of_birth = year_of_birth if year_of_birth else datetime.now().year - self.age

    def __str__(self):
        return f"[Employee]:\
         \nid: {self.employee_id}\nname: {self.name}\naddress: {self. address}\nage: {self.age}\
         \nyear_of_birth: {self.year_of_birth}"
    @abstractmethod
    def CalculateSalary(self,ABC):
        pass

    def get_age(self):
        self.year_of_birth = datetime.now().year - self.age
        return f"{self.name}'s year of birth is: {self.year_of_birth}"

class Worker(Employee):
    total_workers = 0

    def __init__(self, employee_id: str, name: str, address: str, age: int, hours_per_day: float, hour_rate: float, year_of_birth = None):
        super().__init__(employee_id, name, address, age, year_of_birth)
        Worker.total_workers += 1
        self.hours_per_day = hours_per_day
        self.hour_rate = hour_rate

    def __str__(self):
        return f"Super: {super().__str__()}\
    \nhours_per_day: {self.hours_per_day}\
    \nhour_rate: {self.hour_rate}"

    @override
    def CalculateSalary(self):
        return f"{Employee.__name__}'s salary is: {self.hours_per_day * self.hour_rate}"

Lily = Worker(342457678, 'Lily','Gruzenberg 6, Tel Aviv', 36, 10, 40)
Avraoom = Worker(391261500, 'Avroom', 'Maze 31 Tel Aviv', 52, 10, 40 )

class Manager(Employee):
    def __init__(self, employee_id: str, name: str, address: str, age: int, number_of_employees: int, employee_rate: float, year_of_birth = None):
        super().__init__(employee_id, name, address, age, year_of_birth)
        self.number_of_employees = number_of_employees
        self.employee_rate = employee_rate


    def __str__(self):
        return (f"Super: {super().__init__()}\nnumber_of_employees: {self.number_of_employees}\""
                f"\nemployee_rate: {self.employee_rate}")

    @override
    def CalculateSalary(self):
        return f"Manager salary is: {self.number_of_employees * self.employee_rate}"


Yossi = Manager('038776233', "Yossi", "Rotschild 101, Aviv", 42, Worker.total_workers, 500)


class Contractor:
    def __init__(self, number_of_projects: int, income_per_project: float):
        self.number_of_projects = number_of_projects
        self.income_per_project = income_per_project

    def __str__(self):
        return f"[Contractor]:\nNumber of projects:\
 {self.number_of_projects}\nincome per project: {self.income_per_project}"


    def income(self):
        return f"Contractor income is {self.number_of_projects * self.income_per_project}"

contractor = Contractor(3, 1300)

print(Lily)
print(Yossi.CalculateSalary())
print(Lily.get_age())
print(Yossi.get_age())
