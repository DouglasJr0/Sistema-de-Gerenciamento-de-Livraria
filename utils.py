def validar_ano(ano):
    try:
        ano = int(ano)
        if 1000 <= ano <= 2100:
            return ano
        else:
            raise ValueError
    except ValueError:
        print("Ano inválido! Digite um número entre 1000 e 2100.")
        return None

def validar_preco(preco):
    try:
        preco = float(preco)
        if preco >= 0:
            return preco
        else:
            raise ValueError
    except ValueError:
        print("Preço inválido! Digite um número positivo.")
        return None

def validar_texto(texto, campo):
    if not texto.strip():
        print(f"{campo} não pode estar vazio.")
        return None
    return texto.strip()

from pathlib import Path

def criar_pasta(caminho):
    Path(caminho).mkdir(parents=True, exist_ok=True)

def formatar_preco(valor):
    try:
        return f"R${valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return "R$0,00"
