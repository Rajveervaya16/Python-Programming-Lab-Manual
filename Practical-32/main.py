print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565002")
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
if conn.is_connected():
    print("Database Connected Successfully")
conn.close()
