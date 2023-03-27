from django.contrib import admin

from .models import SubCategory, SuperCategory
from .forms import SubCategoryForm


class SubCategoryInline(admin.TabularInline):
    model = SubCategory


class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_category',)
    inlines = (SubCategoryInline,)

admin.site.register(SuperCategory, SuperRubricAdmin)


class SubRubricAdmin(admin.ModelAdmin):
    form = SubCategoryForm


admin.site.register(SubCategory, SubRubricAdmin)
