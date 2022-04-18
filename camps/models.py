from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    birth_date = models.DateField(blank=True, null=True)
    MANAGER = 'MG'
    GUARDIAN = 'GD'
    POSITION_CHOICES = [
        (MANAGER, 'Kierownik'),
        (GUARDIAN, 'Wychowawca'),
    ]
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)


class Parent(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()


class Group(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)


class Activity(models.Model):
    groups = models.ManyToManyField(Group)
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_program = models.BooleanField()


class Participant(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    room = models.CharField(max_length=20, blank=True)
    email_address = models.EmailField(blank=True)
    parents = models.ManyToManyField(Parent)
    groups = models.ManyToManyField(Group)


class ProgramActivity(models.Model):
    name = models.CharField(max_length=200)
