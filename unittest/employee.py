class Employee():

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

    def email(self):
        return '{}_{}@gmail.com'.format(self.fname,self.lname)

    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

    