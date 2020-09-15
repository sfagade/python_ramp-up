student_grades = [6.27, 3.82, 12.66, 4.83, 12.96, 2.67, 4.93, 2.58]


def mean(my_list):
    the_mean = sum(my_list) / len(my_list)
    return the_mean


print(mean(student_grades))
