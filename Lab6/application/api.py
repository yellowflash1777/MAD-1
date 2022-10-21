from email import message
from xml.dom import ValidationErr
from flask_restful import Resource
from flask_restful import marshal_with,fields,reqparse
from application.database import db
from application.models import Course, Enrollments, Student
from application.validation import NotFoundError,ValidationError,BadError

#fields
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

#requestParser()
create_course_parser= reqparse.RequestParser()
create_course_parser.add_argument('course_name')
create_course_parser.add_argument('course_code')
create_course_parser.add_argument('course_description')

create_student_parser= reqparse.RequestParser()
create_student_parser.add_argument('first_name')
create_student_parser.add_argument('last_name')
create_student_parser.add_argument('roll_number')

create_enrollment_parser= reqparse.RequestParser()
create_enrollment_parser.add_argument('course_id')

class CourseAPI(Resource):

    @marshal_with(course_fields)
    def get(self,course_id):
        course=db.session.query(Course).filter(Course.course_id==course_id).first()        
        if course:
            return course
        else:
            raise NotFoundError(status_code=404)

    @marshal_with(course_fields)
    def put(self,course_id):
        
        args=create_course_parser.parse_args()
        course_name=args.get('course_name',None)
        course_code=args.get('course_code',None)
        course_description=args.get('course_description',None)
        if course_code is None:
            raise ValidationError(status_code=400,error_code="COURSE002",error_message="Course Code is required")
        if course_name is None:
            raise ValidationError(status_code=400,error_code="COURSE001",error_message="Course Name is required")
        course=db.session.query(Course).filter(Course.course_code==course_code).first()
        if course:
            raise BadError(status_code=409, message='course_code already exist')
        course=db.session.query(Course).filter(Course.course_id==course_id).first()        
        if course:
            course.course_name=course_name
            course.course_code=course_code
            course.course_description=course_description
            db.session.commit()
            return course
        else:
            raise NotFoundError(status_code=404)
        

    def delete(self,course_id):
        pass
    
    @marshal_with(course_fields)
    def post(self):
        args=create_course_parser.parse_args()
        course_name=args.get('course_name',None)
        course_code=args.get('course_code',None)
        course_description=args.get('course_description',None)
        if course_code is None:
            raise ValidationError(status_code=400,error_code="COURSE002",error_message="Course Code is required")
        if course_name is None:
            raise ValidationError(status_code=400,error_code="COURSE001",error_message="Course Name is required")

        course=db.session.query(Course).filter(Course.course_code==course_code).first()
        if course:
            raise BadError(status_code=409, message='course_code already exist')
        course=Course(course_name=course_name,course_code=course_code,course_description=course_description)
        db.session.add(course)
        db.session.commit()
        return course


class StudentAPI(Resource):

    @marshal_with(student_feilds)
    def get(self,student_id):
        student=db.session.query(Student).filter(Student.student_id==student_id).first()        
        if student:
            return student
        else:
            raise NotFoundError(status_code=404)
    @marshal_with(student_feilds)
    def put(self,student_id):
        args=create_student_parser.parse_args()
        first_name=args.get('first_name',None)
        last_name=args.get('last_name',None)
        roll_number=args.get('roll_number',None)
        if first_name is None:
            raise ValidationError(status_code=400,error_code="STUDENT002",error_message="First Name is required")
        if roll_number is None:
            raise ValidationError(status_code=400,error_code="STUDENT001",error_message="Roll No is required")

        student=db.session.query(Student).filter(Student.roll_number==roll_number).first()
        if student:
            raise BadError(status_code=409, message='Student already exist')
        student=db.session.query(Student).filter(Student.student_id==student_id).first()
        if student:
            student.first_name=first_name
            student.last_name=last_name
            student.roll_number=roll_number
            db.session.commit()
            return student
        else:
            raise NotFoundError(status_code=404)


    def delete(self,student_id):
        pass

    @marshal_with(student_feilds)
    def post(self):
        args=create_student_parser.parse_args()
        first_name=args.get('first_name',None)
        last_name=args.get('last_name',None)
        roll_number=args.get('roll_number',None)
        if first_name is None:
            raise ValidationError(status_code=400,error_code="STUDENT002",error_message="First Name is required")
        if roll_number is None:
            raise ValidationError(status_code=400,error_code="STUDENT001",error_message="Roll No is required")

        student=db.session.query(Student).filter(Student.roll_number==roll_number).first()
        if student:
            raise BadError(status_code=409, message='Student already exist')
        student=Student(first_name=first_name,last_name=last_name,roll_number=roll_number)
        db.session.add(student)
        db.session.commit()
        return student

class EnrollmentAPI(Resource):

    @marshal_with(enrollment_feilds)
    def get(self,student_id):
        enrollments=db.session.query(Enrollments).filter(Enrollments.student_id==student_id).all()        
        if enrollments:
            return enrollments
        else:
            raise NotFoundError(status_code=404)

    @marshal_with(enrollment_feilds)
    def post(self,student_id):
        args=create_enrollment_parser.parse_args()
        course_id=args.get("course_id",None)
        student=db.session.query(Student).filter(Student.student_id==student_id).first()
        if student:
            pass
        else:
            raise ValidationError(status_code=400,error_code="ENROLLMENT002",error_message="Student does not exist")
        
        print('*************************************************')
        print(course_id)
        print('*************************************************')
        if course_id is None:
            raise ValidationError(status_code=400,error_code="ENROLLMENT003",error_message="Course id is required")
        course=db.session.query(Course).filter(Course.course_id==course_id).first()
        if course:
            pass
        else:
            raise ValidationError(status_code=400,error_code="ENROLLMENT001",error_message="Course does not exist")
        enrollments=Enrollments(student_id=student_id,course_id=course_id)
        db.session.add(enrollments)
        db.session.commit()
        return enrollments



    def delete(self,student_id,course_id):
        pass

#raise ValidationError(status_code=400,error_code="ENROLLMENT001",error_message="Course does not exist")