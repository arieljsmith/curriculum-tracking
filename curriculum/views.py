from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Curriculum, Student, Note, Word, Concept, Game, Objective
from .forms import CurriculumForm, StudentForm, NoteForm, WordForm, ConceptForm, GameForm, ObjectiveForm


# ================================
# I N D E X / H O M E
# ================================

# def index(request):
#     context = {'curricula': Curriculum.objects.all(), 'students': Student.objects.all()}
#     return render(request, 'home.html', context=context)


# ====================================
# I N D E X / H O M E
# (FOR ON-PAGE AJAX FORMS; ONLY THIS
# OR THE ABOVE SHOULD BE ACTIVE,
# NOT BOTH)
# ====================================

def index(request):
    context = {'curricula': Curriculum.objects.all(), 'students': Student.objects.all(), 'curriculum_form': CurriculumForm(), 'student_form': StudentForm()}
    return render(request, 'home.html', context=context)

# ================================
# D E T A I L  P A G E S
# ================================


# def curriculum_detail(request, pk):
#     curriculum = get_object_or_404(Curriculum, pk=pk)
#     return render(request, 'curriculum_detail.html', {'curriculum': curriculum})


# def student_detail(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     curricula = Curriculum.objects.all()
#     student_curriculum_covered = []
#     student_curriculum_partially_covered = []
#     for curriculum in student.curriculum_covered.all():
#         student_curriculum_covered.append(curriculum.german_title)
#     for curriculum in student.curriculum_partially_covered.all():
#         student_curriculum_partially_covered.append(curriculum.german_title)

#     in_student_curriculum_covered = set(student_curriculum_covered)
#     in_student_curriculum_partially_covered = set(student_curriculum_partially_covered)
#     in_student_curriculum_partially_covered_but_not_in_in_student_curriculum_covered = in_student_curriculum_partially_covered - in_student_curriculum_covered

#     combined_covered_and_partially_covered = student_curriculum_covered + list(in_student_curriculum_partially_covered_but_not_in_in_student_curriculum_covered)

#     curriculum_not_covered = curricula.exclude(german_title__in=combined_covered_and_partially_covered)
#     return render(request, 'student_detail.html', {'student': student, 'curricula': curricula, 'curriculum_not_covered': curriculum_not_covered})


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note_detail.html', {'note': note})


def word_detail(request, pk):
    word = get_object_or_404(Word, pk=pk)
    return render(request, 'word_detail.html', {'word': word})


def concept_detail(request, pk):
    concept = get_object_or_404(Concept, pk=pk)
    return render(request, 'concept_detail.html', {'concept': concept})


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'game_detail.html', {'game': game})


def objective_detail(request, pk):
    objective = get_object_or_404(Objective, pk=pk)
    return render(request, 'objective_detail.html', {'objective': objective})


# ====================================
# D E T A I L  P A G E S
# (FOR ON-PAGE AJAX FORMS; ONLY THIS
# OR THE ABOVE SHOULD BE ACTIVE,
# NOT BOTH)
# ====================================

def curriculum_detail(request, pk):
    context = {'curriculum': get_object_or_404(Curriculum, pk=pk), 'word_form': WordForm(), 'concept_form': ConceptForm(), 'game_form': GameForm(), 'objective_form': ObjectiveForm()}
    return render(request, 'curriculum_detail.html', context=context)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    curricula = Curriculum.objects.all()
    student_curriculum_covered = []

    for curriculum in student.curriculum_covered.all():
        student_curriculum_covered.append(curriculum.german_title)
    for curriculum in student.curriculum_partially_covered.all():
        student_curriculum_covered.append(curriculum.german_title)

    deduped_student_curriculum_covered = set(student_curriculum_covered)

    curriculum_not_covered = curricula.exclude(german_title__in=deduped_student_curriculum_covered)
    return render(request, 'student_detail.html', {'student': student, 'curricula': curricula, 'curriculum_not_covered': curriculum_not_covered, 'note_form': NoteForm()})

# ================================
# E D I T  P A G E S
# ================================

def curriculum_edit(request, pk):
    curriculum = get_object_or_404(Curriculum, pk=pk)
    if request.method == "POST":
        form = CurriculumForm(request.POST, request.FILES, instance=curriculum)
        if form.is_valid():
            curriculum = form.save()
            curriculum.save()
        return redirect('curriculum_detail', pk=curriculum.pk)
    else:
        form = CurriculumForm(instance=curriculum)
    return render(request, 'curriculum_edit.html', {'form': form})


def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save()
            student.save()
        return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_edit.html', {'form': form})


def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            note = form.save()
            note.save()
        return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_edit.html', {'form': form})


