from django.contrib import admin
from productapp.models import Product

class ManageProduct(admin.ModelAdmin):
  list_display=["name","price","stock","isTrending"] #listでobjectの形を見やすいようにする
  list_editable=["price","stock","isTrending"]  #listで直接修正できる
  list_per_page=5  #listの1ページでいくらの数を表示したいか
  search_fields=["name"]  #商品名(name)で検索できるinputがある
  list_filter=["isTrending"]  #checkが入っていたら、当てはまる商品が表示される

# Register your models here.
admin.site.register(Product,ManageProduct)