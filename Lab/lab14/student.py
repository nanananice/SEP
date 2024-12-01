class University():
    def __init__(self):
        self.name = ''
        self.program = []
        self.student = {id:student}


class Student():
    def __init__(self):
        self.id = id
        self.name =''
        self.status = 'normal'
        self.course = []

class Program():
    def __init__(self, courselist):
        self.level = ''
        self.name = ''
        self.start = ''
        self.course = [courselist]

    def addCourse(self, course):
        pass

    def getCourse(self, course):
        pass

class Course():
    def __init__(self, Lecturer, student):
        self.credit = 0
        self.id = 0
        self.lecturer = Lecturer
        self.name = ''
        self.semester = ''
        self.student_list = [student]
    
    def enroll(self, char):
        pass
    
    def getcredit(self):
        pass

    def getLecturer(self):
        pass

    def getStuents(self):
        pass

class Lecturer():
    def __init__(self):
        self.name =''
        self.course = []
    
    def getCourse(self):
        pass

class Takes():
    def __init__(self):
        self.student = []
        self.course = []
        self.grade = ''
        self.scores = 0

class Transcript():
    def __init__(self):
        self.complete = True
        self.issue_date = ''
        self.takes = []
    
    def printTranscript(self):
        pass

