import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    firstName: Mapped[str] = mapped_column(nullable=False)
    lastName: Mapped[str] = mapped_column(nullable=False)

    #address: Mapped["Address"] = relationship(back_populates="person")

class Favoritos(Base):
    __tablename__='favoritos'
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[str] = mapped_column(ForeignKey('usuario.id'), nullable=True)
    usuario: Mapped["Usuario"] = relationship()

    planetas_id: Mapped[int] = mapped_column(ForeignKey('planetas.id'), nullable=True)
    planetas: Mapped["Planetas"] = relationship()

    personajes_id: Mapped[int] = mapped_column(ForeignKey('personajes.id'), nullable=True)
    personajes: Mapped["Personajes"] = relationship()


class Planetas(Base):
    __tablename__ = 'planetas'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    gravity: Mapped[str] = mapped_column()
    diameter: Mapped[str] = mapped_column()
    climate: Mapped[str] = mapped_column()
    terrain: Mapped[str] = mapped_column()


class Personajes(Base):
    __tablename__='personajes'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    height: Mapped[str] = mapped_column()
    gender: Mapped[str] = mapped_column()
    birthYear: Mapped[str] = mapped_column()
    eyeColor: Mapped[str] = mapped_column()

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
