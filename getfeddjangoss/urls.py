from django.contrib import admin
from django.urls import path
from application import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('userDetails/',views.usersDetail),
    path('canteenDetail/',views.canteenDetail),
    path('categoriesDetail/',views.categoriesDetail),
    path('viewProfile/',views.viewProfileDetail),
    path('cntnOwnerDetail/',views.cntnOwnersDetail),
    path('route/',views.post),
    # path('restaurants/',views.restaurantsDetails)
]