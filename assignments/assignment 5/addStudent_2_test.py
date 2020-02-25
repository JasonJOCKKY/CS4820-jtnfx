import pytest
import System
import json

# The professor should not be able to add student to courses that the professor do not teach
def test_addStudent_2(grading_system):
    username = 'saab'
    password = 'boomr345'
    course = 'cloud_computing'
    newStudent = 'akend3'
    grading_system.login(username, password)
    grading_system.usr.add_student(newStudent, course)
    assert json_users()[newStudent]['courses'][course]

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def json_users():
    with open('Data/users.json') as f:
        users = json.load(f)
    return users