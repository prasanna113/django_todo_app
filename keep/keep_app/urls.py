from django.conf.urls import url
from keep_app import views

urlpatterns = [
    url(r'^api/todo$', views.todo_list, name="todo-create-update"),
    url(r'^api/todo/(?P<pk>[0-9]+)$', views.todo_list_details),
    url(r'^api/todo/completed', views.todo_completed)
]
