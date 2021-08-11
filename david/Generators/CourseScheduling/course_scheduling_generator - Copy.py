

import collections


def solve(fnames, lnames, courses):
  outStr = ""
  courseMap = collections.OrderedDict()
  for c in courses:
    courseMap[c] = 0
 
  used = []

  for f, l, c in zip(fnames, lnames, courses):
    if (f,l,c) not in used:
      used.append((f,l,c))
      courseMap[c] += 1

  for course in courseMap.keys():
   print(course + " " + str(courseMap[course]) + "\n")
    

  


def main():

  # length = int(input())
  # fnames = []
  # lnames = []
  # courses = []

  # for i in range(length):
  #   inStr = input()
  #   f,l,c = inStr.split()

  #   fnames.append(f)
  #   lnames.append(l)
  #   courses.append(c)


  # solve(fnames,lnames,courses)
  n = int(input())
  courses = {}
  for _ in range(n):
  	student, course = input().rsplit(' ', 1)
  	courses.setdefault(course, set()).add(student)
  for course, students in sorted(courses.items()):
  	print(course, len(students))
main()
