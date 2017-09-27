#Rätt URL:s med rätt vyer. Alltså visa rätt sida när URL har ett visst värde.

from django.urls import path
from quiz import views

urlpatterns = [
	path("",views.startpage),
	path("quiz/<int:quiz_number>/"),views.quiz,
	path("quiz/<int:quiz_number>/question/<int:question_number>/", views.question),
	path("quiz/<int:quiz_number>/completed/"), views.completed,
	
]

