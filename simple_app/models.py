from django.db import models


class Users(models.Model):

    def __init__(self, name, age, drink):
        self.name = models.CharField(max_length=30)
        self.age = models.DecimalField(max_digits=2)
        self.drink = None

    def user(self):
        pass

    def validator(self):
        if int in self.name:
            raise ValueError
        if str in self.age:
            raise ValueError
        else:
            return True

    def calculous(self, validator):
        if validator():    
            if self.age < 10:
                self.drink = 'milk'
            elif self.age > 10 < 20:
                self.drink = 'coca-cola'
            else:
                self.drink = 'vodka'

            return self.drink
