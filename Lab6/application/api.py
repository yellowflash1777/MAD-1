from flask_restful import Resource
from numpy import delete

class CourseAPI(Resource):
    def get(self,course_id):
        pass

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

