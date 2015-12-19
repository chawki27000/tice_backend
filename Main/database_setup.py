import psycopg2
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# Classe ORM Administrateur
class Administrateur(Base):
    __tablename__ = 'administrateur'

    id_util = Column(Integer, primary_key=True)
    nom_util = Column(String(200), nullable=False)
    prenom_util = Column(String(200), nullable=False)
    mail_util = Column(String(150), nullable=False)
    password_util = Column(String(64), nullable=False)
    login_util = Column(String(30), nullable=False)
    grade_util = Column(String(50), nullable=False)

    # JSON response
    @property
    def serialize(self):
        return {
            'id_util': self.id_util,
            'nom_util': self.nom_util,
            'prenom_util': self.prenom_util,
            'mail_util': self.mail_util,
            'password_util': self.password_util,
            'login_util': self.login_util,
            'grade_util': self.grade_util,
        }


# Classe ORM Formateur
class Formateur(Base):
    __tablename__ = 'formateur'

    id_util = Column(Integer, primary_key=True)
    nom_util = Column(String(200), nullable=False)
    prenom_util = Column(String(200), nullable=False)
    mail_util = Column(String(150), nullable=False)
    password_util = Column(String(64), nullable=False)
    login_util = Column(String(30), nullable=False)
    grade_util = Column(String(50), nullable=False)
    spec_formation = Column(String(80), nullable=False)
    type_formation = Column(String(80), nullable=False)

    # JSON response
    @property
    def serialize(self):
        return {
            'id_util': self.id_util,
            'nom_util': self.nom_util,
            'prenom_util': self.prenom_util,
            'mail_util': self.mail_util,
            'password_util': self.password_util,
            'login_util': self.login_util,
            'grade_util': self.grade_util,
            'spec_formation': self.spec_formation,
            'type_formation': self.type_formation,
        }


# Classe ORM Categorie
class Categorie(Base):
    __tablename__ = 'categorie'

    id_categ = Column(Integer, primary_key=True)
    lib_categ = Column(String(80), nullable=False)

    id_util = Column(Integer, ForeignKey('administrateur.id_util'))
    administrateur = relationship(Administrateur)

    # JSON response
    @property
    def serialize(self):
        return {
            'id_categ': self.id_categ,
            'lib_categ': self.lib_categ,
            'id_util': self.id_util,
        }


# Classe ORM Formation
class Formation(Base):
    __tablename__ = 'formation'

    id_form = Column(Integer, primary_key=True)
    lib_form = Column(String(80), nullable=False)
    date_deb_form = Column(String(30), nullable=False)
    date_fin_form = Column(String(30), nullable=False)

    id_categ = Column(Integer, ForeignKey('categorie.id_categ'))
    categorie = relationship(Categorie)


# Classe ORM Apprenant
class Apprenant(Base):
    __tablename__ = 'apprenant'
    id_util = Column(Integer, primary_key=True)
    nom_util = Column(String(200), nullable=False)
    prenom_util = Column(String(200), nullable=False)
    mail_util = Column(String(150), nullable=False)
    password_util = Column(String(64), nullable=False)
    login_util = Column(String(30), nullable=False)
    grade_util = Column(String(50), nullable=False)
    diplome_appr = Column(String(50), nullable=False)

    id_form = Column(Integer, ForeignKey('formation.id_form'))
    formation = relationship(Formation)


# Classe ORM Regroupement
class Regroupement(Base):
    __tablename__ = 'regroupement'

    id_group = Column(Integer, primary_key=True)
    date_group = Column(String(30), nullable=False)

    id_form = Column(Integer, ForeignKey('formation.id_form'))
    formation = relationship(Formation)


##Classe ORM Cours
class Cours(Base):
    __tablename__ = 'cours'

    id_cour = Column(Integer, primary_key=True)
    lib_cour = Column(String(80), nullable=False)

    id_form = Column(Integer, ForeignKey('formation.id_form'))
    formation = relationship(Formation)


# Classe ORM Chapitre
class Chapitre(Base):
    __tablename__ = 'chapitre'

    id_chap = Column(Integer, primary_key=True)
    lib_chap = Column(String(80), nullable=False)

    id_cour = Column(Integer, ForeignKey('cours.id_cour'))
    cours = relationship(Cours)


# Classe ORM Ressource
class Ressource(Base):
    __tablename__ = 'ressource'

    id_ress = Column(Integer, primary_key=True)
    lib_ress = Column(String(80), nullable=False)
    type_ress = Column(String(50), nullable=False)

    id_chap = Column(Integer, ForeignKey('chapitre.id_chap'))
    chapitre = relationship(Chapitre)


# Classe ORM Animer
class Animer(Base):
    __tablename__ = 'animer'

    id_anim = Column(Integer, primary_key=True)
    id_util = Column(Integer, ForeignKey('formateur.id_util'))
    formateur = relationship(Formateur)

    id_form = Column(Integer, ForeignKey('formation.id_form'))
    formation = relationship(Formation)


# Classe ORM Test
class Test(Base):
    __tablename__ = 'test'

    id_test = Column(Integer, primary_key=True)

    id_util = Column(Integer, ForeignKey('apprenant.id_util'))
    apprenant = relationship(Apprenant)

    id_form = Column(Integer, ForeignKey('formation.id_form'))
    formation = relationship(Formation)

    date_test = Column(String(30), nullable=False)
    note_test = Column(Integer, nullable=False)


engine = create_engine('postgresql://chawki:linux@localhost/flask_db')
Base.metadata.create_all(engine)
