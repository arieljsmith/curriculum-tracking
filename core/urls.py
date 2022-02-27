"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from curriculum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('curriculum/<int:pk>/', views.curriculum_detail, name='curriculum_detail'),
    path('curriculum/<int:pk>/edit/', views.curriculum_edit, name='curriculum_edit'),
    path('curriculum/<int:pk>/delete/', views.curriculum_delete, name='curriculum_delete'),
    path('curriculum/new/', views.curriculum_new, name='curriculum_new'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('student/new/', views.student_new, name='student_new'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
    path('note/new/', views.note_new, name='note_new'),
    path('word/<int:pk>/', views.word_detail, name='word_detail'),
    path('word/<int:pk>/edit/', views.word_edit, name='word_edit'),
    path('word/<int:pk>/delete/', views.word_delete, name='word_delete'),
    path('word/new/', views.word_new, name='word_new'),
    path('concept/<int:pk>/', views.concept_detail, name='concept_detail'),
    path('concept/<int:pk>/edit/', views.concept_edit, name='concept_edit'),
    path('concept/<int:pk>/delete/', views.concept_delete, name='concept_delete'),
    path('concept/new/', views.concept_new, name='concept_new'),
    path('game/<int:pk>/', views.game_detail, name='game_detail'),
    path('game/<int:pk>/edit/', views.game_edit, name='game_edit'),
    path('game/<int:pk>/delete/', views.game_delete, name='game_delete'),
    path('game/new/', views.game_new, name='game_new'),
    path('objective/<int:pk>/', views.objective_detail, name='objective_detail'),
    path('objective/<int:pk>/edit/', views.objective_edit, name='objective_edit'),
    path('objective/<int:pk>/delete/', views.objective_delete, name='objective_delete'),
    path('objective/new/', views.objective_new, name='objective_new'),
    path('api/curriculum/new', views.ajax_curriculum_new, name='ajax_curriculum_new'),
    path('api/student/new', views.ajax_student_new, name='ajax_student_new'),
    path('api/word/new', views.ajax_word_new, name='ajax_word_new'),
    path('api/concept/new', views.ajax_concept_new, name='ajax_concept_new'),
    path('api/game/new', views.ajax_game_new, name='ajax_game_new'),
    path('api/objective/new', views.ajax_objective_new, name='ajax_objective_new'),
]
