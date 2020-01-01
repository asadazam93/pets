from django.contrib import admin

from animals.models import Dog, Cat


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday')
    search_fields = ('name', )

    def get_queryset(self, request):
        return request.user.dogs.all()


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday')
    search_fields = ('name',)

    def get_queryset(self, request):
        return request.user.cats.all()