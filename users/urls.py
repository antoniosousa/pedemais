from django.urls import path

from  .views import(
    user_list,
    user_create,
    user_delete,
    user_update,
)

urlpatterns = [
    path('user_list/', user_list, name='user_list'),
    path('user_create/', user_create, name='user_create'),
    path('user_delete/', user_delete, name='user_delete'),
    path('user_update/', user_update, name='user_update')

]