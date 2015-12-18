from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Administrateur, Formateur, Categorie
from database_setup import Formation, Apprenant, Regroupement, Cours
from database_setup import Chapitre, Ressource, Animer, Test

engine = create_engine('sqlite:///tice.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

print 'Administrateur'
items = session.query(Administrateur).all()

for item in items:
    print item.id_util
    print item.nom_util

print 'Formateur'
items = session.query(Formateur).all()

for item in items:
    print item.id_util
    print item.nom_util
