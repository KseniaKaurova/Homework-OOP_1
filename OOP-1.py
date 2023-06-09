class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_lecture(self, lecture, course, grade):
        if course in self.courses_in_progress and isinstance(lecture, Lecturer):
            if course in lecture.courses_attached:
                lecture.grades[course] += grade
            else:
                lecture.grades[course] = grade
        else:
            return 'Что-то не сходится...'

    def average(self):
        s = 0
        l = 0
        for k, v in self.grades.items():
            s += sum(v)
            l += len(v)
        average = s / l

        return average

    def __str__(self):
        return f'Имя: {self.name}' \
               f'Фамилия: {self.surname}' \
               f'Средняя оценка за домашние задания: {self.average()}' \
               f'Курсы в процессе изучения: {self.courses_in_progress}' \
               f'Завершенные курсы: {self.finished_courses}'

    def __lt__(self, other):
        if self.average() < other.avуrage():
            return self.name, self.surname
        else:
            return other.name, other.surname


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average(self):
        s = 0
        l = 0
        for k, v in self.grades.items():
            s += sum(v)
            l += len(v)
        average = s / l

        return average

    def __str__(self):
        return f'Имя: {self.name} ' \
               f'Фамилия: {self.surname} ' \
               f'Средняя оценка за лекции: {self.average()}'

    def __lt__(self, other):
        if self.average() < other.avуrage():
            return self.name, self.surname
        else:
            return other.name, other.surname


class Reviewer(Mentor):
    def grade(self, student, course, grade):
        if course in student.grades:
            student.grades[course] += grade
        else:
            student.grades[course] = grade

    def __str__(self):
        return f'Имя: {self.name}' \
               f' Фамилия: {self.surname}'


def average_students_course(student_list, course):
    s = 0
    l = 0
    for student in student_list:
        s += sum(student.grades.get(course, []))
        l += len(student.grades.get(course, []))

    return s / l


def average_lecture_course(lecture_list, course):
    s = 0
    l = 0
    for lecture in lecture_list:
        s += sum(lecture.grades.get(course, []))
        l += len(lecture.grades.get(course, []))

    return s / l


sasha = Student('Sasha', 'Ivanov', 'm')
vasy = Student('Vasiliy', 'Petrov', 'm')
egor = Student('Egor', 'Sidorov', 'm')
masha = Student('Masha', 'Semenova', 'w')
katy = Student('Ekaterina', 'Karpova', 'w')
andreeva = Lecturer('Nina', 'Andreeva')
nikolaeva = Lecturer('Olga', 'Nikolaeva')
timonov = Lecturer('Vadim', 'Timonov')
savkin = Lecturer('Alexey', 'Savkin')
smirnov = Reviewer('Artem', 'Smirnov')
fedorov = Reviewer('Vadim', 'Fedorov')

student_list = [sasha, vasy, egor, masha, katy]
lecture_list = [andreeva, nikolaeva, timonov, savkin]

