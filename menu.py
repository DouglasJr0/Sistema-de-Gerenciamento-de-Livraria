from database import adicionar_livro, buscar_livros, atualizar_preco, remover_livro, buscar_por_autor, fechar_conexao
from file_manager import fazer_backup
from export_manager import exportar_csv, gerar_relatorio_html, gerar_relatorio_pdf

def menu():
    while True:
        print("\n===== Sistema de Gerenciamento de Livraria =====")
        print("1. Adicionar novo livro")
        print("2. Exibir todos os livros")
        print("3. Atualizar preço de um livro")
        print("4. Remover um livro")
        print("5. Buscar livros por autor")
        print("6. Exportar dados para CSV")
        print("8. Importar dados de CSV")
        print("9. Fazer backup do banco de dados")
        print("10. Gerar relatório HTML")
        print("11. Gerar relatório PDF")
        print("12. Sair")

        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                titulo = input("Título: ").strip()
                autor = input("Autor: ").strip()
                ano = int(input("Ano: "))
                preco = float(input("Preço: "))
                fazer_backup()
                adicionar_livro(titulo, autor, ano, preco)
                print("✅ Livro adicionado.")
            case "2":
                for livro in buscar_livros():
                    print(livro)
            case "3":
                id_livro = int(input("ID do livro: "))
                novo_preco = float(input("Novo preço: "))
                fazer_backup()
                if atualizar_preco(id_livro, novo_preco):
                    print("✅ Preço atualizado.")
                else:
                    print("❌ Livro não encontrado.")
            case "4":
                id_livro = int(input("ID do livro: "))
                fazer_backup()
                if remover_livro(id_livro):
                    print("✅ Livro removido.")
                else:
                    print("❌ Livro não encontrado.")
            case "5":
                autor = input("Nome do autor: ").strip()
                resultados = buscar_por_autor(autor)
                for livro in resultados:
                    print(livro)
            case "6": exportar_csv()
            case "7":
                fazer_backup()
                print("✅ Backup realizado.")
            case "8": gerar_relatorio_html()
            case "9": gerar_relatorio_pdf()
            case "10":
                print("👋 Saindo...")
                fechar_conexao()
                break
            case _: print("❌ Opção inválida.")
