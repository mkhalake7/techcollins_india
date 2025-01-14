
from models import db

from flask import render_template,url_for
from models import* 
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app

admin = Admin(app,name='Data_Management', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Excel_d, db.session))
