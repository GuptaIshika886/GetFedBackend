from django.contrib import admin
from .models import RegisteredUsers
from .models import Canteen
from .models import Categories
from .models import ViewProfile
from .models import RegisteredCntnOwners

@admin.register(RegisteredUsers)
class RegisteredUsersAdmin(admin.ModelAdmin):
    list_display=['id','username','email','pwd','cpwd']

@admin.register(RegisteredCntnOwners)
class RegisteredCntnOwnersAdmin(admin.ModelAdmin):
    list_display=['id','username','cname','email','pwd','cpwd']

@admin.register(Canteen)
class CanteenAdmin(admin.ModelAdmin):
    list_display=['c_id','c_email','c_name','c_address','c_phoneNo','c_feedback']

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display=['c_id','item_name','item_price']

@admin.register(ViewProfile)
class ViewProfileAdmin(admin.ModelAdmin):
    list_display=['username','email']