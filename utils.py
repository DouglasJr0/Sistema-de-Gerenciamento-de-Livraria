from pathlib import Path

def validar_texto(valor, nome_campo="Campo"):
    valor = valor.strip()
    if valor:
        return valor
    print(f"❌ {nome_campo} não pode estar vazio.")
    return None

def validar_ano(valor):
    try:
        ano = int(valor)
        if 1000 <= ano <= 2100:
            return ano
    except:
        pass
    print("❌ Ano inválido. Deve ser um número entre 1000 e 2100.")
    return None

def validar_preco(valor):
    try:
        preco = float(valor)
        if preco >= 0:
            return preco
    except:
        pass
    print("❌ Preço inválido. Deve ser um número positivo.")
    return None

def validar_id(valor):
    try:
        id_num = int(valor)
        if id_num > 0:
            return id_num
    except:
        pass
    print("❌ ID inválido. Deve ser um número inteiro positivo.")
    return None

def validar_csv_linha(linha):
    t = validar_texto(linha.get('titulo', ''), "Título")
    a = validar_texto(linha.get('autor', ''), "Autor")
    y = validar_ano(linha.get('ano_publicacao', ''))
    p = validar_preco(linha.get('preco', ''))
    if None not in [t, a, y, p]:
        return t, a, y, p
    return None

def validar_caminho_arquivo(caminho):
    path = Path(caminho.strip())
    if path.exists() and path.suffix.lower() == '.csv':
        return path
    print("❌ Caminho inválido ou não é um arquivo CSV.")
    return None
