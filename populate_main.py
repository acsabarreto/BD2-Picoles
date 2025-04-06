from time import sleep
from uuid import uuid4

from tqdm import tqdm  # pip install tqdm
from sqlalchemy.orm import Session

from helpers import gerar_string, gerar_int, gerar_float, gerar_cor
from db import get_session
from models import (AditivoNutritivo, Sabor, TipoEmbalagem,
                    TipoPicole, Ingrediente, Conservante,
                    Revendedor, Lote, NotaFiscal, Picole)


#1) Aditivos Nutritivos
def populate_aditivo_nutritivo():
    print(f'Cadastrando Aditivo Nutritivo: ')

    # Estamos criando a sessão antes pois vamos inserir vários objetos
    cor = gerar_cor()
    with get_session() as session:
        for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            nome: str = gerar_string()
            formula_quimica: str = gerar_string(frase=True)
            data = {
                "id": n,
                "nome":nome, 
                "formula_quimica":formula_quimica
            }
            aditivo_nutritivo: AditivoNutritivo = AditivoNutritivo(**data)
            session.add(aditivo_nutritivo)
            sleep(0.05)
        
        # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
        session.commit()
    print('Aditivos Nutritivos cadastrados com sucesso')

#2) Sabores
def populate_sabor():
    print(f'Cadastrando Sabores: ')

    cor = gerar_cor()
    with get_session() as session:
        for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            nome: str = gerar_string()
            data = {
                "id": n,
                "nome": nome
            }
            sabor: Sabor = Sabor(**data)
            session.add(sabor)
            sleep(0.05)
            
        # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
        session.commit()
    print('Sabores cadastrados com sucesso')

#3) Tipos Embalagem
def populate_tipo_embalagem():
    print(f'Cadastrando Tipos Embalagem: ')

    cor = gerar_cor()

    with get_session() as session:
        for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            nome: str = gerar_string()
            
            data = {
                "id": n,
                "nome": nome
            }
            
            tipo_embalagem: TipoEmbalagem = TipoEmbalagem(**data)
            session.add(tipo_embalagem)
            sleep(0.05)
            
        # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
        session.commit()
    print('Tipos Embalagem cadastrados com sucesso')


#4) Tipos Picole
def populate_tipo_picole():
    print(f'Cadastrando Tipos Picolé: ')

    cor = gerar_cor()

    with get_session() as session:
        for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            nome: str = gerar_string()
            data = {
                "id": n,
                "nome": nome
            }
            tipo_picole: TipoPicole = TipoPicole(**data)
            session.add(tipo_picole)
            sleep(0.05)
            
        # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
        session.commit()
    print('Tipos Picolé cadastrados com sucesso')


#5) Ingredientes
def populate_ingrediente():
    print(f'Cadastrando Ingredientes: ')

    cor = gerar_cor()

    with get_session() as session:
        for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            nome: str = gerar_string()
            data = {
                "id": n,
                "nome": nome
            }
            ingrediente: Ingrediente = Ingrediente(**data)
            session.add(ingrediente)
            sleep(0.05)
            
        # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
        session.commit()
    print('Ingredientes cadastrados com sucesso')

#6) Conservantes
def populate_conservante():
    print(f'Cadastrando Conservantes: ')

    cor = gerar_cor()
    with get_session() as session:
        for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            nome: str = gerar_string()
            descricao: str = gerar_string(frase=True)
            
            data = {
                "id": n,
                "nome": nome,
                "descicao": conservante
            }
            conservante: Conservante = Conservante(**data)
            session.add(conservante)
            sleep(0.05)
            
        # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
        session.commit()
    print('Conservantes cadastrados com sucesso')


#7) Revendedor
def populate_revendedor():
    print(f'Cadastrando Revendedores: ')

    cor = gerar_cor()
    with get_session() as session:
        for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            cnpj: str = gerar_string()
            razao_social: str = gerar_string()
            contato: str = gerar_string()

            data = {
                "id": n,
                "cnpj":cnpj,
                "razao_social":razao_social,
                "contato":contato
            }

            revendedor: Revendedor = Revendedor(**data)
            session.add(revendedor)
            sleep(0.05)
            
        # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
        session.commit()
    print('Revendedores cadastrados com sucesso')


#8) Lote
def populate_lote():
    print(f'Cadastrando Lotes: ')

    cor = gerar_cor()

    with get_session() as session:
        for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            id_tipo_picole: int = gerar_int()
            quantidade: int = gerar_int()

            data = {
                "id": n,
                "id_tipo_picole": id_tipo_picole,
                "quantidade": quantidade
            }
            lote: Lote = Lote(**data)
            session.add(lote)
            sleep(0.05)
            
        # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
        session.commit()
    print('Lotes cadastrados com sucesso')


#9) Nota Fiscal
def populate_nota_fiscal():
    print(f'Cadastrando Notas Fiscais: ')

    cor = gerar_cor()
    with get_session() as session:
        for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            valor: float = gerar_float(digitos=3)
            numero_serie: str = gerar_string()
            descricao: str = gerar_string(frase=True)
            id_revendedor: int = gerar_int()
            data = {
                "id": n,
                "valor": valor,
                "numero_serie": numero_serie,
                "descricao": descricao,
                "id_revendedor": id_revendedor
            }
            nota_fiscal: NotaFiscal = NotaFiscal(**data)
            session.add(nota_fiscal)
            sleep(0.05)
            
        # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
        session.commit()
    print('Notas Fiscais cadastradas com sucesso')


#10) Piole
def populate_picole():
    print(f'Cadastrando Picolés: ')

    cor = gerar_cor()
    with get_session() as session:
        for n in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            preco: float = gerar_float()
            id_sabor: int = gerar_int()
            id_tipo_embalagem: int = gerar_int()
            id_tipo_picole: int = gerar_int()

            picole: Picole = Picole(preco=preco, id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole)
            
            # Ingredientes
            for n in range(5):
                nome: str = gerar_string()
                ingrediente: Ingrediente = Ingrediente(nome=nome)
                picole.ingredientes.append(ingrediente)

            op = gerar_float()
            if op > 5:
                for _ in range(3):
                    # Aditivos Nutritivos
                    nome: str = gerar_string()
                    formula_quimica: str = gerar_string(frase=True)
                    aditivo_nutritivo: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)
                    picole.aditivos_nutritivos.append(aditivo_nutritivo)
            else:
                for _ in range(3):
                    # Conservantes
                    nome: str = gerar_string()
                    descricao: str = gerar_string(frase=True)
                    conservante: Conservante = Conservante(nome=nome, descricao=descricao)
                    picole.conservantes.append(conservante)

            session.add(picole)
            sleep(0.05)
            
        # Perceba que estamos executando o commit somente no final. Desta forma os 100 dados serão enviados em um único batch para o banco
        session.commit()
    print('Picolés cadastrados com sucesso')


def popular():
    #1) Aditivos Nutritivos
    populate_aditivo_nutritivo()

    #2) Sabores
    populate_sabor()

    #3) Tipos Embalagem
    populate_tipo_embalagem()

    #4) Tipos Picole
    populate_tipo_picole()

    #5) Ingredientes
    populate_ingrediente()

    #6) Conservantes (Deixando vazio para poder verificar resultados em tabelas vazias)
    # populate_conservante()
    
    #7) Revendedores
    populate_revendedor()

    #8) Lotes
    populate_lote()

    #9) Notas Fiscais
    populate_nota_fiscal()

    #10) Picole
    #populate_picole()



if __name__ == '__main__':
    popular()
