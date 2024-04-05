import mysql.connector as mc

mydb = mc.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "python_project"
        )
def storeDataForLastDiv(i):
    mycursor = mydb.cursor()

    query4 = "INSERT INTO class (ID,python_faculty,fsd_faculty,de_faculty,ps_faculty,students) VALUES (%s, %s, %s, %s, %s, %s)"

    with open(f"D:\\Projects_Sem-3\\Python-I_Individual\\class\\D6\\students.txt", 'r') as f:
        content = f.read()
        print(content)
        value = (i.id, i.python_faculty, i.fsd_faculty, i.de_faculty, i.ps_faculty, content)

        mycursor.execute(query4, value) 
        mydb.commit()
