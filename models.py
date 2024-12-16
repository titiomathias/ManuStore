from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from db import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60), nullable=False)
    telefone = Column(String(20), nullable=False)
    email = Column(String(80), nullable=False)
    compras = Column(Integer, nullable=False)
    data_cadastro = Column(Date, nullable=False)


class Estoque(Base):
    __tablename__ = "estoque"

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(20), nullable=False)
    fornecedor = Column(String(60), nullable=False)
    descricao = Column(String(60), nullable=False)
    estoque_atual = Column(Integer, nullable=False)


class Entrada(Base):
    __tablename__ = "entradas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_codigo = Column(Integer, ForeignKey("estoque.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor_peca = Column(Float, nullable=False)
    frete_peca = Column(Float, nullable=False)
    custo_peca = Column(Float, nullable=False)
    custo_total = Column(Float, nullable=False)

    estoque = relationship("Estoque", backref="entradas")



class Saida(Base):
    __tablename__ = "saidas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_codigo = Column(Integer, ForeignKey("estoque.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor_venda = Column(Integer, nullable=False)
    forma_pagamento = Column(Integer, nullable=False)
    lucro_venda = Column(Integer, nullable=False)

    estoque = relationship("Estoque", backref="saidas")


class Gestao(Base):
    __tablename__ = "gestao"

    id = Column(Integer, primary_key=True, autoincrement=True)
    n_vendas = Column(Integer, nullable=False)
    n_dias = Column(Integer, nullable=False)
    faturamento = Column(Float, nullable=False)
    lucro = Column(Float, nullable=False)
    fluxo_de_caixa = Column(Float, nullable=False)
    lista_produtos_destaque = Column(LONGTEXT, nullable=False)
    metodos_pagamentos_destaque = Column(LONGTEXT, nullable=False)
    data_intervalo = Column(LONGTEXT, nullable=False)
    data_relatorio = Column(Date, nullable=False)
