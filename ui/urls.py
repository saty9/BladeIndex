from django.urls import path, include
from ui import views


urlpatterns = [
    path('', views.new_results),
    path('<slug:table_name>', views.results)
]
