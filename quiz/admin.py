from django.contrib import admin

#quiz-modellerna för databasen

from quiz.models import Quiz, Question

admin.site.register(Quiz)
admin.site.register(Question)
