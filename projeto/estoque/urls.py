from django.urls import path
from . import views

app_name = "estoque"
urlpatterns = [
    path("", views.index, name="index"),
    path("pagina/criar", views.criar_pagina, name="criar_pagina"),
    path("lista/", views.lista, name="lista"),
    path("detalhes/<uuid:id>/", views.detalhes, name="detalhes"),
    path("detalhes/<uuid:id>/editar/", views.editar, name="editar"),
    path("detalhes/<uuid:id>/apagar/", views.apagar, name="apagar"),
]