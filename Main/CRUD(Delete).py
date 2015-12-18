from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Administrateur, Formateur, Categorie
from database_setup import Formation, Apprenant, Regroupement, Cours
from database_setup import Chapitre, Ressource, Animer, Test

engine = create_engine('sqlite:///tice.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Delete (Administrateur) by (id_util)
MyAdmin = session.query(Administrateur).filter_by(id_util=1).one()
session.delete(MyAdmin)
session.commit()

# Delte (Formateur) by (id_util)
MyFormateur = session.query(Formateur).filter_by(id_util=1).one()

