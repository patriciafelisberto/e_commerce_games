from rest_framework.routers import SimpleRouter

from .views import ProdutoViewSet, CarrinhoViewSet


router = SimpleRouter()
router.register('produtos', ProdutoViewSet)
router.register('carrinhos', CarrinhoViewSet)