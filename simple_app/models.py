from django.db import models


class Users(models.Model):
    """
    simple user
    """

    name = models.CharField(max_length=30)
    age = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    drink = models.CharField(max_length=9, default='water')


    # def calculous(self, validator):
    #     if validator():    
    #         if self.age < 10:
    #             self.drink = 'milk'
    #         elif self.age > 10 < 20:
    #             self.drink = 'coca-cola'
    #         else:
    #             self.drink = 'vodka'