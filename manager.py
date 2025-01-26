from employee import *
from typing import override

class Manager(Employee):
    def __init__(self, employee_id: str, name: str, address: str, age: int, number_of_employees: int, employee_rate: float, year_of_birth = None):
        super().__init__(employee_id, name, address, age, year_of_birth)
        self.number_of_employees = number_of_employees
        self.employee_rate = employee_rate


    def __str__(self):
        return (f"Super: {super().__str__()}\nnumber_of_employees: {self.number_of_employees}\
                \nemployee_rate: {self.employee_rate}")

    @override
    def CalculateSalary(self):
        return f"Manager salary is: {self.number_of_employees * self.employee_rate}"

from worker import Worker
Yossi = Manager('038776233', "Yossi", "Rotschild 101, Aviv", 42, Worker.total_workers, 500)
