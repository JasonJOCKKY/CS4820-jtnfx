import pytest
import System
import json

# Login as a professor and change grade
def test_changeGrade(grading_system):
    username = 'saab'
    password = 'boomr345'
    course = 'comp_sci'
    student = 'akend3'
    assignment = 'assignment1'
    newGrade = 50
    grading_system.login(username, password)
    grading_system.usr.change_grade(student, course, assignment, newGrade)
    assert json_users()[student]['courses'][course][assignment]['grade'] == newGrade

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def json_users():
    with open('Data/users.json') as f:
        users = json.load(f)
    return users