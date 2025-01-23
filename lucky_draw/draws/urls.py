from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('result', views.draw_results, name='draw_results'),
    path('generate/<str:date>/', views.generate_draw_results_for_date, name='generate_draw_results'),
    # path('export/', views.export_results_csv, name='export_results_csv'),
]