import pytest
import System
import json

# Login as a professor and create assignment in the course that the professor does not teach
def test_createAssignment_2(grading_system):
    username = 'saab'
    password = 'boomr345'
    course = 'databases'
    newAssignment = 'assignment000'
    newDueDate = '5/10/21'
    grading_system.login(username, password)
    grading_system.usr.create_assignment(newAssignment, newDueDate, course)
    assert json_courses()[course]['assignments'][newAssignment]['due_date'] is None # The professor should not be able to do this

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def json_courses():
    with open('Data/courses.json') as f:
        courses = json.load(f)
    return courses