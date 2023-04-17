class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.finished_courses or course in self.courses_in_progress) \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_rate(self)}' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return average_rate(self) < average_rate(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_rate(self)}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return average_rate(self) < average_rate(other)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def average_rate(self):
    grades = []
    for val in self.grades.values():
        grades.extend(val)
    result = round(sum(grades) / len(grades), 1)
    return result


def average_hw_rate_in_course(students_list, course):
    grades = []
    for student in students_list:
        if isinstance(student, Student) and \
                (course in student.finished_courses or course in student.courses_in_progress):
            grades.extend(student.grades[course])
    result = round(sum(grades) / len(grades), 1)
    return result


def average_lec_rate_in_course(lecturers_list, course):
    grades = []
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            grades.extend(lecturer.grades[course])
    result = round(sum(grades) / len(grades), 1)
    return result


student_1 = Student('Harry', 'Potter', 'male')
student_1.courses_in_progress += ['Occlumency']
student_1.courses_in_progress += ['Care of Magical Creatures']
student_1.courses_in_progress += ['Potion Information Tracker']
student_1.finished_courses += ['Introduction to potions']

student_2 = Student('Ron', 'Weasley', 'male')
student_2.courses_in_progress += ['Care of Magical Creatures']
student_2.courses_in_progress += ['Potion Information Tracker']
student_2.finished_courses += ['Introduction to potions']

student_3 = Student('Hermione', 'Granger', 'female')
student_3.courses_in_progress += ['Care of Magical Creatures']
student_3.courses_in_progress += ['Potion Information Tracker']
student_3.finished_courses += ['Introduction to potions']

some_students = [student_1, student_2, student_3]

lecturer_1 = Lecturer('Severus', 'Snape')
lecturer_1.courses_attached += ['Occlumency']
lecturer_1.courses_attached += ['Potion Information Tracker']
lecturer_1.courses_attached += ['Introduction to potions']

lecturer_2 = Lecturer('Rubeus', 'Hagrid')
lecturer_2.courses_attached += ['Care of Magical Creatures']

some_lecturers = [lecturer_1, lecturer_2]

reviewer_1 = Reviewer('Draco', 'Malfoy')
reviewer_1.courses_attached += ['Potion Information Tracker']
reviewer_1.courses_attached += ['Introduction to potions']

reviewer_2 = Reviewer('Albus', 'Dumbledore')
reviewer_2.courses_attached += ['Potion Information Tracker']
reviewer_2.courses_attached += ['Introduction to potions']
reviewer_2.courses_attached += ['Occlumency']
reviewer_2.courses_attached += ['Care of Magical Creatures']

reviewer_1.rate_hw(student_1, 'Potion Information Tracker', 2)
reviewer_1.rate_hw(student_1, 'Potion Information Tracker', 1)
reviewer_1.rate_hw(student_1, 'Potion Information Tracker', 3)

reviewer_1.rate_hw(student_2, 'Potion Information Tracker', 1)
reviewer_1.rate_hw(student_2, 'Potion Information Tracker', 2)
reviewer_1.rate_hw(student_2, 'Potion Information Tracker', 2)

reviewer_1.rate_hw(student_3, 'Potion Information Tracker', 4)
reviewer_1.rate_hw(student_3, 'Potion Information Tracker', 5)
reviewer_1.rate_hw(student_3, 'Potion Information Tracker', 6)

reviewer_2.rate_hw(student_1, 'Occlumency', 10)
reviewer_2.rate_hw(student_1, 'Care of Magical Creatures', 10)

student_1.rate_lec(lecturer_1, 'Occlumency', 6)
student_1.rate_lec(lecturer_1, 'Potion Information Tracker', 5)
student_1.rate_lec(lecturer_1, 'Introduction to potions', 4)
student_1.rate_lec(lecturer_2, 'Care of Magical Creatures', 10)

student_2.rate_lec(lecturer_1, 'Potion Information Tracker', 5)
student_2.rate_lec(lecturer_1, 'Introduction to potions', 4)
student_2.rate_lec(lecturer_2, 'Care of Magical Creatures', 10)

student_3.rate_lec(lecturer_1, 'Potion Information Tracker', 8)
student_3.rate_lec(lecturer_1, 'Introduction to potions', 9)
student_3.rate_lec(lecturer_2, 'Care of Magical Creatures', 10)

print(student_1.grades)
print(lecturer_1.grades)
print(lecturer_2.grades)
print(student_1)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(lecturer_1 < lecturer_2)
print(student_1 < student_2)
print(f"Курс: Pit\nСредняя оценка: {average_hw_rate_in_course(some_students, 'Potion Information Tracker')}")
print(f"Курс: Pit\nСредняя оценка: {average_lec_rate_in_course(some_lecturers, 'Potion Information Tracker')}")
