from db import engine, DBModel

def main():
    from models import (AditivoNutritivo, Sabor, 
                        TipoEmbalagem, TipoPicole, 
                        Picole, Ingrediente,
                        Conservante, Lote, Revendedor,
                        NotaFiscal,
                        aditivos_nutritivos_picole,
                        ingredientes_picoles,
                        conservantes_picoles,
                        lotes_nota_fiscal)

    with engine.connect() as conn:
        DBModel.metadata.drop_all(conn)
        DBModel.metadata.create_all(conn)

if __name__ == '__main__':
    main()