from django.urls import path
from .views import PokemonTotalDataView ,AddToFavoriteView,DigimonListView,DigimonDetailView
urlpatterns=[
    path('total/',PokemonTotalDataView.as_view()),
    path('add-to-favorite/', AddToFavoriteView.as_view()),
    path('list-view/',DigimonListView.as_view()),
    path('edit/<pk>',DigimonDetailView.as_view())

]