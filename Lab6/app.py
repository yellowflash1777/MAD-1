import os
from flask import Flask
from flask_restful import Api
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db

app = None
api = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv('ENV', "development") == "production":
      raise Exception("Currently no production config is setup.")
    else:
      print("Staring Local Development")
      app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api=Api(app)
    app.app_context().push()
    return app,api

app ,api= create_app()

# Import all the controllers so they are loaded
from application.controllers import *

#Import restful controllers
from application.api import *

api.add_resource(CourseAPI,'/api/course','/api/course/{course_id}')
api.add_resource(StudentAPI,'/api/student','/api/student/{student_id}')
api.add_resource(EnrollmentAPI,'/api/student/{student_id}/course','/api/student/{student_id}/course/{course_id}')


if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0',port=5000)
