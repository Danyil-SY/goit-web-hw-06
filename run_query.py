import sqlite3


def execute_query(file) -> list:
    with sqlite3.connect("study.db") as con:
        cur = con.cursor()
        with open(file, "r") as f:
            sql = f.read()
        cur.execute(sql)
        return cur.fetchall()


def main():
    try:
        task = input("Enter query number (01, 02, 03 ... 12): ")
        file = "query_" + task + ".sql"
        print(execute_query(file))
    except ValueError:
        print("Wrong query number.")


if __name__ == "__main__":
    main()
