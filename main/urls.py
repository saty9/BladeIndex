from django.urls import path, include
from main import views


urlpatterns = [
    path('table_list', views.rating_table_list, name="main/table_list"),
    path('table_participants/<str:name>', views.rating_table_participants, name="main/table_participants"),
    path('<int:table_id>/<int:competitor_id>/ratings', views.ratings),
    path('<int:table_id>/new_result', views.update_rating),
    path('competitors', views.competitors, name="main/competitors"),
    path('table_data/<str:name>', views.table_data, name='main/table_data')
]
