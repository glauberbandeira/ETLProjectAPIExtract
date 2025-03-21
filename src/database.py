from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, String, Integer, DateTime
from datetime import datetime

# Cria a classe Base do SQLAlchemy (na versão 2.x)
Base = declarative_base()

class BitcoinPrice(Base):
    """Define a tabela no banco de dados."""
    __tablename__ = "bitcoin_prices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    crypto = Column(String(50), nullable=False)  # até 50 caracteres
    currency = Column(String(10), nullable=False)        # até 10 caracteres
    timestamp = Column(DateTime, default=datetime.now)