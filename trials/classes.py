class Employee:
  """ Employee sinifi hakkinda bilgi
  girisini buradan yapacagiz.
  """

  raise_amt = 1.05
  num_of_emps = 0
  employee = []

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    #self.email = self.first + '.' + self.last + '@email.com'
    self.pay = int(pay)
    self.add_at_list()
    #Employee.num_of_emps += 1
    Employee.num_of_emps = len(self.employee)
    
  def add_at_list(self):
    if self.fullname not in self.employee:
      self.employee.append(self.fullname)
      print("'%s' eklendi." %(self.fullname))        
    else:
      print("'%s' zaten eklendi." %(self.fullname))
     
  @property
  def email(self):
    return '{}.{}@email.com'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amt)
    print('%s\'nın maaşı %s TL oldu.' %(self.fullname, self.pay))

  @classmethod
  def set_raise_amt(cls, value):
    cls.raise_amt = value
    print("Maaş artış oranı : ", "%", "%s oldu." %(value))

  @classmethod
  def from_string(cls, emp_str):
    """Bu fonksiyon ile 'first', 'last' ve 'pay' girilecektir.
Kelime aralarina '-' isareti koyarak bu sekilde giriniz : from_string("ADI-SOYADI-MAASI")
"""
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)

  @property
  def fullname(self):
    return '{} {}'.format(self.first, self.last)
    
  @fullname.setter
  def fullname(self, name):
    first, last = name.split(' ')
    self.first = first
    self.last = last
    
  @fullname.deleter
  def fullname(self):
    print('Ad silindi.')
    self.first = None
    self.last = None

  @staticmethod
  def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
      return False
    return True

  @staticmethod
  def ardisik_sayilar_toplami(n):
    return n * (n+1) / 2

  @staticmethod
  def karekok(n):
    return n**0.5

  @staticmethod
  def karesi(n):
    return  n**2

  @staticmethod
  def kup(n):
    return  n**3

  def __repr__(self):
    return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

  def __str__(self):
    return '{} - {}'.format(self.fullname, self.email)

  def __add__(self, other):
    self.pay = self.pay + int(other)
    return self.pay

  def __len__(self):
    return len(self.fullname)

class Manager(Employee):
  """ Manager sinifi hakkinda bilgi
  girisini buraya yazacagiz.
  """

  raise_amt = 1.20
  num_of_mngrs = 0
  managers = []

  def __init__(self, *args, employees=None):
    super().__init__(*args)
    if employees is None:
      self.employees = []
    else:
      self.employees = employees
      print("'%s' eklendi..." %(employees[0].fullname))
    self.add_mngr_list()
    Manager.num_of_mngrs = len(self.managers)

  def add_mngr_list(self):
    if self.fullname not in self.managers:
      self.managers.append(self.fullname)
      print("'%s' eklendi..." %(self.fullname))        
    else:
      print("'%s' zaten eklendi..." %(self.fullname)) 
    
  def add_emp(self, emp):
    for i in self.managers:
      if i != emp.fullname and emp not in self.employees:
        self.employees.append(emp)
        print("'%s' eklendi..." %(emp.fullname))
      else:
        print("'%s' zaten eklendi..." %(emp.fullname))

  def remove_emp(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)
      print("'%s' silindi..." %(emp.fullname))
    else:
      print("'%s' zaten silindi..." %(emp.fullname))

  def print_emps(self):
    for emp in self.employees:
      print('-->', emp.fullname)

  def __repr__(self):
    return "Manager('{}', '{}', {})".format(self.first, self.last, self.pay)

class Developer(Employee):
  """ Developer sinifi hakkinda bilgi
  girisi buraya yazilacak.
  """

  raise_amt = 1.10

  def __init__(self, *args, prog_lang=None):
    super().__init__(*args)
    self.prog_lang = prog_lang

dev_1 = Developer('Corey', 'Schafer', 50000, prog_lang='Python')
dev_2 = Developer('Test', 'Employee', 60000, prog_lang='Java') # *args kullanildiysa argumen önüne "prog_lang=" eklenir.

mgr_1 = Manager('Sue', 'Smith', 90000, employees=[dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()

emp_1 = Employee('Ali', 'Er', 2000)
emp_2 = Employee('Veli', 'Can', 1000)

Employee.set_raise_amt(1.02)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
print(Manager.is_workday(datetime.date(2020,4,20)))
print(Manager.is_workday(datetime.datetime.now()))
print(Manager.is_workday(datetime.date.today()))

print(Employee.from_string.__doc__)

a1 = "ali cem can"
a2 = "ali#cem#can"
b = ["ali", "cem", "can"]
c = ("ali", "cem", "can", )

print("-".join(a1))
print("-".join(b))
print("-".join(c))

x = a1.split() # x = a.split(' ')
z = a2.split("#")
print(x)
print(z)

import pandas as pd
df = pd.DataFrame({
    'invalid_input' : ["NULL", "12.5", "1"],
    'valid_input' : ["7.8", "12.5", "1"]
})

df.style

df['valid_input'].astype(float)

df['invalid_input'].astype(float)

pd.to_numeric(df['invalid_input'], errors='coerce')