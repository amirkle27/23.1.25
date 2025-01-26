from abc import ABC, abstractmethod
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
