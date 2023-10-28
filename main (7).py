class Student:
  
 def __init__(self,name,roll_no,cgpa):
  self.name=name
  self.roll_no=roll_no
  self.cgpa=cgpa

def sort_students(studentlist):
  sorted_students= sorted(studentlist,
                         key=lambda student:student.cgpa,reverse=True)
  return sorted_students

#example usage
students=[Student("kavi\t","a365f\t",6.9),
          Student("suba\t","b37u8\t",7.2),
          Student("mithu\t","c754c\t",6.3),
          Student("nadhiya\t","d676g\t",8.7)]

sorted_students= sort_students(students)

for student in sorted_students:
  print("NAME:",student.name,"ROLL_NO:",student.roll_no,"CGPA:",student.cgpa)
  