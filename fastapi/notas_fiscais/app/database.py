import oracledb
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import config

pool = None
engine = None
SessionLocal = None


def init_pool():
    """Inicializa o pool de conexões Oracle e integra com SQLAlchemy."""
    global pool, engine, SessionLocal

    if not pool:
        pool = oracledb.create_pool(
            user=config.ORACLE_USER,
            password=config.ORACLE_PASSWORD,
            dsn=config.ORACLE_DSN,
            min=1,
            max=5,
            increment=1
        )
        print("Pool Oracle criado com sucesso")

        # Cria engine SQLAlchemy usando o pool existente
        engine = create_engine(
            "oracle+oracledb://",
            creator=lambda: pool.acquire(),  # usa o pool existente
            echo=False,
            future=True
        )

        SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )

# Declarative Base
Base = declarative_base()

def get_db():
    """Dependência do FastAPI para obter sessão do banco."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
