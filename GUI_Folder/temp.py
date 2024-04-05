# import mysql.connector as mc
# mydb = mc.connect(
#             host = "localhost",
#             user = "root",
#             password = "",
#             database = "python_project"
#         )

# mycursor = mydb.cursor()

# query1 = "select student_id,t1_python,t1_fsd,t1_de,t1_ps from sem_3_exam"
# mycursor.execute(query1)

# result = mycursor.fetchall()

# # for i in result:
# #     for j in i:
# #         print(j)

# students_marks_sum_list = []
            
# for i in result:
#     # temp = 
#     students_marks_sum_list.append((i[0], sum([i[1],i[2],i[3],i[4]])))

# # print(students_marks_sum_list)

# students_marks_sum_list.sort(key=lambda k : k[1])
# print(students_marks_sum_list)
# # print ("{:<8} {:<15} {:<10} {:<10}".format('Rank',f'{students_marks_sum_list}','','Change'))
# whichTest = "Test-1"
# print("{:<20} {:<20} {:<5} {:<25} {:<10} {:<10}".format('Rank','Enrollment Number','Div','Student Name','Mentor Short Name',f'{whichTest}\n'))
d = {1: ["Python", 33.2, 'UP'],
2: ["Java", 23.54, 'DOWN'],
3: ["Ruby", 17.22, 'UP'],
10: ["Lua", 10.55, 'DOWN'],
5: ["Groovy", 9.22, 'DOWN'],
6: ["C", 1.55, 'UP']
}
print ("{:<8} {:<15} {:<10} {:<10}".format('Pos','Lang','Percent','Change'))
for k, v in d.items():
    lang, perc, change = v
    print ("{:<8} {:<15} {:<10} {:<10}".format(k, lang, perc, change))