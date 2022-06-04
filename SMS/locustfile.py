from email import header
import json
from locust import HttpUser, task

class Testing(HttpUser):
    #login to the roles is necessary in order to perform further testing
    def on_start(self):
        self.login_student()
        self.login_teacher()

    #authentication of student
    def login_student(self):
        # login to the application
        response = self.client.get('\student_login.php')
        csrftoken = response.cookies['csrftoken']
        self.client.post('/student_login',
                         {'email':'albert@gmail.com', 'password': 'albert@123'},
                         headers={'X-CSRFToken': csrftoken})

    #authentication of teacher
    def login_teacher(self):
    # login to the application
        response = self.client.get('/admin_login.php')
        csrftoken = response.cookies['csrftoken']
        self.client.post('/admin_login.php',
                            {'email':'admin@gmail.com', 'password': 'admin@123'},
                            headers={'X-CSRFToken': csrftoken})

    #tasks to be tested:
    @task
    def basic_get_test(self):
        self.client.get("/admin")   