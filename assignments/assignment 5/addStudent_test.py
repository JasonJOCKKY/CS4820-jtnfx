import pytest
import System
import json

# Login as a professor and add a student
def test_addStudent(grading_system):
    username = 'saab'
    password = 'boomr345'
    course = 'comp_sci'
    newStudent = 'hdjsr7'
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