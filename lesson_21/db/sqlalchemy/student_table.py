from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, UniqueConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from faker import Faker
import random

faker = Faker()

Base = declarative_base()

DATABASE_URL = "postgresql+psycopg://kate:kate@localhost:5432/mydb"

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

    registrations = relationship("Registration", back_populates="student", cascade="all, delete-orphan")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)

    registrations = relationship("Registration", back_populates="course_obj", cascade="all, delete-orphan")


class Registration(Base):
    __tablename__ = "registrations"

    __table_args__ = (UniqueConstraint("student_id", "course_id"),)

    id = Column(Integer, primary_key=True)
    
    student_name = Column(String)
    student_id = Column(Integer,ForeignKey("students.id"), nullable=False)
    course = Column(String)
    course_id = Column(Integer,ForeignKey("courses.id"), nullable=False)

    student = relationship("Student",back_populates="registrations")
    course_obj = relationship( "Course", back_populates="registrations" )

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


session = Session()



def create_data():
    course_titles = ["Python", "SQL", "Web Design", "Data Science", "Algorithms"]

    courses = []
    for title in course_titles:
        courses.append(Course(title=title))

    students = []
    for _ in range(20):
        students.append(Student(name=faker.name(), age=random.randint(18, 60)))

    session.add_all(courses)
    session.add_all(students)
    session.commit()

    for student in students:
        total = random.randint(1, 3)
        chosen_courses = random.sample(courses, total)

        for course in chosen_courses:
            session.add(
                Registration(
                    student_name=student.name,
                    student_id=student.id,
                    course=course.title,
                    course_id = course.id
                )
            )

    session.commit()


def add_student_to_course(name, age, course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if course is None:
        return None

    student = Student(name=name, age=age)
    session.add(student)
    session.commit()

    session.add(
        Registration(
            student_name=student.name,
            student_id=student.id,
            course=course.title,
            course_id=course.id
        )
    )
    session.commit()

    return student


def get_students_by_course(course_title):
    registrations = (
        session.query(Registration).filter_by(course=course_title).all())

    students = []

    for reg in registrations:
        student = session.get(Student, reg.student_id)
        if student:
            students.append(student)

    return students


def get_courses_by_student(student_id):
    registrations = (session.query(Registration).filter_by(student_id=student_id).all())

    courses = []

    for reg in registrations:
        courses.append(reg.course)

    return courses


def update_student(student_id, new_name=None, new_age=None):
    student = session.get(Student, student_id)
    if student is None:
        return

    if new_name is not None:
        student.name = new_name
    if new_age is not None:
        student.age = new_age

    session.commit()

def update_course(course_id, new_title):
    course = session.get(Course, course_id)
    if course is None:
        return

    course.title = new_title
    session.commit()


def delete_student(student_id):
    student = session.get(Student, student_id)
    if student is None:
        return

    session.delete(student)
    session.commit()



create_data()
session.close()