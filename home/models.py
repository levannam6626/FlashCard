from django.db import models

# Create your models here.
class Taikhoan(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.username}"

class Hocphan(models.Model):
    taikhoan = models.ForeignKey(Taikhoan,on_delete=models.CASCADE)
    tenhocphan = models.CharField(max_length=20)
    mota = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.tenhocphan}"

class Tudien(models.Model):
    hocphan = models.ForeignKey(Hocphan,on_delete=models.CASCADE)
    thuatngu = models.CharField(max_length=200)
    dinhnghia= models.CharField(max_length=200)
    def __str__(self):
        return f"{self.thuatngu}"