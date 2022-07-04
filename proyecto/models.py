# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CursoUser(models.Model):
    nota1 = models.FloatField(blank=True, null=True)
    nota2 = models.FloatField(blank=True, null=True)
    nota3 = models.FloatField(blank=True, null=True)
    promedio = models.FloatField(blank=True, null=True)
    curso = models.ForeignKey('Cursos', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

    class Meta:
        managed = False
        db_table = 'curso_user'


class Cursos(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cursos'


class Roles(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'roles'

    


class UserRoles(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey(Roles, models.DO_NOTHING)

    def __str__(self):
        return str(self.user)
    class Meta:
        managed = False
        db_table = 'user_roles'
        unique_together = (('user', 'role'),)


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    birthday = models.CharField(max_length=55, blank=True, null=True)
    email = models.CharField(unique=True, max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=55, blank=True, null=True)
    last_name = models.CharField(max_length=55, blank=True, null=True)
    password = models.CharField(max_length=120, blank=True, null=True)
    username = models.CharField(unique=True, max_length=20, blank=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        managed = False
        db_table = 'users'
