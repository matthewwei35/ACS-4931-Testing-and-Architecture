# By Kamran Bigdely Nov. 2020
# Replace temp variable with query

# TODO: Use 'extract method' refactoring technique to improve this code.
# TODO: If required, use 'replace temp variable with query' technique to make it easier to extract methods.

class Employer:
    def __init__(self, name):
        self.name = name
    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
    def get_gpa(self):
        return self.gpa
    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students) -> None:
        self.students = students
    def check_gpa(self, min_gpa, passed_students):
        for s in self.students:
            if s.get_gpa() > min_gpa:
                passed_students.append(s)
    def print_graduated_students(self, passed_students):
        print('*** Student who graduated *** ')
        for s in passed_students:
            print(s.name)
        print('****************************')
    def send_congrats_email(self, passed_students):
        for s in passed_students:
            s.send_congrat_email()
    def get_percentile(self, percentile, passed_students):
        int(percentile * len(passed_students))
    def process_graduation(self):
        # Find the students in the school who have successfully graduated.
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        self.check_gpa(min_gpa, passed_students)
        # print student's name who graduated.
        self.print_graduated_students(passed_students)
        # Send congrat emails to them.
        self.send_congrats_email(passed_students)
        # Find the top 10% of them and send their contact to the top employers
        passed_students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        top_10_percent = passed_students[self.get_percentile(percentile, passed_students):]
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        for e in top_employers:
            e.send(top_10_percent)

students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'),
            Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
school  = School(students)
school.process_graduation()
