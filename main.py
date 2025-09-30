from database import criar_tabela
from file_manager import inicializar_diretorios
from menu import menu

def main():
    inicializar_diretorios()
    criar_tabela()
    menu()

if __name__ == "__main__":
    main()
