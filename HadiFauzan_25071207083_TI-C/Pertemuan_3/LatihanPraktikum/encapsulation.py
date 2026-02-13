class Person:
  def __init__(self, name, age):
    self.name = name    #public property
    self.__age = age    #double underscore = private property

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())

p1.set_age(26)  #single underscore = protect property
print(p1.get_age()) #if get__age with double underscore = error



class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Bisa diakses tapi direkomendasikan untuk tidak memanggil ini