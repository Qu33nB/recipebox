from django.urls import path
from recipe import views

urlpatterns = [
    path('', views.index)
    # path('admin/', admin.site.urls),
]
