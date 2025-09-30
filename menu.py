from utils import validar_ano, validar_preco, validar_texto, validar_id, validar_caminho_arquivo
from database import adicionar_livro, buscar_livros, atualizar_preco, remover_livro, buscar_por_autor
from file_manager import fazer_backup
from export_manager import exportar_csv, gerar_relatorio_html, gerar_relatorio_pdf
import csv

def menu():
    while True:
        print("\n=== Sistema de Gerenciamento de Livraria ===")
        print("1. Adicionar novo livro")
        print("2. Exibir todos os livros")
        print("3. Atualizar preço de um livro")
        print("4. Remover um livro")
        print("5. Buscar livros por autor")
        print("6. Exportar dados para CSV")
        print("7. Importar dados de CSV")
        print("8. Fazer backup do banco de dados")
        print("9. Gerar relatório HTML")
        print("10. Gerar relatório PDF")
        print("11. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = autor = ano = preco = None
            while titulo is None:
                titulo = validar_texto(input("Título: "), "Título")
            while autor is None:
                autor = validar_texto(input("Autor: "), "Autor")
            while ano is None:
                ano = validar_ano(input("Ano de publicação: "))
            while preco is None:
                preco = validar_preco(input("Preço: "))

            fazer_backup()
            adicionar_livro(titulo, autor, ano, preco)
            print("✅ Livro adicionado.")

        elif escolha == "2":
            livros = buscar_livros()
            if livros:
                for l in livros:
                    print(f"ID: {l[0]} | {l[1]} - {l[2]} ({l[3]}) - R${l[4]:.2f}")
            else:
                print("Nenhum livro cadastrado.")

        elif escolha == "3":
            id_livro = preco = None
            while id_livro is None:
                id_livro = validar_id(input("ID do livro: "))
            while preco is None:
                preco = validar_preco(input("Novo preço: "))

            fazer_backup()
            if atualizar_preco(id_livro, preco):
                print("✅ Preço atualizado.")
            else:
                print("❌ Livro não encontrado.")

        elif escolha == "4":
            id_livro = None
            while id_livro is None:
                id_livro = validar_id(input("ID do livro: "))

            fazer_backup()
            if remover_livro(id_livro):
                print("✅ Livro removido.")
            else:
                print("❌ Livro não encontrado.")

        elif escolha == "5":
            autor = input("Autor: ")
            livros = buscar_por_autor(autor)
            if livros:
                for l in livros:
                    print(f"ID: {l[0]} | {l[1]} - {l[2]} ({l[3]}) - R${l[4]:.2f}")
            else:
                print("Nenhum livro encontrado.")

        elif escolha == "6":
            exportar_csv()

        elif escolha == "7":
            caminho = None
            while caminho is None:
                caminho = validar_caminho_arquivo(input("Caminho do CSV: "))
            with open(caminho, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    validated = validar_csv_linha(row)
                    if validated:
                        adicionar_livro(*validated)
            print("✅ CSV importado.")

        elif escolha == "8":
            fazer_backup()
            print("✅ Backup realizado.")

        elif escolha == "9":
            gerar_relatorio_html()

        elif escolha == "10":
            gerar_relatorio_pdf()

        elif escolha == "11":
            print("👋 Saindo...")
            break

        else:
            print("❌ Opção inválida.")
