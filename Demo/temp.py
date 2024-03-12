f = open(f"D:\\Projects_Sem-3\\Python-I_Individual\\class\\D5\\students.txt", 'r')
content = f.read()
print(content,"prince") 
        # query5 = "INSERT INTO class (students) VALUES (%s)"
        # value = (content,)
        # mycursor.execute(query5, value)
        # mydb.commit()