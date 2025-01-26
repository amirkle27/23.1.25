class Contractor:
    def __init__(self, number_of_projects: int, income_per_project: float):
        self.number_of_projects = number_of_projects
        self.income_per_project = income_per_project

    def __str__(self):
        return f"[Contractor]:\nNumber of projects:\
 {self.number_of_projects}\nincome per project: {self.income_per_project}"


    def income(self):
        return f"Contractor income is {self.number_of_projects * self.income_per_project}"
