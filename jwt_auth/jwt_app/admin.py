from django.contrib import admin
from jwt_app.models import User,Book


admin.site.register(User)
admin.site.register(Book)
