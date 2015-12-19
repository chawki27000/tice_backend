from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Administrateur, Formateur, Categorie
from database_setup import Formation, Apprenant, Regroupement, Cours
from database_setup import Chapitre, Ressource, Animer, Test

app = Flask(__name__)

engine = create_engine('postgresql://chawki:linux@localhost/flask_db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/v1')
def index():
    return "Index TICE API V1"


# CRUD Create : Administrateur
@app.route('/v1/administrateur/new', methods=['GET', 'POST'])
def newAdministrateurItem():
    if request.method == 'POST':
        newItem = Administrateur(nom_util=request.form['nom_util'], prenom_util=request.form['prenom_util'],
                                 mail_util=request.form['mail_util'], password_util=request.form['password_util'],
                                 login_util=request.form['login_util'], grade_util=request.form['grade_util'])

        session.add(newItem)
        failed = False
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            session.flush()  # for resetting non-commited .add()
            failed = True

        if failed == False:
            return jsonify({'state': '1', 'error': 'no error'})
        else:
            return jsonify({'state': '0', 'error': 'failed operation'})


# CRUD Delete : Administrateur
@app.route('/v1/administrateur/del/<int:ident>')
def delAdministrateurItem(ident):
    myItem = session.query(Administrateur).filter_by(id_util=ident).one()
    session.delete(myItem)
    session.commit()


# Making an API Endpoint (GET Request)
@app.route('/v1/administrateur/all/json')
def getAdminJson():
    items = session.query(Administrateur).all()

    return jsonify(Administrateur=[i.serialize for i in items])


######################################################################
# CRUD Create : Formateur
@app.route('/v1/formateur/new', methods=['GET', 'POST'])
def newFormateurItem():
    if request.method == 'POST':
        newItem = Formateur(nom_util=request.form['nom_util'], prenom_util=request.form['prenom_util'],
                            mail_util=request.form['mail_util'], password_util=request.form['password_util'],
                            login_util=request.form['login_util'], grade_util=request.form['grade_util'],
                            spec_formation=request.form['spec_formation'],
                            type_formation=request.form['type_formation'])

        session.add(newItem)
        failed = False
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            session.flush()  # for resetting non-commited .add()
            failed = True

        if failed == False:
            return jsonify({'state': '1', 'error': 'no error'})
        else:
            return jsonify({'state': '0', 'error': 'failed operation'})


# CRUD Delete : Formateur
@app.route('/v1/formateur/del/<int:ident>')
def delFormateurItem(ident):
    myItem = session.query(Formateur).filter_by(id_util=ident).one()
    session.delete(myItem)
    session.commit()


# Making an API Endpoint (GET Request)
@app.route('/v1/formateur/all/json')
def getformateurJson():
    items = session.query(Formateur).all()
    return jsonify(Formateur=[i.serialize for i in items])


######################################################################
# CRUD Create : Categorie
@app.route('/v1/categorie/new', methods=['GET', 'POST'])
def newCategorieItem():
    if request.method == 'POST':
        newItem = Categorie(lib_categ=request.form['lib_categ'], id_util=request.form['id_util'])

        session.add(newItem)
        failed = False
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            session.flush()  # for resetting non-commited .add()
            failed = True

        if failed == False:
            return jsonify({'state': '1', 'error': 'no error'})
        else:
            return jsonify({'state': '0', 'error': 'failed operation'})


# CRUD Delete : Categorie
@app.route('/v1/categorie/del/<int:ident>')
def delCategorieItem(ident):
    myItem = session.query(Categorie).filter_by(id_categ=ident).one()
    session.delete(myItem)
    session.commit()


# Making an API Endpoint (GET Request)
@app.route('/v1/categorie/all/json')
def getCategorieJson():
    items = session.query(Categorie).all()
    return jsonify(categorie=[i.serialize for i in items])


######################################################################
# CRUD Create : Formation
@app.route('/v1/formation/new', methods=['GET', 'POST'])
def newFormationItem():
    if request.method == 'POST':
        newItem = Formation(lib_form=request.form['lib_form'], date_deb_form=request.form['date_deb_form'],
                            date_fin_form=request.form['date_fin_form'], id_categ=request.form['id_categ'])

        session.add(newItem)
        failed = False
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            session.flush()  # for resetting non-commited .add()
            failed = True

        if failed == False:
            return jsonify({'state': '1', 'error': 'no error'})
        else:
            return jsonify({'state': '0', 'error': 'failed operation'})


