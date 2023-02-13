SISTEMA DE E-COMMERCE DE GAMES COM DJANGO REST_FRAMEWORK

1 - clone o repositório;

2 - docker-compose up --build -d #Starta e roda os serviços definidos no "docker-compose.yml";

3 - docker-compose run web python manage.py makemigrations #Prepara as migrações dentro do ambiente docker;

4 - docker-compose run web python manage.py migrate #Efetua as migrações dentro do ambiente docker;

5 - docker-compose run web python manage.py runserver #Starta a aplicação game;

6 - acesse o site localhost:8000/admin #Acessar o Admin do Django e verificar o ambiente criado do back;

7 - Para usar o sistema de testes - "docker-compose run web python manage.py test";

8 - Endpoints:

#Lista todos os produtos
http://localhost:8000/api/v1/produtos/
#Lista um produto específico
http://localhost:8000/api/v1/produtos/{produto_id}

#Lista todos os carrinhos (vendas)
http://localhost:8000/api/v1/carrinhos/

#Lista um carrinho (venda) específico
http://localhost:8000/api/v1/carrinhos/{carrinho_id}

Obrigada e espero que tenha curtido o projeto!


