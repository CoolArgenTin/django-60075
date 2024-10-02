from django.urls import path
from inicio.views import mi_view, inicio, dataxd, primer_template
urlpatterns = [
    path("mi-view/", mi_view),
    path("", inicio),
    path("data-xd", dataxd),
    path("primer-template", primer_template)
]