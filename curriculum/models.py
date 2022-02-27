from distutils.command.build_scripts import first_line_re
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
import gc

LEVEL_CHOICES = [('BGN', 'beginner'), ('INT', 'intermediate'), ('ADV', 'advanced')]


class User(AbstractUser):
    pass


class Curriculum(models.Model):
    german_title = models.CharField(max_length=100)
    english_title = models.CharField(max_length=100, blank=True, null=True)
    # focus_vocabulary = models.TextField(max_length=5000, blank=True, null=True)
    # incidental_vocabulary = models.TextField(max_length=5000, blank=True, null=True)
    # concepts_learned = models.TextField(max_length=2000, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Curricula"

    def __str__(self):
        return self.german_title


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    current_level = models.CharField(max_length=100, default='-----', choices=LEVEL_CHOICES)
    starting_level = models.CharField(max_length=100, default='-----', choices=LEVEL_CHOICES)
    curriculum_covered = models.ManyToManyField(to='Curriculum', null=True, blank=True, related_name='completed_students')
    curriculum_partially_covered = models.ManyToManyField(to='Curriculum', null=True, blank=True, related_name='partial_students')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))


class Note(models.Model):
    note = models.TextField(max_length=2000)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='note')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note


class Word(models.Model):
    word = models.CharField(max_length=100)
    associated_curriculum = models.ManyToManyField(to='Curriculum', related_name='associated_vocab')

    def __str__(self):
        return self.word


class Concept(models.Model):
    concept = models.CharField(max_length=100)
    associated_curriculum = models.ManyToManyField(to='Curriculum', related_name='associated_concepts')

    def __str__(self):
        return self.concept


class Game(models.Model):
    game = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=100, default='-----', choices=LEVEL_CHOICES)
    associated_curriculum = models.ManyToManyField(to='Curriculum', related_name='associated_games')

    def __str__(self):
        return self.game

class Objective(models.Model):
    objective = models.TextField(max_length=2000)
    associated_curriculum = models.ManyToManyField(to='Curriculum', related_name='associated_objectives')

    def __str__(self):
        return self.objective