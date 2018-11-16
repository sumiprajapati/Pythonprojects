
def read_file():
    file = open("student.csv")
    list=[]
    for line in file.readlines():
        record = line.split(",")
        list.append(record)
    return list[1:]

def find_total_and_average(students):
    mylist = []
    for student in students:
        total = 0
        for score in student[3:8]:
            total += float(score)
        st = student[1], total, total/5
        mylist.append(st)
    return mylist


def find_pass_student(students):
    ""
    mylist = []
    for student in students:
        result = "pass"
        for score in student[3:]:
            if float(score) < 32:
                result = "fail"
                break
        if result == "pass":
            mylist.append(student)
    return mylist

def get_merit_list(students):
    ""
    passed = find_pass_student(students)
    passed_with_avg = find_total_and_average(passed)
    passed_with_avg.sort(key=lambda x:x[1], reverse=True)

    return passed_with_avg


if __name__ == '__main__':
    students = read_file()
    print(get_merit_list(students))
    # print(students)
    # tav = find_total_and_average(students)
    # ps = find_pass_student(students)
    # ml = get_merit_list(students)
    #
    # print("Average and total marks for students", tav)
    # print("List of passed student", ps)
    # print("Merit lists", ml)

