class employee:
    numofemp=0

    sum=0
    def __init__(self,name,family,salary,department):
        self.name=name
        self.family = family
        self.salary = salary
        self.department = department
        employee.numofemp+=1
    def averagesal(self):
        employee.sum+=self.salary
        print("Employee Count:",self.numofemp)


class fulltimeEmp(employee):
    def __init__(self, name, family, salary, department):
        employee.__init__(self, name, family, salary, department)
    def averagesal(self):
        super().averagesal()
        self.averagesalary = employee.sum / employee.numofemp
        print(self.averagesalary)


a=fulltimeEmp("aashish","thota",1000,"cse")
a.averagesal()
b=fulltimeEmp("anu","jasti",2000,"eee")
b.averagesal()
