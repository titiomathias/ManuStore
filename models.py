from sqlalchemy import Column, Integer, String
from .db import Base

class Estoque(Base):
    __tablename__ = "estoque"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    quantidade = Column(Integer)
