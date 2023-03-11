from django.db import models

class Customer_record(models.Model):
    fullName = models.TextField()
    phoneNumber = models.TextField()
    age = models.IntegerField()

    # bloodPressure = models.TextField()
    # tempreture = models.CharField(max_length=5)
    def __str__(self):
        return self.fullName
    



class Medicine_record(models.Model):
    medName = models.TextField()
    currentStock = models.IntegerField()
    lastLoadedStock = models.IntegerField()
    lastLoadingDate = models.DateTimeField(auto_now_add=True, editable=True)
    price = models.IntegerField()

    def __str__(self):
        return self.medName
    

class Medicine_pres(models.Model):
    # timingsChoice = {
    #     "OPD" : "Once per day",
    #     "TPD" : "Twice per day",
    #     "THPD" : "Thrice per day"
    # }
    customerId = models.ForeignKey(Customer_record, on_delete=models.CASCADE)
    medName = models.ForeignKey(Medicine_record, related_name='prescriptions', on_delete=models.DO_NOTHING)
    dose = models.IntegerField()
    # date = models.DateTimeField(auto_now_add=True, editable=True)
    # timings = models.CharField(max_length=4, choices=timingsChoice)

    def __str__(self):
        return f"{self.medName} - {self.customerId.fullName}"
