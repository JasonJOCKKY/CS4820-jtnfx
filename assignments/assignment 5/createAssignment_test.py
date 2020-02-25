import pytest
import System
import json

# Login as a professor and create assignment
def test_createAssignment(grading_system):
    username = 'saab'
    password = 'boomr345'
    course = 'comp_sci'
    newAssignment = 'assignment000'
    newDueDate = '5/10/21'
    grading_system.login(username, password)
    grading_system.usr.create_assignment(newAssignment, newDueDate, course)
    assert json_courses()[course]['assignments'][newAssignment]['due_date'] == newDueDate

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def json_courses():
    with open('Data/courses.json') as f:
        courses = json.load(f)
    return courses