from django.contrib import admin
from .models import Produto, Carrinho, Checkout


class CheckoutAdmin(admin.TabularInline):
    model = Checkout
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    pass


class CarrinhoAdmin(admin.ModelAdmin):
    date_hierarchy = 'data'
    list_filter = ['data', 'valor_compra', 'metodo_pagamento']

    inlines = [CheckoutAdmin]
    list_display = ['data', 'valor_compra', 'metodo_pagamento']


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Carrinho, CarrinhoAdmin)
