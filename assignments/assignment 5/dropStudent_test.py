import pytest
import System
import json

# Login as a professor and drop a student
def test_dropStudent(grading_system):
    username = 'goggins'
    password = 'augurrox'
    course = 'software_engineering'
    dropStudent = 'yted91'
    grading_system.login(username, password)
    grading_system.usr.drop_student(dropStudent, course)
    courses = json_users()[dropStudent]['courses']
    isPresent = False
    for element in courses:
        if element == course:
            isPresent = True

    assert isPresent == False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def json_users():
    with open('Data/users.json') as f:
        users = json.load(f)
    return users