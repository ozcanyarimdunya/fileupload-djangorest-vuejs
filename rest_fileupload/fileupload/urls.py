from django.urls import path

from .views import (
    PersonListView, PersonCreateView, PersonListCreateView
)

person_list = PersonListView.as_view()
person_create = PersonCreateView.as_view()
person_list_create = PersonListCreateView.as_view()

app_name = "fileupload"
urlpatterns = [
    path('list/', person_list, name="person_list"),
    path('create/', person_create, name="person_create"),
    path('list-create/', person_list_create, name="person_list_create"),
]
