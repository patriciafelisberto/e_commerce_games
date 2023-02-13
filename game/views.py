from rest_framework import viewsets
from rest_framework.response import Response
from .models import Produto, Carrinho, Checkout
from .serializers import ProdutoSerializer, CarrinhoSerializer, CheckoutSerializer
from rest_framework import mixins


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering', 'nome')
        if ordering == 'valor':
            queryset = queryset.order_by('preco')
        elif ordering == 'popularidade':
            queryset = queryset.order_by('-score')
        else:
            queryset = queryset.order_by(ordering)
        return queryset

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer


class CheckoutViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer




