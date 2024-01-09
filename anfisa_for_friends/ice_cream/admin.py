from django.contrib import admin
from .models import Category, IceCream, Wrapper, Topping


admin.site.empty_value_display = 'Не задано'


class IceCreamInLine(admin.TabularInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (IceCreamInLine,)
    list_display = ('title',)


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_on_main',
        'is_published',
        'category',
        'wrapper'

    )
    list_editable = (
        'is_on_main',
        'is_published',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)


admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(Wrapper)
admin.site.register(Topping)
# Register your models here.