# CRUD Delete : Formation
@app.route('/v1/formation/del/<int:ident>')
def delFormationItem(ident):
    myItem = session.query(Formation).filter_by(id_form=ident).one()
    session.delete(myItem)
    session.commit()

# Making an API Endpoint (GET Request)
@app.route('/v1/formation/all/json')
def getFormationJson():
    items = session.query(Formation).all()
    return jsonify(formation=[i.serialize for i in items])


######################################################################
# CRUD Create : Apprenant
@app.route('/v1/apprenant/new', methods=['GET', 'POST'])
def newApprenantItem():
    if request.method == 'POST':
        newItem = Apprenant(nom_util=request.form['nom_util'], prenom_util=request.form['prenom_util'],
                            mail_util=request.form['mail_util'], password_util=request.form['password_util'],
                            login_util=request.form['login_util'], grade_util=request.form['grade_util'],
                            diplome_appr=request.form['diplome_appr'], id_form=request.form['id_form'])

        session.add(newItem)

        failed = False
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            session.flush()  # for resetting non-commited .add()
            failed = True

        if failed == False:
            return jsonify({'state': '1', 'error': 'no error'})
        else:
            return jsonify({'state': '0', 'error': 'failed operation'})


# CRUD Delete : Apprenant
@app.route('/v1/apprenant/del/<int:ident>')
def delApprenantItem(ident):
    myItem = session.query(Apprenant).filter_by(id_util=ident).one()
    session.delete(myItem)
    session.commit()

# Making an API Endpoint (GET Request)
@app.route('/v1/apprenant/all/json')
def getApprenantJson():
    items = session.query(Apprenant).all()
    return jsonify(apprenant=[i.serialize for i in items])


######################################################################
# CRUD Create : Regroupement
@app.route('/v1/regroupement/new', methods=['GET', 'POST'])
def newRegroupementItem():
    if request.method == 'POST':
        newItem = Regroupement(date_group=request.form['date_group'], id_form=request.form['id_form'])

        session.add(newItem)
        failed = False
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            session.flush()  # for resetting non-commited .add()
            failed = True

        if failed == False:
            return jsonify({'state': '1', 'error': 'no error'})
        else:
            return jsonify({'state': '0', 'error': 'failed operation'})


# CRUD Delete : Regroupement
@app.route('/v1/regroupement/del/<int:ident>')
def delRegroupementItem(ident):
    myItem = session.query(Regroupement).filter_by(id_group=ident).one()
    session.delete(myItem)
    session.commit()

# Making an API Endpoint (GET Request)
@app.route('/v1/regroupement/all/json')
def getRegroupementJson():
    items = session.query(Regroupement).all()
    return jsonify(regroupement=[i.serialize for i in items])


######################################################################
# CRUD Create : Cours
@app.route('/v1/cours/new', methods=['GET', 'POST'])
def newCoursItem():
    if request.method == 'POST':
        newItem = Cours(lib_cour=request.form['lib_cour'], id_form=request.form['id_form'])

        session.add(newItem)
        failed = False
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            session.flush()  # for resetting non-commited .add()
            failed = True

        if failed == False:
            return jsonify({'state': '1', 'error': 'no error'})
        else:
            return jsonify({'state': '0', 'error': 'failed operation'})


# CRUD Delete : Cours
@app.route('/v1/cours/del/<int:ident>')
def delCoursItem(ident):
    myItem = session.query(Cours).filter_by(id_cour=ident).one()
    session.delete(myItem)
    session.commit()

# Making an API Endpoint (GET Request)
@app.route('/v1/cours/all/json')
def getCoursJson():
    items = session.query(Cours).all()
    return jsonify(cours=[i.serialize for i in items])

