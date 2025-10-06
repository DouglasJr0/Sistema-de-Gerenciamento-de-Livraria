# Sistema de Gerenciamento de Livraria

📚 Projeto em **Python** para gerenciar livros utilizando **SQLite**.
O sistema oferece CRUD completo, backup automático, importação/exportação de dados e geração de relatórios em CSV, HTML e PDF.

---

## Funcionalidades

### Operações CRUD

* Adicionar novo livro
* Exibir todos os livros cadastrados
* Atualizar preço de um livro
* Remover um livro
* Buscar livros por autor

### Manipulação de Arquivos

* Exportar dados para CSV
* Importar dados de CSV
* Backup automático do banco de dados
* Limpeza automática de backups antigos (mantém apenas os 5 mais recentes)

### Relatórios

* Gerar relatórios HTML interativos com **DataTables** e **Bootstrap**
* Gerar relatórios PDF com **FPDF**, formatação profissional

### Validações de Entrada

* **Título/Autor**: Não podem estar vazios
* **Ano**: Deve ser um número entre 1000 e 2100
* **Preço**: Deve ser um número positivo

---

## Tecnologias Utilizadas

* Python 3.11+
* SQLite
* FPDF2 (para PDF)
* Bootstrap 5 (para HTML)
* DataTables (para tabelas interativas)

---

## Estrutura do Projeto

```bash
meu_sistema_livraria/
│
├─ data/                  # Banco SQLite
│   └─ livraria.db
├─ backups/               # Backups automáticos
├─ exports/               # Arquivos CSV, HTML e PDF
│
├─ database.py            # CRUD e conexão SQLite
├─ file_manager.py        # Backup automático e limpeza
├─ export_manager.py      # Exportação CSV, HTML e PDF
├─ menu.py                # Menu interativo
├─ main.py                # Ponto de entrada
├─ utils.py               # Funções auxiliares (validações)
└─ requirements.txt       # Dependências do Python
```

## Pré-requisitos

* Python 3.11 ou superior instalado
* Pip atualizado
* Bibliotecas listadas em `requirements.txt`

## Como Rodar

1. Clone o repositório:

```bash
git clone https://github.com/SeuUsuario/Sistema-de-Gerenciamento-de-Livraria.git
cd Sistema-de-Gerenciamento-de-Livraria
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o sistema:

```bash
python main.py
```

## Banco de Dados

O sistema utiliza SQLite com a seguinte estrutura:

**Tabela: livros**

* `id`: INTEGER PRIMARY KEY AUTOINCREMENT
* `titulo`: TEXT NOT NULL
* `autor`: TEXT NOT NULL
* `ano_publicacao`: INTEGER NOT NULL
* `preco`: REAL NOT NULL

## Funcionalidades de Backup

* Backup automático antes de qualquer modificação (inserção, atualização, remoção)
* Manutenção automática de apenas 5 backups mais recentes
* Nomenclatura com timestamp: `backup_livraria_YYYY-MM-DD_HHMMSS.db`

## Menu do Sistema

1. Adicionar novo livro
2. Exibir todos os livros
3. Atualizar preço de um livro
4. Remover um livro
5. Buscar livros por autor
6. Exportar dados para CSV
7. Importar dados de CSV
8. Fazer backup do banco de dados
9. Gerar relatório HTML
10. Gerar relatório PDF
11. Sair

## Observações

* Para abrir arquivos PDF dentro do VSCode, use a extensão **vscode-pdf**
* Os relatórios HTML são interativos, permitindo ordenação e pesquisa nos dados

Link do projeto rodando:
https://drive.google.com/drive/folders/16qf-U9h_fzIvS8Pt3uMCmRganP48pAjT?usp=sharing
