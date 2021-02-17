class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    @classmethod     
    def from_string(cls, string):
        full_name = string.split("-")
        return cls(full_name[0], full_name[1], int(full_name[2]))

        