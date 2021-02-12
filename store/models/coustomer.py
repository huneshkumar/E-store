from django.db import models



class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=500)


    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_Email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False



    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False
