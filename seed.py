from faker import Faker
from sqlite3 import Error, Connection
from connect import create_connection, database


def insert_data(conn: Connection, sql: str, data: tuple) -> int:
    """Inserts data into the database."""
    cur = conn.cursor()
    try:
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
    finally:
        cur.close()


def create_students(conn: Connection, num_students: int) -> None:
    """Creates student records in the database."""
    fake = Faker()
    students = [
        (i, fake.name(), fake.random_int(min=1, max=3))
        for i in range(1, num_students + 1)
    ]
    sql = """
    INSERT INTO students(student_id, student_name, group_id)
    VALUES (?, ?, ?)
    """
    for student in students:
        insert_data(conn, sql, student)


def create_groups(conn: Connection) -> None:
    """Creates group records in the database."""
    sql = """
    INSERT INTO groups(group_id, group_name)
    VALUES (?, ?)
    """
    groups = [(1, "Group A"), (2, "Group B"), (3, "Group C")]
    for group in groups:
        insert_data(conn, sql, group)


def create_teachers(conn: Connection, num_teachers: int) -> None:
    """Creates teacher records in the database."""
    fake = Faker()
    teachers = [(i, fake.name()) for i in range(1, num_teachers + 1)]
    sql = """
    INSERT INTO teachers(teacher_id, teacher_name)
    VALUES (?, ?)
    """
    for teacher in teachers:
        insert_data(conn, sql, teacher)


def create_subjects(conn: Connection, num_subjects: int) -> None:
    """Creates subject records in the database."""
    fake = Faker()
    subjects = [
        (i, fake.word(), fake.random_int(min=1, max=5))
        for i in range(1, num_subjects + 1)
    ]
    sql = """
    INSERT INTO subjects(subject_id, subject_name, teacher_id)
    VALUES (?, ?, ?)
    """
    for subject in subjects:
        insert_data(conn, sql, subject)


def create_grades(conn: Connection, num_students: int, num_subjects: int) -> None:
    """Creates grade records in the database."""
    fake = Faker()
    grades = [
        (
            i,
            fake.random_int(min=1, max=num_students),
            fake.random_int(min=1, max=num_subjects),
            fake.random_int(min=60, max=100),
            fake.date(),
        )
        for i in range(1, 21)
    ]
    sql = """
    INSERT INTO grades(grade_id, student_id, subject_id, grade, date_received)
    VALUES (?, ?, ?, ?, ?)
    """
    for grade in grades:
        insert_data(conn, sql, grade)


if __name__ == "__main__":
    fake = Faker()
    num_students = fake.random_int(min=30, max=50)
    num_teachers = fake.random_int(min=3, max=5)
    num_subjects = fake.random_int(min=5, max=8)

    with create_connection(database) as conn:
        if conn is not None:
            create_students(conn, num_students)
            create_groups(conn)
            create_teachers(conn, num_teachers)
            create_subjects(conn, num_subjects)
            create_grades(conn, num_students, num_subjects)
        else:
            print("Error! Cannot create the database connection.")
