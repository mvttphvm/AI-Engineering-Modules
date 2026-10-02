from sqlalchemy import (
    create_engine, String, Integer, ForeignKey, Table, Column, select, func
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from typing import List

engine = create_engine("sqlite:///:memory:", echo=False)


class Base(DeclarativeBase):
    pass


# This is the middle table that connects students and courses
student_courses = Table(
    "enrollments",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True),
)


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    # One department can have multiple teachers
    teachers: Mapped[List["Teacher"]] = relationship(
        "Teacher",
        back_populates="department"
    )

    courses: Mapped[List["Course"]] = relationship(
        "Course",
        back_populates="department"
    )

    def __repr__(self) -> str:
        return f"<Department (name = '{self.name}')>"


class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    department_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("departments.id")
    )

    department: Mapped["Department"] = relationship(
        "Department",
        back_populates="teachers"
    )

    courses: Mapped[list["Course"]] = relationship(
        "Course",
        back_populates="teacher"
    )

    def __repr__(self) -> str:
        return f"<Teacher (name = '{self.name}')>"


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    credits: Mapped[int] = mapped_column(Integer, default=3)
    department_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("departments.id")
    )
    teacher_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("teachers.id"),
        nullable=True
    )

    department: Mapped["Department"] = relationship(
        "Department",
        back_populates="courses"
    )

    teacher: Mapped["Teacher"] = relationship(
        "Teacher",
        back_populates="courses"
    )

    # This connects Course and Student through the enrollment table
    students: Mapped[list["Student"]] = relationship(
        "Student",
        secondary=student_courses,
        back_populates="courses"
    )

    def __repr__(self) -> str:
        return f"<Course (title = '{self.title}')>"


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False
    )
    year: Mapped[int] = mapped_column(Integer, nullable=False)

    # Same many-to-many relationship from the Student side
    courses: Mapped[list["Course"]] = relationship(
        "Course",
        secondary=student_courses,
        back_populates="students"
    )

    def __repr__(self) -> str:
        return (
            f"<Student (name = '{self.name}', "
            f"email = '{self.email}', year = {self.year})>"
        )


# ── Test block ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    Base.metadata.create_all(engine)

    with Session(engine) as session:

        # ── Seed departments ──────────────────────────────────────────────────
        cs_dept = Department(name="Computer Science")
        math_dept = Department(name="Mathematics")

        session.add_all([cs_dept, math_dept])
        session.flush()

        # ── Seed teachers ─────────────────────────────────────────────────────
        prof_kim = Teacher(
            name="Prof. Kim",
            department_id=cs_dept.id
        )

        prof_lee = Teacher(
            name="Prof. Lee",
            department_id=cs_dept.id
        )

        prof_chen = Teacher(
            name="Prof. Chen",
            department_id=math_dept.id
        )

        prof_patel = Teacher(
            name="Prof. Patel",
            department_id=math_dept.id
        )

        session.add_all([
            prof_kim,
            prof_lee,
            prof_chen,
            prof_patel
        ])
        session.flush()

        # ── Seed courses ─────────────────────────────────────────────────────
        db101 = Course(
            title="Databases 101",
            credits=3,
            department_id=cs_dept.id,
            teacher_id=prof_kim.id
        )

        py201 = Course(
            title="Python Advanced",
            credits=3,
            department_id=cs_dept.id,
            teacher_id=prof_lee.id
        )

        ai301 = Course(
            title="Artificial Intelligence",
            credits=4,
            department_id=cs_dept.id,
            teacher_id=prof_kim.id
        )

        calc1 = Course(
            title="Calculus I",
            credits=4,
            department_id=math_dept.id,
            teacher_id=prof_chen.id
        )

        stats = Course(
            title="Statistics",
            credits=3,
            department_id=math_dept.id,
            teacher_id=prof_patel.id
        )

        session.add_all([
            db101,
            py201,
            ai301,
            calc1,
            stats
        ])
        session.flush()

        # ── Seed students ────────────────────────────────────────────────────
        alice = Student(
            name="Alice Chen",
            email="alice@uni.edu",
            year=2
        )

        bob = Student(
            name="Bob Martinez",
            email="bob@uni.edu",
            year=1
        )

        carol = Student(
            name="Carol Singh",
            email="carol@uni.edu",
            year=3
        )

        david = Student(
            name="David Kim",
            email="david@uni.edu",
            year=2
        )

        emily = Student(
            name="Emily Nguyen",
            email="emily@uni.edu",
            year=4
        )

        frank = Student(
            name="Frank Wilson",
            email="frank@uni.edu",
            year=1
        )

        session.add_all([
            alice,
            bob,
            carol,
            david,
            emily,
            frank
        ])
        session.flush()

        # Add students to courses using the relationship
        # instead of manually inserting into the enrollment table
        alice.courses.append(db101)
        alice.courses.append(py201)

        bob.courses.append(db101)
        bob.courses.append(ai301)

        carol.courses.append(db101)
        carol.courses.append(py201)
        carol.courses.append(calc1)

        david.courses.append(db101)
        david.courses.append(ai301)

        emily.courses.append(db101)
        emily.courses.append(calc1)

        frank.courses.append(py201)
        frank.courses.append(stats)

        session.commit()

    # ── Demo 1: Each department and its teachers ──────────────────────────────
    print("=== Departments and Teachers ===")

    with Session(engine) as session:
        departments = session.execute(
            select(Department)
        ).scalars().all()

        for department in departments:
            print(f"  {department.name}:")

            for teacher in department.teachers:
                print(f"    {teacher.name}")

    print()

    # ── Demo 2: Each teacher and the courses they teach ───────────────────────
    print("=== Teachers and Courses ===")

    with Session(engine) as session:
        teachers = session.execute(
            select(Teacher)
        ).scalars().all()

        for teacher in teachers:
            print(f"  {teacher.name}:")

            for course in teacher.courses:
                print(f"    {course.title}")

    print()

    # ── Demo 3: Each course with its enrolled students ───────────────────────
    print("=== Courses and Students ===")

    with Session(engine) as session:
        courses = session.execute(
            select(Course)
        ).scalars().all()

        for course in courses:
            print(f"  {course.title}:")

            for student in course.students:
                print(f"    {student.name}")

    print()

    # ── Demo 4: Each student and the courses they're enrolled in ─────────────
    print("=== Students and Courses ===")

    with Session(engine) as session:
        students = session.execute(
            select(Student)
        ).scalars().all()

        for student in students:
            print(f"  {student.name}:")

            for course in student.courses:
                print(f"    {course.title}")

    print()

    # ── Demo 5: Any course with more than 3 students ─────────────────────────
    print("=== Courses with More Than 3 Students ===")

    with Session(engine) as session:
        # Count enrollment rows for each course and only keep courses with > 3
        stmt = (
            select(
                Course.title,
                func.count(
                    student_courses.c.student_id
                ).label("student_count")
            )
            .join(
                student_courses,
                Course.id == student_courses.c.course_id
            )
            .group_by(Course.id)
            .having(
                func.count(student_courses.c.student_id) > 3
            )
        )

        results = session.execute(stmt).all()

        for title, count in results:
            print(f"  {title}: {count} students")

    print()