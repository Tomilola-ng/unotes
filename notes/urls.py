from django.urls import path
from .views import *

urlpatterns = [
    path('create/', NoteCreate.as_view() ,name = 'createView'),
    path('view/<str:pk>', NoteDetail.as_view() ,name = 'detailView'),
    path('update/<str:pk>/', NoteUpdate.as_view() ,name = 'updateView'),
    path('delete/<str:pk>/', NoteDelete.as_view() ,name = 'deleteView'),
]