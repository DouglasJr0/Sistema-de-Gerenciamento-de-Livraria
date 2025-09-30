# Sistema de Gerenciamento de Livraria

📚 Projeto em **Python** para gerenciar livros utilizando **SQLite**.  
O sistema permite CRUD completo, backup automático, importação/exportação de dados e geração de relatórios em CSV, HTML e PDF.

---

## Funcionalidades

- Adicionar, atualizar e remover livros
- Buscar livros por autor
- Exportar dados para CSV
- Gerar relatórios HTML interativos com **DataTables** e **Bootstrap**
- Gerar relatórios PDF com **FPDF**
- Backup automático do banco de dados

---

## Tecnologias Utilizadas

- Python 3.11+
- SQLite (banco de dados)
- FPDF2 (para PDF)
- Bootstrap 5 (para HTML)
- DataTables (para tabelas interativas)

---

## Estrutura do Projeto

meu_sistema_livraria/
│
├─ data/
│ └─ livraria.db # Banco de dados SQLite
├─ backups/ # Backups automáticos do banco
├─ exports/ # Relatórios CSV, HTML e PDF
│
├─ database.py # CRUD e conexão SQLite
├─ file_manager.py # Backup automático
├─ export_manager.py # Exportação CSV, HTML e PDF
├─ menu.py # Menu interativo
├─ main.py # Ponto de entrada
└─ utils.py # Funções utilitárias (opcional)
---

## Como Rodar

1. Clone o repositório:

```bash
git clone https://github.com/SeuUsuario/Sistema-de-Gerenciamento-de-Livraria.git
cd Sistema-de-Gerenciamento-de-Livraria

Instale as dependências:

pip install -r requirements.txt

Execute o sistema:
python main.py
