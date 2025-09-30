from utils import validar_ano, validar_preco, validar_texto
from database import adicionar_livro, buscar_livros, atualizar_preco, remover_livro, buscar_por_autor
from file_manager import fazer_backup
from export_manager import exportar_csv, gerar_relatorio_html, gerar_relatorio_pdf

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
            titulo = None
            while titulo is None:
                titulo = validar_texto(input("Título: "), "Título")

            autor = None
            while autor is None:
                autor = validar_texto(input("Autor: "), "Autor")

            ano = None
            while ano is None:
                ano = validar_ano(input("Ano de publicação: "))

            preco = None
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
            id_livro = input("ID do livro: ")
            preco = None
            while preco is None:
                preco = validar_preco(input("Novo preço: "))
            fazer_backup()
            if atualizar_preco(int(id_livro), preco):
                print("✅ Preço atualizado.")
            else:
                print("❌ Livro não encontrado.")

        elif escolha == "4":
            id_livro = input("ID do livro: ")
            fazer_backup()
            if remover_livro(int(id_livro)):
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
            caminho = input("Caminho do CSV: ")
            try:
                from database import adicionar_livro
                import csv
                with open(caminho, newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        t = validar_texto(row['titulo'], "Título")
                        a = validar_texto(row['autor'], "Autor")
                        y = validar_ano(row['ano_publicacao'])
                        p = validar_preco(row['preco'])
                        if None not in [t,a,y,p]:
                            adicionar_livro(t,a,y,p)
                print("✅ CSV importado.")
            except Exception as e:
                print(f"Erro: {e}")

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
