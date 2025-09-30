import sqlite3
import os
import csv
from pathlib import Path
from datetime import datetime
import shutil
from fpdf import FPDF  # Certifique-se de que esta biblioteca esteja instalada

# Diretórios base
BASE_DIR = Path(__file__).parent.resolve()
DATA_DIR = BASE_DIR / 'data'
BACKUP_DIR = BASE_DIR / 'backups'
EXPORT_DIR = BASE_DIR / 'exports'
DB_PATH = DATA_DIR / 'livraria.db'

# Criar diretórios se não existirem
for directory in [DATA_DIR, BACKUP_DIR, EXPORT_DIR]:
    os.makedirs(directory, exist_ok=True)

# Conexão com o banco
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Criação da tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano_publicacao INTEGER NOT NULL,
        preco REAL NOT NULL
    )
""")
conn.commit()

# ---------------------- Funções de Backup ----------------------
def fazer_backup():
    now = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    backup_path = BACKUP_DIR / f'backup_livraria_{now}.db'
    shutil.copy(DB_PATH, backup_path)
    limpar_backups_antigos()

def limpar_backups_antigos(max_backups=5):
    backups = sorted(BACKUP_DIR.glob("backup_livraria_*.db"), key=os.path.getmtime, reverse=True)
    for backup in backups[max_backups:]:
        backup.unlink()

# ---------------------- Funções CRUD ----------------------
def adicionar_livro():
    try:
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        ano = int(input("Ano de publicação: "))
        preco = float(input("Preço: "))

        if not titulo or not autor or ano <= 0 or preco < 0:
            print("❌ Dados inválidos.")
            return

        fazer_backup()
        cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)",
                       (titulo, autor, ano, preco))
        conn.commit()
        print("✅ Livro adicionado com sucesso.")
    except ValueError:
        print("❌ Entrada inválida. Ano deve ser inteiro e preço numérico.")

def exibir_livros():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    if livros:
        print("\n📚 Livros cadastrados:")
        for livro in livros:
            print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]} | Preço: R${livro[4]:.2f}")
    else:
        print("📭 Nenhum livro cadastrado.")

def atualizar_preco():
    try:
        id_livro = int(input("ID do livro: "))
        novo_preco = float(input("Novo preço: "))
        fazer_backup()
        cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, id_livro))
        conn.commit()
        if cursor.rowcount:
            print("✅ Preço atualizado.")
        else:
            print("❌ Livro não encontrado.")
    except ValueError:
        print("❌ Entrada inválida.")

def remover_livro():
    try:
        id_livro = int(input("ID do livro a remover: "))
        fazer_backup()
        cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
        conn.commit()
        if cursor.rowcount:
            print("✅ Livro removido.")
        else:
            print("❌ Livro não encontrado.")
    except ValueError:
        print("❌ Entrada inválida.")

def buscar_por_autor():
    autor = input("Digite o nome do autor: ").strip()
    cursor.execute("SELECT * FROM livros WHERE autor LIKE ?", (f'%{autor}%',))
    resultados = cursor.fetchall()
    if resultados:
        for livro in resultados:
            print(f"ID: {livro[0]} | Título: {livro[1]} | Ano: {livro[3]} | Preço: R${livro[4]:.2f}")
    else:
        print("📭 Nenhum livro encontrado para esse autor.")

# ---------------------- Exportação e Importação CSV ----------------------
def exportar_csv():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    csv_path = EXPORT_DIR / "livros_exportados.csv"
    with open(csv_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'titulo', 'autor', 'ano_publicacao', 'preco'])
        writer.writerows(livros)
    print(f"✅ Exportado para {csv_path}")

def importar_csv():
    csv_path = input("Digite o caminho do arquivo CSV para importar: ").strip()
    if not Path(csv_path).exists():
        print("❌ Arquivo não encontrado.")
        return

    fazer_backup()

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        livros_inseridos = 0
        for row in reader:
            try:
                cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)",
                               (row['titulo'], row['autor'], int(row['ano_publicacao']), float(row['preco'])))
                livros_inseridos += 1
            except Exception as e:
                print(f"❌ Erro ao importar linha: {row} | Erro: {e}")
        conn.commit()
    print(f"✅ {livros_inseridos} livros importados.")

# ---------------------- Relatórios HTML e PDF ----------------------
def gerar_relatorio_html():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    html_path = EXPORT_DIR / "relatorio_livros.html"

    html = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Relatório de Livros</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- DataTables CSS -->
    <link href="https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css" rel="stylesheet">
</head>
<body class="p-4">
    <div class="container">
        <h1 class="mb-4">📚 Relatório de Livros</h1>
        <table id="tabelaLivros" class="table table-striped table-bordered">
            <thead class="table-dark">
                <tr>
                    <th>ID</th>
                    <th>Título</th>
                    <th>Autor</th>
                    <th>Ano</th>
                    <th>Preço</th>
                </tr>
            </thead>
            <tbody>
    """

    for livro in livros:
        html += f"""
                <tr>
                    <td>{livro[0]}</td>
                    <td>{livro[1]}</td>
                    <td>{livro[2]}</td>
                    <td>{livro[3]}</td>
                    <td>R${livro[4]:.2f}</td>
                </tr>
        """

    html += """
            </tbody>
        </table>
    </div>

    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- DataTables JS -->
    <script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.13.6/js/dataTables.bootstrap5.min.js"></script>

    <script>
        $(document).ready(function() {
            $('#tabelaLivros').DataTable({
                "language": {
                    "url": "//cdn.datatables.net/plug-ins/1.13.6/i18n/pt-BR.json"
                }
            });
        });
    </script>
</body>
</html>
    """

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Relatório HTML gerado em: {html_path}")

