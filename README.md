Sistema de Cadastro de Clientes
Um sistema web completo e funcional para a gestão de clientes, desenvolvido com Python e Django. Este projeto demonstra um ciclo de desenvolvimento completo, desde a criação da base de dados e funcionalidades essenciais até à implantação (deployment) num ambiente de produção.

🚀 Funcionalidades Principais
Este sistema possui todas as funcionalidades essenciais para uma gestão de clientes (CRUD), com uma interface limpa e responsiva.

Registar Clientes: Adicionar novos clientes à base de dados através de um formulário simples.

Listar Clientes: Ver todos os clientes registados numa tabela organizada e paginada.

Editar Clientes: Atualizar as informações de qualquer cliente existente.

Excluir Clientes: Remover clientes da base de dados com uma etapa de confirmação.

Busca Inteligente: Pesquisar clientes por nome ou e-mail.

Paginação: A lista de clientes é dividida em páginas para garantir a performance e a usabilidade, mesmo com um grande volume de dados.

Validação de Dados: O sistema valida os dados de entrada, como o formato do telefone, para garantir a integridade da informação.

🛠️ Tecnologias Utilizadas
Este projeto foi construído com tecnologias modernas e muito procuradas no mercado:

Backend:

Python 3.13

Django 5.2

Gunicorn (Servidor de Aplicação para produção)

Frontend:

HTML5

CSS3

Bootstrap 5 (para um design moderno e responsivo)

Base de Dados:

MySQL (para desenvolvimento local)

PostgreSQL (para o ambiente de produção)

Implantação (Deployment):

Render.com (Plataforma como Serviço - PaaS)

Git & GitHub (para controlo de versão e implantação contínua)

💻 Como Executar o Projeto Localmente
Para executar este projeto na sua máquina, siga os seguintes passos:

Clone o repositório:

git clone https://github.com/Robertsan31/Costumer_registration.git

Navegue para a pasta do projeto e crie um ambiente virtual:

cd Costumer_registration/registration
python -m venv venv
source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

Configure a sua base de dados local no arquivo settings.py.

Aplique as migrações:

python manage.py migrate

Execute o servidor de desenvolvimento:

python manage.py runserver

O site estará disponível em http://127.0.0.1:8000.

📸 Capturas de Ecrã


<img width="1546" alt="Captura de Tela 2025-06-07 às 10 27 56" src="https://github.com/user-attachments/assets/3529a334-0722-4b55-b4e2-170db107d799" />
<img width="1360" alt="Captura de Tela 2025-06-07 às 10 28 26" src="https://github.com/user-attachments/assets/c6fc9bb6-6715-4edb-a4cf-0bbad9dcde4c" />
<img width="1373" alt="Captura de Tela 2025-06-07 às 10 28 53" src="https://github.com/user-attachments/assets/2b0664ce-d687-4a2b-80dd-05c75b23fb8f" />
