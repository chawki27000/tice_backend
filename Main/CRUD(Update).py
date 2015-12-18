from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Administrateur, Formateur, Categorie
from database_setup import Formation, Apprenant, Regroupement, Cours
from database_setup import Chapitre, Ressource, Animer, Test

engine = create_engine('sqlite:///tice.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

MyAdmin = session.query(Administrateur).filter_by(id_util=1).one()

MyAdmin.nom_util = "abdallah"
MyAdmin.prenom_util = "ismail"

# update the database
session.add(MyAdmin)
session.commit()
