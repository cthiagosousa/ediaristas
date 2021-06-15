from django.urls import path
from .views import getAllDiarists, createDiarist, updateDiarist, deleteDiarist

urlpatterns = [
    path('create-diarist', createDiarist, name='create-diarist'),
    path('list-diarists', getAllDiarists, name='list-diarists'),
    path('update-diarist/<int:id>', updateDiarist, name='update-diarist'),
    path('delete-diarist/<int:id>', deleteDiarist, name='delete-diarist')
]
