from django.contrib import admin
from .models import Blog,Category
from django.utils.safestring import mark_safe

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug","selected_categories")   # basliklari object <1> tarzi  degilde normal bir sekilde gosterir ayriyetten isactive ve ishome var mi yok mu onu gosterir 
    list_editable = ("is_active","is_home","slug")     # tiklama ile yapabilmemize olanak saglar 
    search_fields = ("title","description",)   # baslik ve description arama yeri ekler ve ona gore filtreler
    readonly_fields = ("slug",)  # burasi aciklamanin kalici hale gelmesini sagliyor yani adminden degistiremiyoruz 
    list_filter = ("is_active","is_home","categories",)
    
    def selected_categories(self, obj):
        categories = obj.categories.all()
        
        if not categories:
            return "No categories available"
        
        html = "<ul>"
        for category in categories:
            html += "<li>" + category.name + "</li>"
        html += "</ul>"
        
        return mark_safe(html)
        
    



admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)