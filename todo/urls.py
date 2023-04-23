from django.urls import path
from todo.views import hello_from_todo,inside_todo
urlpatterns = [
    # /todo
    path('',hello_from_todo),
    # /todo/inside
    path('inside',inside_todo),
]