from sqlite3 import Error, Connection
from connect import create_connection, database


def create_table(conn: Connection, create_table_sql: str) -> None:
    """Creates a table in the database."""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(f"Error creating table: {e}")


if __name__ == "__main__":
    sql_create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
        student_id INT PRIMARY KEY,
        student_name TEXT NOT NULL,
        group_id INT,
        FOREIGN KEY (group_id) REFERENCES groups(group_id)
    );
    """

    sql_create_groups_table = """
    CREATE TABLE IF NOT EXISTS groups (
        group_id INT PRIMARY KEY,
        group_name TEXT NOT NULL
    );
    """

    sql_create_teachers_table = """
    CREATE TABLE IF NOT EXISTS teachers (
        teacher_id INT PRIMARY KEY,
        teacher_name TEXT NOT NULL
    );
    """

    sql_create_subjects_table = """
    CREATE TABLE IF NOT EXISTS subjects (
        subject_id INT PRIMARY KEY,
        subject_name TEXT NOT NULL,
        teacher_id INT,
        FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
    );
    """

    sql_create_grades_table = """
    CREATE TABLE IF NOT EXISTS grades (
        grade_id INT PRIMARY KEY,
        student_id INT,
        subject_id INT,
        grade INT,
        date_received DATE,
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
    );
    """

    with create_connection(database) as conn:
        if conn is not None:
            create_table(conn, sql_create_students_table)
            create_table(conn, sql_create_groups_table)
            create_table(conn, sql_create_teachers_table)
            create_table(conn, sql_create_subjects_table)
            create_table(conn, sql_create_grades_table)
        else:
            print("Error! Cannot create the database connection.")
