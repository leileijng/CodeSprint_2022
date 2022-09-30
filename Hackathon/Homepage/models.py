from django.db import models



class Individual(models.Model):
    Email = models.EmailField(max_length=200)
    Phone = models.IntegerField()
    Address = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Resume = models.FileField(max_length=200)

    def __str__(self):
        return self.Email

class Company(models.Model):
    CompanyName = models.CharField(max_length=200)
    UEN = models.CharField(max_length=200)
    Industry = models.CharField(max_length=200)
    Phone = models.IntegerField()
    Address = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Password = models.CharField(max_length=200)
    Documents = models.FileField(max_length=200)

    def __str__(self):
        return self.CompanyName

class VerifiedJobListing(models.Model):
    JobTitle = models.CharField(max_length=200)
    Company = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Salary = models.IntegerField()
    JobDescription = models.TextField(max_length=1000)
    Hash = models.CharField(max_length=200)

    def __str__(self):
        return '{}/{}'.format(self.Company, self.JobTitle)

class JobListing(models.Model):
    JobTitle = models.CharField(max_length=200)
    Company = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Salary = models.IntegerField()
    Source = models.CharField(max_length=200)
    JobDescription = models.TextField(max_length=1000)

    def __str__(self):
        return '{}/{}'.format(self.Company, self.JobTitle)
