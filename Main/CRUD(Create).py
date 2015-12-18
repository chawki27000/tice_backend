from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Administrateur, Formateur, Categorie
from database_setup import Formation, Apprenant, Regroupement, Cours
from database_setup import Chapitre, Ressource, Animer, Test

engine = create_engine('sqlite:///tice.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# New entry in table
# NewEntry = ClassName(property = "value")
# session.add(newEntry)
# session.commit()
myAdmin = Administrateur(nom_util="benchehida", prenom_util="chawki",
                         mail_util="chawki27000@hotmail.com", password_util="chawki27000",
                         login_util="chawki27000", grade_util="Chef de departement")
session.add(myAdmin)
session.commit()

# New entry in table
myFormateur = Formateur(nom_util="djebbour", prenom_util="sofiane",
                        mail_util="djebbour@gmail.com", password_util="djsof",
                        login_util="djsof", grade_util="MCA",
                        spec_formation="Compilation", type_formation="acamedique")
session.add(myFormateur)
session.commit()

# New entry in table
myCategorie = Categorie(lib_categ="UEF", id_util=1)
session.add(myCategorie)
session.commit()

# New entry in table
myFormation = Formation(lib_form="Compilation", date_deb_form="01/01/2009",
                        date_fin_form="01/01/2010", id_categ=1)
session.add(myFormation)
session.commit()

# New entry in table
myApprenant = Apprenant(nom_util="chaa", prenom_util="mostapha",
                        mail_util="mostapha@hotmail.fr", password_util="azerty",
                        login_util="azerty27", grade_util="licence",
                        diplome_appr="master", id_form=1)
session.add(myApprenant)
session.commit()

# New entry in table
myRegroupement = Regroupement(date_group="01/02/2011", id_form=1)
session.add(myRegroupement)
session.commit()

# New entry in table
myCours = Cours(lib_cour="Analyse LR", id_form=1)
session.add(myCours)
session.commit()

# New entry in table
myChapitre = Chapitre(lib_chap="Analyse Ascendante", id_cour=1)
session.add(myChapitre)
session.commit()

# New entry in table
myRessource = Ressource(lib_ress="No idea", type_ress="numerique",
                        id_chap=1)
session.add(myRessource)
session.commit()

# New entry in table
myAnimer = Animer(id_util=1, id_form=1)
session.add(myAnimer)
session.commit()

# New entry in table
myTest = Test(id_util=1, id_form=1, date_test="01/01/2016",
              note_test=15)
session.add(myTest)
session.commit()