def word_edit(request, pk):
    word = get_object_or_404(Word, pk=pk)
    if request.method == "POST":
        form = WordForm(request.POST, request.FILES, instance=word)
        if form.is_valid():
            word = form.save()
            word.save()
        return redirect('word_detail', pk=word.pk)
    else:
        form = WordForm(instance=word)
    return render(request, 'word_edit.html', {'form': form})


def concept_edit(request, pk):
    concept = get_object_or_404(Concept, pk=pk)
    if request.method == "POST":
        form = ConceptForm(request.POST, request.FILES, instance=concept)
        if form.is_valid():
            concept = form.save()
            concept.save()
        return redirect('concept_detail', pk=concept.pk)
    else:
        form = ConceptForm(instance=concept)
    return render(request, 'concept_edit.html', {'form': form})


def game_edit(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            game = form.save()
            game.save()
        return redirect('game_detail', pk=game.pk)
    else:
        form = GameForm(instance=game)
    return render(request, 'game_edit.html', {'form': form})


def objective_edit(request, pk):
    objective = get_object_or_404(Objective, pk=pk)
    if request.method == "POST":
        form = ObjectiveForm(request.POST, request.FILES, instance=objective)
        if form.is_valid():
            objective = form.save()
            objective.save()
        return redirect('objective_detail', pk=objective.pk)
    else:
        form = ObjectiveForm(instance=objective)
    return render(request, 'objective_edit.html', {'form': form})


# ================================
# D E L E T E  P A G E S
# ================================

def curriculum_delete(request, pk):
    curriculum = get_object_or_404(Curriculum, pk=pk)

    if request.method == "POST":
        curriculum.delete()
        return HttpResponseRedirect("/")
    return render(request, "curriculum_delete.html")


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        return HttpResponseRedirect("/")
    return render(request, "student_delete.html")


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        return HttpResponseRedirect("/")
    return render(request, "note_delete.html")


def word_delete(request, pk):
    word = get_object_or_404(Word, pk=pk)

    if request.method == "POST":
        word.delete()
        return HttpResponseRedirect("/")
    return render(request, "word_delete.html")


def concept_delete(request, pk):
    concept = get_object_or_404(Concept, pk=pk)

    if request.method == "POST":
        concept.delete()
        return HttpResponseRedirect("/")
    return render(request, "concept_delete.html")


def game_delete(request, pk):
    game = get_object_or_404(Game, pk=pk)

    if request.method == "POST":
        game.delete()
        return HttpResponseRedirect("/")
    return render(request, "game_delete.html")


def objective_delete(request, pk):
    objective = get_object_or_404(Objective, pk=pk)

    if request.method == "POST":
        objective.delete()
        return HttpResponseRedirect("/")
    return render(request, "objective_delete.html")


# ================================
# C R E A T I O N  P A G E S
# ================================

def curriculum_new(request):
    if request.method == "POST":
        form = CurriculumForm(request.POST, request.FILES)
        if form.is_valid():
            curriculum = form.save()
            curriculum.save()
        return redirect('curriculum_detail', pk=curriculum.pk)
    else:
        form = CurriculumForm()
    return render(request, 'curriculum_new.html', {'form': form})


def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            student.save()
        return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'student_new.html', {'form': form})


def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save()
            note.save()
        return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'note_new.html', {'form': form})


def word_new(request):
    if request.method == "POST":
        form = WordForm(request.POST, request.FILES)
        if form.is_valid():
            word = form.save()
            word.save()
        return redirect('word_detail', pk=word.pk)
    else:
        form = WordForm()
    return render(request, 'word_new.html', {'form': form})


def concept_new(request):
    if request.method == "POST":
        form = ConceptForm(request.POST, request.FILES)
        if form.is_valid():
            concept = form.save()
            concept.save()
        return redirect('concept_detail', pk=concept.pk)
    else:
        form = ConceptForm()
    return render(request, 'concept_new.html', {'form': form})


def game_new(request):
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save()
            game.save()
        return redirect('game_detail', pk=game.pk)
    else:
        form = GameForm()
    return render(request, 'game_new.html', {'form': form})


def objective_new(request):
    if request.method == "POST":
        form = ObjectiveForm(request.POST, request.FILES)
        if form.is_valid():
            objective = form.save()
            objective.save()
        return redirect('objective_detail', pk=objective.pk)
    else:
        form = ObjectiveForm()
    return render(request, 'objective_new.html', {'form': form})


