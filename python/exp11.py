# 11.Create a class Manager which will inherit the Employee class with data
# members:Post,No_of_Employee. Create suitable methods for reading and
# printing Manager information(Single Inheritance,use Super method)
class Employee:
    def __init__(self, post, no_of_emp):
        self.post = post
        self.no_of_emp = no_of_emp
        self.no_of_emp = no_of_emp

    def display(self):
        print("Post: ", self.post)
        print("No of Employee: ", self.no_of_emp)


class Manager(Employee):
    def __init__(self, post, no_of_emp):
        super().__init__(post, no_of_emp)

    def display(self):
        super().display()


def main():
    manager = Manager("Manager", 10)
    manager.display()
