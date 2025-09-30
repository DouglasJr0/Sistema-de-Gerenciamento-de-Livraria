import csv
from pathlib import Path
from fpdf import FPDF
from database import buscar_livros

BASE_DIR = Path(__file__).parent.resolve()
EXPORT_DIR = BASE_DIR / 'exports'
EXPORT_DIR.mkdir(exist_ok=True)

# CSV
def exportar_csv():
    livros = buscar_livros()
    csv_path = EXPORT_DIR / "livros_exportados.csv"
    with open(csv_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'titulo', 'autor', 'ano_publicacao', 'preco'])
        writer.writerows(livros)
    print(f"✅ Exportado para {csv_path}")

# HTML com DataTables
def gerar_relatorio_html():
    livros = buscar_livros()
    html_path = EXPORT_DIR / "relatorio_livros.html"

    html = """<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Relatório de Livros</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css" rel="stylesheet">
</head>
<body class="p-4">
<div class="container">
<h1 class="mb-4">📚 Relatório de Livros</h1>
<table id="tabelaLivros" class="table table-striped table-bordered">
<thead class="table-dark">
<tr><th>ID</th><th>Título</th><th>Autor</th><th>Ano</th><th>Preço</th></tr>
</thead><tbody>
"""
    for livro in livros:
        html += f"<tr><td>{livro[0]}</td><td>{livro[1]}</td><td>{livro[2]}</td><td>{livro[3]}</td><td>R${livro[4]:.2f}</td></tr>\n"

    html += """
</tbody></table></div>
<script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/dataTables.bootstrap5.min.js"></script>
<script>
$(document).ready(function() { $('#tabelaLivros').DataTable({ "language": { "url": "//cdn.datatables.net/plug-ins/1.13.6/i18n/pt-BR.json" } }); });
</script></body></html>
"""
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Relatório HTML gerado em: {html_path}")

# PDF
def gerar_relatorio_pdf():
    livros = buscar_livros()
    pdf_path = EXPORT_DIR / "relatorio_livros.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Relatório de Livros", ln=True, align="C")
    pdf.ln(10)

    col_widths = [10, 60, 50, 20, 30]
    headers = ["ID", "Título", "Autor", "Ano", "Preço"]
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, 1, 0, "C")
    pdf.ln()

    pdf.set_font("Arial", size=10)
    for livro in livros:
        pdf.cell(col_widths[0], 10, str(livro[0]), 1)
        pdf.cell(col_widths[1], 10, livro[1][:30], 1)
        pdf.cell(col_widths[2], 10, livro[2][:25], 1)
        pdf.cell(col_widths[3], 10, str(livro[3]), 1, 0, "C")
        pdf.cell(col_widths[4], 10, f"R${livro[4]:.2f}", 1, 0, "R")
        pdf.ln()
    pdf.output(str(pdf_path))
    print(f"✅ Relatório PDF gerado em: {pdf_path}")
