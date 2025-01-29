from django.contrib import admin
from .models import *
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','create','update','image','sub_category')
    list_filter = ('create',)
    prepopulated_fields = {
        'slug':('name',)
    }
class ProductVariant(admin.StackedInline):
    model = Variants
    extra = 2
class ImageInlines(admin.TabularInline):
    model = Image
    extra = 2
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'create', 'update','mount','available','unit_price','discounting','total_price',]
    list_filter = ['available',]
    list_editable = ['mount','available']
    raw_id_fields = ('Category',)
    inlines = [ProductVariant,ImageInlines]
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name','id']
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name','id']
class VariantAdmin(admin.ModelAdmin):
    list_display = ['name','id']
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','create','rate']


admin.site.register(Color,ColorAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(product,ProductAdmin)
admin.site.register(Variants,VariantAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Image)