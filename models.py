from sqlalchemy import create_engine, Column, String, Date
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine("postgresql+psycopg2://professor:professor@db-isac-rds1.ccjja7bteogf.us-east-1.rds.amazonaws.com:5432/db_isac")
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Usuarios(Base):
    __tablename__ = "usuarios"
    cpf = Column(String(14), primary_key=True)
    nome = Column(String(50), index=True)
    data_nascimento = Column(Date)

    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __repr__(self):
        return "Usuario: {}".format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
