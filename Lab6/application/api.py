from flask_restful import Resource
from flask_restful import marshal_with,fields
from application.database import db
from application.models import Course, Enrollments, Student
from application.validation import NotFoundError

course_fields={
    "course_id":fields.Integer,
    "course_name":fields.String,
    "course_code":fields.String,
    "course_description":fields.String, 
}

student_feilds={
    "student_id":fields.Integer,
    "first_name":fields.String,
    "last_name":fields.String,
    "roll_number":fields.String,
}
enrollment_feilds={
    "enrollment_id":fields.Integer,
    "student_id":fields.Integer,
    "course_id":fields.Integer
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

    @marshal_with(student_feilds)
    def get(self,student_id):
        student=db.session.query(Student).filter(Student.student_id==student_id).first()        
        if student:
            return student
        else:
            raise NotFoundError(status_code=404)

    def put(self,student_id):
        pass

    def delete(self,student_id):
        pass

    def post(self):
        pass

class EnrollmentAPI(Resource):

    @marshal_with(enrollment_feilds)
    def get(self,student_id):
        enrollments=db.session.query(Enrollments).filter(Enrollments.student_id==student_id).all()        
        if enrollments:
            return enrollments
        else:
            raise NotFoundError(status_code=404)

    def post(self,student_id):
        pass

    def delete(self,student_id,course_id):
        pass

