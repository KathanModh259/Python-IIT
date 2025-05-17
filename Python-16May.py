import math

# 1. Library Access System
print("== 1. Library Access System ==")

class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id

    def display_info(self):
        print(f"Name: {self.name}, Membership ID: {self.membership_id}")

class StudentMember(Member):
    def __init__(self, name, membership_id):
        super().__init__(name, membership_id)
        self.books_borrowed = 0

    def add_book(self):
        self.books_borrowed += 1
        print("Book added.")

    def return_book(self):
        if self.books_borrowed > 0:
            self.books_borrowed -= 1
            print("Book returned.")
        else:
            print("No books to return.")

    def borrowing_status(self):
        print(f"{self.name} has borrowed {self.books_borrowed} book(s).")

student = StudentMember("Kathan", "LIB123")
student.display_info()
student.add_book()
student.add_book()
student.borrowing_status()
student.return_book()
student.borrowing_status()


# 2. Drone Fleet Management
print("\n== 2. Drone Fleet Management ==")

class Device:
    def __init__(self, device_id):
        self.device_id = device_id

    def device_info(self):
        print(f"Device ID: {self.device_id}")

class Flyer:
    def fly(self):
        print("Drone is flying...")

class Drone(Device, Flyer):
    def __init__(self, device_id):
        super().__init__(device_id)

    def capture_image(self):
        print("Image captured by the drone.")

drone = Drone("DRN001")
drone.device_info()
drone.fly()
drone.capture_image()


# 3. Online Learning Platform
print("\n== 3. Online Learning Platform ==")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"User: {self.name}, Email: {self.email}")

class Instructor(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def upload_content(self, content):
        print(f"Instructor uploaded: {content}")

    def display_info(self):
        print(f"Instructor: {self.name}, Email: {self.email}, Subject: {self.subject}")

class CourseCreator(Instructor):
    def __init__(self, name, email, subject):
        super().__init__(name, email, subject)
        self.courses = []

    def create_course(self, course_name):
        self.courses.append(course_name)
        print(f"Course '{course_name}' created.")

    def display_info(self):
        print(f"Course Creator: {self.name}, Email: {self.email}, Subject: {self.subject}, Courses: {self.courses}")

creator = CourseCreator("Kathan", "kathan@example.com", "Python")
creator.upload_content("OOP Concepts")
creator.create_course("Python for Beginners")
creator.display_info()


# 4. Smart Home Appliance
print("\n== 4. Smart Home Appliance ==")

class Appliance:
    def status(self):
        print("Appliance is functioning normally.")

class Fan(Appliance):
    def status(self):
        print("Fan is spinning.")

class Light(Appliance):
    def status(self):
        print("Light is turned on.")

class AC(Appliance):
    def status(self):
        print("AC is cooling the room.")

devices = [Fan(), Light(), AC()]
for device in devices:
    device.status()


# 5. Geometry Toolkit
print("\n== 5. Geometry Toolkit ==")

class ShapeCalculator:
    def area(self, a, b=None):
        if b is None:
            return math.pi * a * a
        else:
            return a * b

calc = ShapeCalculator()
print(f"Area of circle (r=5): {calc.area(5):.2f}")
print(f"Area of rectangle (l=4, w=6): {calc.area(4, 6)}")
