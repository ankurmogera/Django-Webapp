from django.urls import path, include
from contacts.views import add, dashboard, edit, delete

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('addRecord/', add, name='add'),
    path('editRecord/<int:id>', edit, name='edit'),
    path('deleteRecord/<int:id>', delete, name='delete')
]