from django.urls import path

from project_first_app import views

urlpatterns = [
    path('auto_owner/<int:poll_id>/', views.auto_owner_info, name='auto_owner_info'),
]
