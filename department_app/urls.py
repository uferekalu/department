from django.urls import path
from .import views

app_name = 'department_app'
urlpatterns = [
    path('', views.department_form, name='department_insert'),
    path('<int:id>/', views.department_form, name='department_update'),
    path('delete/<int:id>/', views.department_delete, name='department_delete'),
    path('list/', views.department_list, name='department_list'),
    path('mech_dept/', views.mech_dept, name='mech_dept'),
    path('elect_dept/', views.elect_dept, name='elect_dept'),
    path('civil_dept/', views.civil_dept, name='civil_dept'),
    path('comp_engr_dept/', views.comp_engr_dept, name='comp_engr_dept'),
    path('sci_lab_dept/', views.sci_lab_dept, name='sci_lab_dept'),
    path('food_dept/', views.food_dept, name='food_dept'),
    path('pharm_dept/', views.pharm_dept, name='pharm_dept'),
    path('agric_dept/', views.agric_dept, name='agric_dept'),    
    path('dispense_dept/', views.dispense_dept, name='dispense_dept'),
    path('comp_sci_dept/', views.comp_sci_dept, name='comp_sci_dept'),    
    path('search/', views.search, name='search'),
]