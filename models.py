from sqlmodel import Field, Relationship, SQLModel

# StudentCourseLink
class StudentCourseLink(SQLModel, table=True):
    student_id: int = Field(foreign_key="student.id", primary_key=True)
    course_id: int | None = Field(foreign_key="course.id", primary_key=True)

# student
class Student(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str
    courses: list["Course"] = Relationship(back_populates="students", link_model=StudentCourseLink)

# instructor
class Instructor(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str
    courses: list["Course"] = Relationship(back_populates="instructor")

#course
class Course(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str
    semester: str

    students: list[Student] = Relationship(back_populates="courses", link_model=StudentCourseLink)

    instructor_id: int = Field(foreign_key="instructor.id")
    instructor: Instructor = Relationship(back_populates="courses")