######################################################################
# CRUD Create : Chapitre
@app.route('/v1/chapitre/new', methods=['GET', 'POST'])
def newChapitreItem():
    if request.method == 'POST':
        newItem = Chapitre(lib_chap=request.form['lib_chap'], id_cour=request.form['id_cour'])

        session.add(newItem)
        failed = False
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            session.flush()  # for resetting non-commited .add()
            failed = True

        if failed == False:
            return jsonify({'state': '1', 'error': 'no error'})
        else:
            return jsonify({'state': '0', 'error': 'failed operation'})


# CRUD Delete : Chapitre
@app.route('/v1/chapitre/del/<int:ident>')
def delChapitreItem(ident):
    myItem = session.query(Chapitre).filter_by(id_chap=ident).one()
    session.delete(myItem)
    session.commit()

# Making an API Endpoint (GET Request)
@app.route('/v1/chapitre/all/json')
def getChapitreJson():
    items = session.query(Chapitre).all()
    return jsonify(chapitre=[i.serialize for i in items])

######################################################################
# CRUD Create : Ressource
@app.route('/v1/ressource/new', methods=['GET', 'POST'])
def newRessourceItem():
    if request.method == 'POST':
        newItem = Ressource(lib_ress=request.form['lib_ress'], type_ress=request.form['type_ress'],
                            id_chap=request.form['id_chap'])

        session.add(newItem)
        failed = False
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            session.flush()  # for resetting non-commited .add()
            failed = True

        if failed == False:
            return jsonify({'state': '1', 'error': 'no error'})
        else:
            return jsonify({'state': '0', 'error': 'failed operation'})


# CRUD Delete : Ressource
@app.route('/v1/ressource/del/<int:ident>')
def delRessourceItem(ident):
    myItem = session.query(Ressource).filter_by(id_ress=ident).one()
    session.delete(myItem)
    session.commit()

# Making an API Endpoint (GET Request)
@app.route('/v1/ressource/all/json')
def getRessourceJson():
    items = session.query(Ressource).all()
    return jsonify(ressource=[i.serialize for i in items])

######################################################################
# CRUD Create : Animer
@app.route('/v1/animer/new', methods=['GET', 'POST'])
def newAnimerItem():
    if request.method == 'POST':
        newItem = Animer(id_util=request.form['id_util'], id_form=request.form['id_form'])

        session.add(newItem)
        failed = False
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            session.flush()  # for resetting non-commited .add()
            failed = True

        if failed == False:
            return jsonify({'state': '1', 'error': 'no error'})
        else:
            return jsonify({'state': '0', 'error': 'failed operation'})


# CRUD Delete : Animer
@app.route('/v1/animer/del/<int:ident>')
def delAnimerItem(ident):
    myItem = session.query(Animer).filter_by(id_anim=ident).one()
    session.delete(myItem)
    session.commit()

# Making an API Endpoint (GET Request)
@app.route('/v1/animer/all/json')
def getAnimerJson():
    items = session.query(Animer).all()
    return jsonify(animer=[i.serialize for i in items])

######################################################################
# CRUD Create : Test
@app.route('/v1/test/new', methods=['GET', 'POST'])
def newTestItem():
    if request.method == 'POST':
        newItem = Test(id_util=request.form['id_util'], id_form=request.form['id_form'],
                       date_test=request.form['date_test'], note_test=request.form['note_test'])

        session.add(newItem)
        failed = False
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            session.flush()  # for resetting non-commited .add()
            failed = True

        if failed == False:
            return jsonify({'state': '1', 'error': 'no error'})
        else:
            return jsonify({'state': '0', 'error': 'failed operation'})


# CRUD Delete : Test
@app.route('/v1/test/del/<int:ident>')
def delTestItem(ident):
    myItem = session.query(Test).filter_by(id_test=ident).one()
    session.delete(myItem)
    session.commit()

# Making an API Endpoint (GET Request)
@app.route('/v1/test/all/json')
def getTestJson():
    items = session.query(Test).all()
    return jsonify(test=[i.serialize for i in items])

######################################################################

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': '404'}), 404


@app.errorhandler(500)
def page_not_found(e):
    return jsonify({'error': '500'}), 500

@app.errorhandler(405)
def page_not_found(e):
    return jsonify({'error': '405'}), 405


#######################################################################
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
