from django.db import models

# Subject Model
class Subject(models.Model):
    name = models.CharField(max_length=100)  
    description = models.TextField()  

    def __str__(self):
        return self.name

# Faculty Model
class Faculty(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Student Model
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()  # Date of Birth
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    faculties = models.ManyToManyField(Faculty, related_name='students') 
    subjects = models.ManyToManyField(Subject, related_name='students')  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