# ======================================================================
# ======================================================================
#      _       _   _    __  __ __     _____ _______        ______
#     / \     | | / \   \ \/ / \ \   / /_ _| ____\ \      / / ___|
#    / _ \ _  | |/ _ \   \  /   \ \ / / | ||  _|  \ \ /\ / /\___ \
#   / ___ \ |_| / ___ \  /  \    \ V /  | || |___  \ V  V /  ___) |
#  /_/   \_\___/_/   \_\/_/\_\    \_/  |___|_____|  \_/\_/  |____/
#
# ======================================================================
# ======================================================================


# ====================================
# A J A X  C R E A T I O N  P A G E S
# ====================================

def ajax_curriculum_new(request):
    data = {}
    if request.method == 'POST':
        print(request.POST)
        curriculum_german_title = request.POST.get('german_title')
        curriculum_english_title = request.POST.get('english_title')
        form = CurriculumForm(request.POST)

        if form.is_valid():
            new_curriculum = form.save()
            data['saved'] = True
        data['curriculum_german_title'] = curriculum_german_title
        data['curriculum_english_title'] = curriculum_english_title

    else:
        data = {'response': 'nothing to get'}
    return JsonResponse(data)


def ajax_student_new(request):
    data = {}
    if request.method == 'POST':
        print(request.POST)
        student_first_name = request.POST.get('first_name')
        student_last_name = request.POST.get('last_name')
        student_birthdate = request.POST.get('birthdate')
        student_current_level = request.POST.get('current_level')
        student_starting_level = request.POST.get('starting_level')
        student_curriculum_covered = request.POST.get('curriculum_covered')
        student_curriculum_partially_covered = request.POST.get('curriculum_partially_covered')
        form = StudentForm(request.POST)

        if form.is_valid():
            new_student = form.save()
            data['saved'] = True
        data['student_first_name'] = student_first_name
        data['student_last_name'] = student_last_name
        data['student_birthdate'] = student_birthdate
        data['student_current_level'] = student_current_level
        data['student_starting_level'] = student_starting_level
        data['student_curriculum_covered'] = student_curriculum_covered
        data['student_curriculum_partially_covered'] = student_curriculum_partially_covered

    else:
        data = {'response': 'nothing to get'}
    return JsonResponse(data)


def ajax_word_new(request):
    data = {}
    if request.method == 'POST':
        print(request.POST)
        word_word = request.POST.get('word')
        word_associated_curriculum = request.POST.get('associated_curriculum')
        form = WordForm(request.POST)

        if form.is_valid():
            new_word = form.save()
            data['saved'] = True
        data['word_word'] = word_word
        data['word_associated_curriculum'] = word_associated_curriculum

    else:
        data = {'response': 'nothing to get'}
    return JsonResponse(data)


def ajax_concept_new(request):
    data = {}
    if request.method == 'POST':
        print(request.POST)
        concept_concept = request.POST.get('concept')
        concept_associated_curriculum = request.POST.get('associated_curriculum')
        form = ConceptForm(request.POST)

        if form.is_valid():
            new_concept = form.save()
            data['saved'] = True
        data['concept_concept'] = concept_concept
        data['concept_associated_curriculum'] = concept_associated_curriculum

    else:
        data = {'response': 'nothing to get'}
    return JsonResponse(data)


def ajax_game_new(request):
    data = {}
    if request.method == 'POST':
        print(request.POST)
        game_game = request.POST.get('game')
        game_difficulty_level = request.POST.get('difficulty_level')
        game_associated_curriculum = request.POST.get('associated_curriculum')
        form = GameForm(request.POST)

        if form.is_valid():
            new_game = form.save()
            data['saved'] = True
        data['game_game'] = game_game
        data['game_difficulty_level'] = game_difficulty_level
        data['game_associated_curriculum'] = game_associated_curriculum

    else:
        data = {'response': 'nothing to get'}
    return JsonResponse(data)


def ajax_objective_new(request):
    data = {}
    if request.method == 'POST':
        print(request.POST)
        objective_objective = request.POST.get('objective')
        objective_associated_curriculum = request.POST.get('associated_curriculum')
        form = ObjectiveForm(request.POST)

        if form.is_valid():
            new_objective = form.save()
            data['saved'] = True
        data['objective_objective'] = objective_objective
        data['objective_associated_curriculum'] = objective_associated_curriculum

    else:
        data = {'response': 'nothing to get'}
    return JsonResponse(data)


def ajax_note_new(request):
    data = {}
    if request.method == 'POST':
        print(request.POST)
        note_note = request.POST.get('note')
        note_student = request.POST.get('student')
        form = NoteForm(request.POST)

        if form.is_valid():
            new_note = form.save()
            data['saved'] = True
        data['note_note'] = note_note
        data['note_student'] = note_student

    else:
        data = {'response': 'nothing to get'}
    return JsonResponse(data)