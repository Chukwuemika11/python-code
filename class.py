class Course:
    def __init__(self,code, title, lecturer):
        self.code = code
        self.title = title
        self.lecturer = lecturer

    def DisplayCourse(self):
        print(f"the title course is {self.title}")
        print(f"the course code is {self.code}")
        print(f"the course is taken by {self.lecturer}")


Course1 = Course("CSC 303", "object oriented programming", "Mr.Ben")
Course1.DisplayCourse()