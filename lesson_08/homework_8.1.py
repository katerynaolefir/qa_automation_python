class Student:
    def __init__(self, name, last_name, age, average_mark):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.average_mark = average_mark

    def print_info(self):
        print(
            f"Студент: {self.name} {self.last_name}\n"
            f"Вік: {self.age}\n"
            f"Середній бал: {self.average_mark}"
            )

    def change_average_mark(self, average_mark):
        self.average_mark = average_mark


profile_of_student = Student(name='Катерина', last_name='Олефир', age=25, average_mark=80)
profile_of_student.print_info()
print('-' * 50)
profile_of_student.change_average_mark(average_mark=40)
profile_of_student.print_info()