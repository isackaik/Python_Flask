## API DE USUÁRIO
Este projeto foi parte de um trabalho na disciplica de Banco de Dados 1, na Universidade Federal de Sergipe, ministrada pelo professor André Britto. 

### Linguagens e Frameworks
- Python
- Flask

#### Bibliotecas Adicionais
- SQLAlchemy
- Flask-Restful
- Flask-Swagger
- Flask-Cors
- Flask-HTTPAuth
- Psycopg2
- Requests
- Flask-Migrate

### Descrição do projeto
Na API, foi desenvolvido operações básicas para manipulação com o banco, o famoso CRUD. Possui método para a consulta, alteração e exclusão de usuário através do CPF e o método também de criação de usuário.

O usuário possui os seguintes atributos:
- CPF
- Nome
- Data de nascimento

### Configuração do projeto
Para conseguir rodar o projeto, algumas configurações iniciais são necessárias. Para os comandos abaixo, é necessário que você já tenha o Python instalado em sua máquina.
- Baixe ou clone o projeto em sua máquina local.
- Caso você baixe diretamente do GitHub, o arquivo virá zipado. Extraia-o para uma pasta de sua preferência.
- Em algum editor de texto ou IDE(VS Code, PyCharm, Sublime, etc), abra a pasta do projeto.
- Abra algum terminal dentro do editor de texto e digite o seguinte comando:
``` cmd
python -m venv venv
```
- O comando acima fará com que seja criado um ambiente virtual, em que as bibliotecas e suas versões sejam armazenadas nesse ambiente, evitando conflito com outras versões de sua máquina física.
- Em seguida, digite o comando abaixo:
```
pip install -r requirements.md
```
- O comando acima fará com que seja instalado todas as bibliotecas do arquivo requirements.md. Elas fazem parte do conjunto de bibliotecas usadas no projeto.

Finalizado a execução do comando acima, o projeto já estará com o ambiente virtual criado, bibliotecas instaladas e pronto para iniciar o servidor.

O arquivo a ser executado para subir a API é o "app.py".

Ao ser iniciado corretamente, a aplicação irá subir, por padrão, no endereço: http://127.0.0.1:5000 .

### Rotas

- http://127.0.0.1:5000 - irá abrir a rota padrão do servidor. Nela contém apenas a interface de "Not Found" pois não foi desenvolvido algo para essa rota.

- http://127.0.0.1:5000/usuario/ - esta é a rota de criação de usuário, através do método POST. Através de programas que são capazes de realizar requisições(como o Postman, Insomnia), é possível inserir informações do usuário e realizar sua inserção no banco de dados, se for inserido corretamente.

- http://127.0.0.1:5000/usuario/{cpf} - nesta rota é possível realizar a consulta(método GET), exclusão(método DELETE) e alteração de um usuário(método PUT). É necessário parar o parâmetro "cpf", apenas com números, sem pontuação. 

- http://127.0.0.1:5000/docs - esta é a melhor rota para acessar na api. Nela contém a documentação da API, falando sobre o projeto, possui informações de contato e por ela é possível também realizar as requisições citadas acima, de criação, consulta, alteração e exclusão de usário.

