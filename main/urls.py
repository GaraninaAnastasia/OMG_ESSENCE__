from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path("reference", views.reference, name="reference"),
    path("register", views.register_request, name="register"),
    path("login_", views.login_request, name="login_"),
    path("logout_", views.logout_request, name="logout_"),
    path("projects", views.projects, name="projects"),
    path("standartproject", views.standartproject, name="standartproject"),
    path("cycle1", views.cycle1, name="cycle1"),
    path("cycle2", views.cycle2, name="cycle2"),
    path("cycle3", views.cycle3, name="cycle3"),
    path("cycle4", views.cycle4, name="cycle4"),
    path("cycle5", views.cycle5, name="cycle5"),
    path("cycle6", views.cycle6, name="cycle6"),
    path("cycle7", views.cycle7, name="cycle7"),
    path("cycle8", views.cycle8, name="cycle8"),
    path("results_1", views.results_1, name="results_1"),
    path("results_2", views.results_2, name="results_2"),
    path("results_3", views.results_3, name="results_3"),
    path("results_4", views.results_4, name="results_4"),
    path("results_5", views.results_5, name="results_5"),
    path("results_6", views.results_6, name="results_6"),
    path("results_7", views.results_7, name="results_7"),
    path("results_8", views.results_8, name="results_8"),
]