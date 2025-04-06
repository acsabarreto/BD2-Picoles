from sqlalchemy import Table, Column, String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from db import DBModel

aditivos_nutritivos_picole = Table(
    'aditivos_nutritivos_picole',
    DBModel.metadata,
    Column('id_aditivo_nutritivo', ForeignKey('aditivos_nutritivos.id')),
    Column('id_picole', ForeignKey('picoles.id'))
)

ingredientes_picoles = Table(
    'ingredientes_picoles',
    DBModel.metadata,
    Column('id_ingrediente', ForeignKey('ingredientes.id')),
    Column('id_picole', ForeignKey('picoles.id'))
)

conservantes_picoles = Table(
    'conservantes_picoles',
    DBModel.metadata,
    Column('id_conservante', ForeignKey('conservantes.id')),
    Column('id_picole', ForeignKey('picoles.id'))
)

lotes_nota_fiscal = Table(
    'lotes_nota_fiscal',
    DBModel.metadata,
    Column('id_lote', ForeignKey('lotes.id')),
    Column('id_nota_fiscal', ForeignKey('notas_fiscais.id'))
)

class AditivoNutritivo(DBModel):
    __tablename__ = 'aditivos_nutritivos'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome:Mapped[str] = mapped_column(String(45), nullable=False)
    formula_quimica:Mapped[str] = mapped_column(String(45), nullable= False)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.nome = kwargs['nome']
        self.formula_quimica = kwargs['formula_quimica']

class Sabor(DBModel):

    __tablename__ = 'sabores'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome:Mapped[str] = mapped_column(String(45), nullable=False)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.nome = kwargs['nome']

class TipoEmbalagem(DBModel):

    __tablename__ = 'tipos_embalagem'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome:Mapped[str] = mapped_column(String(45), nullable=False)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.nome = kwargs['nome']

class TipoPicole(DBModel):

    __tablename__ = 'tipos_picole'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome:Mapped[str] = mapped_column(String(45), nullable=False)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.nome = kwargs['nome']

class Picole(DBModel):

    __tablename__ = 'picoles'

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    preco:Mapped[float] = mapped_column(Numeric(4,2),nullable=False)

    id_sabor:Mapped[int] = mapped_column(ForeignKey('sabores.id'))
    id_tipo_embalagem:Mapped[int] = mapped_column(ForeignKey('tipos_embalagem.id'))
    id_tipo_picole:Mapped[int] = mapped_column(ForeignKey('tipos_picole.id'))

class Ingrediente(DBModel):

    __tablename__ = 'ingredientes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome:Mapped[str] = mapped_column(String(45), nullable=False)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.nome = kwargs['nome']

class Conservante(DBModel):

    __tablename__ = 'conservantes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome:Mapped[str] = mapped_column(String(45), nullable=False)
    descricao:Mapped[str] = mapped_column(String(45), nullable=False)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.nome = kwargs['nome']
        self.descricao = kwargs['descricao']

class Lote(DBModel):

    __tablename__ = 'lotes'

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    quantidade:Mapped[int]
    id_tipo_picole:Mapped[int] = mapped_column(ForeignKey('tipos_picole.id'))
    

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.quantidade = kwargs['quantidade']
        self.id_picole = kwargs['id_picole']

class Revendedor(DBModel):

    __tablename__ = 'revendedores'

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cnpj:Mapped[str] = mapped_column(String(45), nullable=False)
    razao_social:Mapped[str] = mapped_column(String(100), nullable=False)
    contato:Mapped[str] = mapped_column(String(100), nullable=False)


    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.cnpj = kwargs['cnpj']
        self.razao_social = kwargs['razao_social']
        self.contato = kwargs['contato']

class NotaFiscal(DBModel):

    __tablename__ = 'notas_fiscais'

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data:Mapped[date] = mapped_column(nullable=False, default=date.today)
    valor:Mapped[float] = mapped_column(Numeric(8,2), nullable=False)
    numero_serie:Mapped[str] = mapped_column(String(45), nullable=False)
    descricao:Mapped[str] = mapped_column(String(200), nullable=False)
    id_revendedor:Mapped[int] = mapped_column(ForeignKey('revendedores.id'))

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.data = kwargs['data']
        self.valor = kwargs['valor']
        self.numero_serie = kwargs['numero_serie']
        self.descricao = kwargs['descricao']
        self.id_revendedor = kwargs['id_revendendor']