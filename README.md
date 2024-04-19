# VAAlugar-API
Para instalar:
use o arquivo requirements.txt para instalar os módulos. No windows:
pip install -r requirements.txt
Recomendo instalação em um ambiente virtual

Para executar localmente, em ambiente Windows:
flask run --host 0.0.0.0 --port 5000 --reload


API do projeto VA'Alugar, como projeto pessoal para a Sprint Desenvolvimento Full Stack Básico da Especialização em Engenharia de Software da PUC Rio.

Requisitos do MVP da Sprint:

- A API deverá ser implementada em Python e com Flask com pelo menos 3 rotas (por exemplo, “/cadastrar_usuario” , “/buscar_usuario” e “/deletar_usuario” ), sendo que pelo menos uma delas deve implementar o método POST (por exemplo, na rota de cadastro).
- Fazer o uso de um banco de dados SQLite, PostgreSQL ou MySQL com pelo menos uma tabela (por exemplo, tabela de usuários cadastrados). Observação : caso seja utilizado PostgreSQL ou MySQL, deve ser entregue um script Python ou SQL para criação, configuração e carga inicial de dados. O script deve estar bem localizado no projeto e todas as orientações para execução devem estar claras no arquivo README.md
- Qualidade da Documentação da API em Swagger.
- Criatividade e Inovação

O que é o projeto VA'Alugar?
  Aqui brincamos com as ideias de VA'A e alugar. 
  No mundo da canoagem, uma VA'A é uma canoa do tipo havaiana ou polinésia, sendo uma embarcação ocupada por 1 a 7 remadores e conectada em sua lateral a um flutuador ou bóia, chamada ama. Saiba mais em: https://kanaloario.com/diferenca-de-canoa-havaiana-canoa-polinesia-ou-vaa/.
  Pessoalmente, gosto de remar em uma Vaa dos tipos OC4 e OC6. Não me interesso muito por competições. O que eu gosto é de remar em lugares novos, e chegar a ilhas e praias só acessíveis por embarcações. Então o meu problema é: se eu quiser remar em algum lugar novo, onde posso encontrar uma canoa para remar? Por exemplo, se eu for para Vitória, no Espírito Santo, onde encontro alguém disposto a me alugar uma V1? Ou, se eu for dono de uma OC4, como acho pessoas interessadas em alugar a minha canoa para passearem num fim de semana?
  Podemos assim dizer que o VA'Alugar é o AirBNB das canoas polinésias.

REQUISITOS FUNCIONAIS DO PROJETO
- Para este MVP, implementaremos 4 funcionalidades em uma API:
  1. Listar canoas disponíveis para locação em determinado lugar.
  2. Registrar o interessa em reservar a canoa para uma determinada data, informando telefone do usuario, canoa escolhida e data para locação.
  3. Listar, a partir de um número de telefone, todas as reservas feitas usando este número.
  4. Postar um comentário relatando a experiência com a locação da canoa.
- Outras funcionalidades podem ser oferecidas, opcionalmente.
- Para persistência dos dados, será usado um banco de dados SQLite. 


CATALOGO DE REQUISIÇOES E RESPOSTAS

1. Usuario busca canoas disponíveis por Município. Metodo: GET. API retorna LISTA de canoas disponiveis no municipio escolhido.
2. Usuario escolhe uma canoa da lista, informa uma data e numero de telefone. Metodo: POST. API registra estas informacoes na tabela de transacoes.
3. Usuario informa seu numero de telefone. Metodo: GET. API retorna LISTA de transacoes realizadas com estes dados.
4. Usuario escolhe uma transacao e escreve seu comentario. Metodo: POST. API atualiza tabela com estes dados.

ESTRUTURA DA PASTA
- subpasta database: armazenar o banco de dados SQLite
- subpasta model: modelos SQLAlchemy
- subpasta schemas: modelos Pydantic para comunicação com camada cliente
- arquivo app.py, nome default utilizado pelo flask
- arquivo README.md
- arquivo requirements.txt
- outros arquivos para ajuda e documentação: Modelo de Entidades e Relacionamentos.pdf, Modelo Logico VAAlugar 0.1.pdf e Procedimento de criação de BD.

DOCUMENTACAO
A API foi desenvolvida com suporte à documentação em Swagger, ReDoc e RapiDoc. Acessar em http://127.0.0.1:5000/openapi/ e escolher o formato de documentação preferido.

