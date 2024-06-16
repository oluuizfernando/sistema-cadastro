## Cadastro Básico de Usuários com Python e Django

Este repositório contém um projeto simples desenvolvido em Python utilizando o framework Django. O projeto permite o cadastro básico de usuários com informações mínimas de nome e idade.

### Funcionalidades:

- **Cadastro de Usuários:** Permite inserir novos usuários especificando apenas nome e idade.
- **Listagem de Usuários:** Exibe todos os usuários cadastrados, mostrando seus nomes e idades.

### Estrutura do Projeto:

- `manage.py`: Script de gerenciamento do Django para execução de comandos.
- `requirements.txt`: Lista de dependências do Python necessárias para o projeto.
- `/meuapp/`: Aplicação principal onde estão definidos os modelos, views, URLs e templates.
  - `models.py`: Define o modelo de dados para o usuário, incluindo nome e idade.
  - `views.py`: Contém as views que processam as requisições HTTP e renderizam as respostas.
  - `urls.py`: Mapeia as URLs para as views correspondentes.
  - `templates/`: Diretório contendo os templates HTML para renderização das páginas.

### Como usar:

1. **Configuração do Ambiente:**
   - Instale as dependências listadas em `requirements.txt`.
   - Configure seu ambiente Django conforme necessário (banco de dados, configurações locais).

2. **Execução:**
   - Utilize `python manage.py runserver` para iniciar o servidor de desenvolvimento.
   - Acesse `http://localhost:8000` no seu navegador para interagir com a aplicação.

### Contribuição:

Este projeto é um exemplo simples de cadastro de usuários usando Django, ideal para iniciantes que desejam aprender sobre criação básica de CRUD em aplicações web.
