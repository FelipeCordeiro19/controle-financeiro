📊 WhatsApp Finance Bot

Este projeto é um bot de WhatsApp para controle financeiro pessoal, utilizando Twilio, Render e Python para registrar gastos em uma planilha do Excel.

🚀 Funcionalidades

📩 Envie mensagens para o bot com a descrição do gasto (ex: "Almoço, 19.90").

📊 O bot processa a mensagem e registra os dados em uma planilha do Excel.

🔄 Integração com Twilio para receber mensagens do WhatsApp.

☁️ Hospedagem no Render para manter o bot ativo e acessível.

🛠 Tecnologias Utilizadas

Python 🐍

Flask 🌐

Twilio API 💬

Render ☁️

Pandas (para manipulação de planilhas Excel) 📑

📦 Como Configurar

1️⃣ Clone o Repositório

 git clone https://github.com/FelipeCordeiro19/controle-financeiro.git
 cd controle-financeiro

2️⃣ Crie um Ambiente Virtual (opcional, mas recomendado)

 python -m venv venv
 source venv/bin/activate  # Linux/Mac
 venv\Scripts\activate  # Windows

3️⃣ Instale as Dependências

 pip install -r requirements.txt

4️⃣ Configure as Variáveis de Ambiente

Crie um arquivo .env e adicione as credenciais do Twilio:

TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_number
RENDER_URL=your_render_url

5️⃣ Execute o Bot

 python app.py

📞 Como Usar

Envie uma mensagem para o número do bot no WhatsApp com o formato:

Almoço, 19.90

O bot irá registrar o gasto na planilha Excel.

A planilha será atualizada automaticamente e armazenada.

📂 Estrutura do Projeto

📂 controle-financeiro
├── 📄 app.py        # Código principal do bot
├── 📄 requirements.txt  # Dependências do projeto
├── 📄 . gitignore   #Arquivos da sua pasta que devem ser ignorados pelo Git

🤝 Contribuição

Sinta-se à vontade para contribuir! Faça um fork do repositório, crie uma branch e envie um pull request. 😃

📜 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo.

⚙️ Desenvolvimento

Este projeto está sendo desenvolvido e em testes iniciais, ainda será costantemente atualizado!

Desenvolvido por Felipe Cordeiro.

