from django.contrib import admin

from cats.models import Achievement, AchievementCat, Cat, Owner

admin.site.register(Achievement)
admin.site.register(Owner)
# admin.site.register(Cat)
@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'color', 'birth_year', 'owner')
    # fields = ('name',)
    search_fields = ('name',)
    




    
admin.site.register(AchievementCat)