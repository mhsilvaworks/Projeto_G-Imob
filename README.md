# G-Imob 🏠

![Status](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-07405e?style=for-the-badge&logo=sqlite&logoColor=white)

> Uma solução inteligente e simples para gestão de imóveis.

---


## 💻 Sobre o Projeto

**G-Imob** é uma aplicação web desenvolvida para simplificar a rotina de proprietários de imóveis e locadores. Diferente de sistemas ERP complexos, o G-Imob foca no essencial: gerenciar propriedades, rastrear inquilinos e organizar contratos de aluguel em uma interface limpa e amigável.

Este projeto foi desenvolvido como **Trabalho de Conclusão do Curso CS50 de Harvard**.

## ✨ Principais Funcionalidades

* **🏡 Gestão de Imóveis:** Cadastro e organização de bens imóveis com detalhes (endereço, valor, tipo).
* **👥 Controle de Inquilinos:** Vínculo de inquilinos a imóveis específicos e gerenciamento de contatos.
* **💾 Banco de Dados Robusto:** Persistência de dados utilizando SQLite (`gerimovel.db`).
* **🔒 Seguro e Privado:** Autenticação baseada em sessões garante que cada usuário gerencie apenas seus próprios dados.
* **📱 Design Responsivo:** Interface construída para funcionar em desktops e visualizações móveis básicas.

## 🛠 Tecnologias Utilizadas

* **Backend:** Python 3, Flask (Framework Web)
* **Banco de Dados:** SQLite, SQLAlchemy (Biblioteca CS50)
* **Frontend:** HTML5, CSS3, Bootstrap, Jinja2 Templating

## 🚀 Como Rodar Localmente

Se você deseja rodar este projeto na sua máquina, siga os passos abaixo:

1.  **Clone o repositório**
    ```bash
    git clone [https://github.com/SEU-USUARIO/g-imob.git](https://github.com/SEU-USUARIO/g-imob.git)
    cd g-imob
    ```

2.  **Instale as Dependências**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute o Servidor**
    ```bash
    flask run
    ```

4.  **Acesse**
    Abra seu navegador e vá para `http://127.0.0.1:5000`

## 📂 Estrutura do Projeto

```text
g-imob/
├── app.py              # Controlador principal da aplicação (Rotas e Lógica)
├── gerimovel.db        # Banco de Dados SQLite
├── requirements.txt    # Dependências do Python
├── static/             # Arquivos estáticos (CSS, Imagens, JS)
└── templates/          # Templates HTML (Jinja2)
📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido por Matheus
