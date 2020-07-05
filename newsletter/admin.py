from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]
    form = SignUpForm
