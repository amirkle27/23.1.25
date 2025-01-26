
from employee import *
from typing import override

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
