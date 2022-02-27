from django import forms
from .models import Curriculum, Student, Note, Word, Concept, Game, Objective


class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = ['german_title', 'english_title']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'birthdate', 'current_level', 'starting_level', 'curriculum_covered', 'curriculum_partially_covered']


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note', 'student']


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'associated_curriculum']


class ConceptForm(forms.ModelForm):
    class Meta:
        model = Concept
        fields = ['concept', 'associated_curriculum']


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['game', 'difficulty_level', 'associated_curriculum']


class ObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = ['objective', 'associated_curriculum']
