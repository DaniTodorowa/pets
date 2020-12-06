

from django.urls import path

from petsnew.views import list_pets, show_pet_details, like_pet

urlpatterns = [
    path('', list_pets),
    path('details/<int:pk>', show_pet_details),
    path('like/', like_pet),
]