def gerar_relatorio_pdf():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    pdf_path = EXPORT_DIR / "relatorio_livros.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Relatório de Livros", ln=True, align="C")
    pdf.ln(10)

    # Cabeçalho da tabela
    pdf.set_font("Arial", 'B', 12)
    col_widths = [10, 60, 50, 20, 30]
    headers = ["ID", "Título", "Autor", "Ano", "Preço"]
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, 1, 0, "C")
    pdf.ln()

    # Conteúdo da tabela
    pdf.set_font("Arial", size=10)
    for livro in livros:
        pdf.cell(col_widths[0], 10, str(livro[0]), 1)
        pdf.cell(col_widths[1], 10, livro[1][:30], 1)  # limita texto
        pdf.cell(col_widths[2], 10, livro[2][:25], 1)
        pdf.cell(col_widths[3], 10, str(livro[3]), 1, 0, "C")
        pdf.cell(col_widths[4], 10, f"R${livro[4]:.2f}", 1, 0, "R")
        pdf.ln()

    pdf.output(str(pdf_path))
    print(f"✅ Relatório PDF gerado em: {pdf_path}")

# ---------------------- Menu Principal ----------------------
def menu():
    while True:
        print("\n===== Sistema de Gerenciamento de Livraria =====")
        print("1. Adicionar novo livro")
        print("2. Exibir todos os livros")
        print("3. Atualizar preço de um livro")
        print("4. Remover um livro")
        print("5. Buscar livros por autor")
        print("6. Exportar dados para CSV")
        print("7. Importar dados de CSV")
        print("8. Fazer backup do banco de dados")
        print("9. Sair")
        print("10. Gerar relatório HTML")
        print("11. Gerar relatório PDF")
        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1": adicionar_livro()
            case "2": exibir_livros()
            case "3": atualizar_preco()
            case "4": remover_livro()
            case "5": buscar_por_autor()
            case "6": exportar_csv()
            case "7": importar_csv()
            case "8": fazer_backup(); print("✅ Backup realizado.")
            case "9": print("👋 Saindo..."); break
            case "10": gerar_relatorio_html()
            case "11": gerar_relatorio_pdf()
            case _: print("❌ Opção inválida.")

if __name__ == "__main__":
    menu()
    conn.close()
