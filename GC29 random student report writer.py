import random
a_good_comment = (" achieves fantastic grades in his exams. ")
b_good_comment = (" is very cheerful in class. ")
c_good_comment = (" is always ready to help others. ")
d_good_comment = (" thinks differently and out of the box. ")
e_good_comment = (" gets involved in group discussions frequently with some great ideas. ")

a_ebi = (" Needs to get involved in class discussions")
b_ebi = (" Needs to proactively ask for feedback and work to achieve them")
c_ebi = (" Must learn to ask homework questions in advance before the lesson")
d_ebi = (" Should improve his listening skills")


good_comments_list = [a_good_comment, b_good_comment, c_good_comment, d_good_comment, e_good_comment]
ebis_list = [a_ebi, b_ebi, c_ebi, d_ebi]
comment = []
Number_of_students = int(input("How many students are there in the class in total"))
for student in range(1, Number_of_students+1):
   Name = input("What is the name of number " + str(student) + " student?")
   for good_comments in range(2):
       two_good_comments = random.choice(good_comments_list)
       comment.append(Name + two_good_comments)
   for ebis in range(1):
       one_ebi = random.choice(ebis_list)
       comment.append(Name + one_ebi)
   print("".join(comment))
   comment.clear()

