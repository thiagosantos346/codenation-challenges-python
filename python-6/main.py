from abc import ABCMeta
from abc import abstractmethod


class Department(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, name, code):
        self.set_department(name)
        self.set_department_code(code)

    @abstractmethod
    def get_department_code(self):
        return self.__code

    @abstractmethod
    def set_department_code(self, code):
        self.__code = code

    @abstractmethod
    def get_department(self):
        return self.__name

    @abstractmethod
    def set_department(self, name):
        self.__name = name


class Employee(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, code, name, salary):
        self.set_code(code)
        self.set_name(name)
        self.set_salary(salary)
        self.set_hours(8)

    @abstractmethod
    def get_code(self):
        return self.__code

    @abstractmethod
    def set_code(self, code):
        self.__code = code

    @abstractmethod
    def get_name(self):
        return self.__name

    @abstractmethod
    def set_name(self, name):
        self.__name = name

    @abstractmethod
    def get_salary(self):
        return self.__salary

    @abstractmethod
    def set_salary(self, salary):
        self.__salary = salary

    @abstractmethod
    def calc_bonus(self):
        pass

    @abstractmethod
    def set_hours(self, hours):
        self.__hours = hours

    @abstractmethod
    def get_hours(self):
        return self.__hours


class Manager(Employee, Department):
    def __init__(self, code, name, salary):
        Employee.__init__(self, code, name, salary)
        Department.__init__(self, 'managers', 1)

    def calc_bonus(self):
        return Employee.get_salary(self) * 0.15

    # Employee
    # Saída
    def get_code(self):
        return Employee.get_code(self)

    def get_hours(self):
        return Employee.get_hours(self)

    def get_name(self):
        return Employee.get_name(self)

    def get_salary(self):
        return Employee.get_salary(self)

    # Entrada
    def set_code(self, code):
        return Employee.set_code(self, code)

    def set_hours(self, hours):
        return Employee.set_hours(self, hours)

    def set_name(self, name):
        return Employee.set_name(self, name)

    def set_salary(self, salary):
        return Employee.set_salary(self, salary)

    # Department
    # Saída
    def get_department(self):
        return Department.get_department(self)

    def get_department_code(self):
        return Department.get_department_code(self)

    # Entrada
    def set_department(self, name):
        return Department.set_department(self, name)

    def set_department_code(self, code):
        return Department.set_department_code(self, code)


class Seller(Employee, Department):

    def __init__(self, code, name, salary):
        Employee.__init__(self, code, name, salary)
        Department.__init__(self, 'sellers', 2)
        self.__sales = 0

    # Seller
    # Saída
    def get_sales(self):
        return self.__sales

    def calc_bonus(self):
        return self.get_sales() * 0.15

    def put_sales(self, sales):
        self.__sales += sales

    # Employee
    # Saída
    def get_code(self):
        return Employee.get_code(self)

    def get_hours(self):
        return Employee.get_hours(self)

    def get_name(self):
        return Employee.get_name(self)

    def get_salary(self):
        return Employee.get_salary(self)

    # Entrada
    def set_code(self, code):
        return Employee.set_code(self, code)

    def set_hours(self, hours):
        return Employee.set_hours(self, hours)

    def set_name(self, name):
        return Employee.set_name(self, name)

    def set_salary(self, salary):
        return Employee.set_salary(self, salary)

    # Department
    # Saída
    def get_department(self):
        return Department.get_department(self)

    def get_department_code(self):
        return Department.get_department_code(self)

    # Entrada
    def set_department(self, name):
        return Department.set_department(self, name)

    def set_department_code(self, code):
        return Department.set_department_code(self, code)
