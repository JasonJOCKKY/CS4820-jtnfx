import pytest
import System
import json

# Login as a student and view assignments
def test_viewAssignment(grading_system):
    username = 'akend3'
    password = '123454321'
    course = 'cloud_computing'
    grading_system.login(username, password)
    
    # assignments obtained from the function
    assigns = grading_system.usr.view_assignments(course)

    # assignments obrained from db
    db_assigns = []
    for key in json_courses()[course]['assignments']:
        db_assigns.append([key, json_courses()[course]['assignments'][key]['due_date']])
    
    assert assigns == db_assigns

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def json_users():
    with open('Data/users.json') as f:
        users = json.load(f)
    return users

def json_courses():
    with open('Data/courses.json') as f:
        courses = json.load(f)
    return courses