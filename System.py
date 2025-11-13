import mysql.connector

# ---------- DATABASE CONNECTION ----------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # change to your MySQL username
        password="yourpassword",  # change to your MySQL password
        database="student_db"     # make sure this database exists
    )

# ---------- ADD STUDENT ----------
def add_student():
    con = connect_db()
    cur = con.cursor()
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Course: ")
    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    cur.execute(query, (name, age, course))
    con.commit()
    print(" Student added successfully!")
    con.close()

# ---------- VIEW STUDENTS ----------
def view_students():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    print("\n--- Student Records ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")
    con.close()

# ---------- UPDATE STUDENT ----------
def update_student():
    con = connect_db()
    cur = con.cursor()
    sid = int(input("Enter Student ID to Update: "))
    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    course = input("Enter New Course: ")
    query = "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s"
    cur.execute(query, (name, age, course, sid))
    con.commit()
    print("Student record updated successfully!")
    con.close()

# ---------- DELETE STUDENT ----------
def delete_student():
    con = connect_db()
    cur = con.cursor()
    sid = int(input("Enter Student ID to Delete: "))
    query = "DELETE FROM students WHERE id=%s"
    cur.execute(query, (sid,))
    con.commit()
    print(" Student record deleted successfully!")
    con.close()

# ---------- MAIN MENU ----------
def main():
    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print(" Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
