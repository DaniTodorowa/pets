from django.contrib import admin

from petsnew.models import Pet, Like

class LikeInLineAdmin(admin.TabularInline):
    model = Like


class PetAdmin(admin.ModelAdmin):
    #fields = ('type', 'name', 'age')
    list_display = ('id','type', 'name', 'age')
    list_filter = ('type', 'age')
    inlines = [
        LikeInLineAdmin,
    ]


admin.site.register(Pet, PetAdmin)
admin.site.register(Like)