from flask_restful import Resource
from flask_restful import marshal_with,fields
from application.database import db
from application.models import Course

course_fields={
    "course_id":fields.Integer,
    "course_name":fields.String,
    "course_code":fields.String,
    "course_description":fields.String, 
}

class CourseAPI(Resource):

    @marshal_with(course_fields)
    def get(self,course_id):
        course=db.session.query(Course).filter(Course.course_id==course_id).first()
        if course:
            return course
        else:
            raise NotFoundError(status_code=404)

    def put(self,course_id):
        pass

    def delete(self,course_id):
        pass

    def post(self):
        pass


class StudentAPI(Resource):
    def get(self,student_id):
        pass

    def put(self,student_id):
        pass

    def delete(self,student_id):
        pass

    def post(self):
        pass

class EnrollmentAPI(Resource):
    def get(self,student_id):
        pass

    def post(self,student_id):
        pass

    def delete(self,student_id,course_id):
        pass

