from todo.views import list_create_todo, DetailUpdateDeleteTodo
from django.conf.urls import url

urlpatterns = [
    url(r'^$', list_create_todo, name='list_create_todo'),
    url(r'^(?P<pk>\d+)/$', DetailUpdateDeleteTodo.as_view(),
        name='detail_update_delete_todo')
]

# GET /api/todos/
# POST /api/todos/
# PUT /api/todos/{id}
# DELETE /api/todos/{id}