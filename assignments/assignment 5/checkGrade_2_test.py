import pytest
import System
import json

# Login as a student and check the grades from the course that the student is not enrolled into
def test_checkGrade_2(grading_system):
    username = 'akend3'
    password = '123454321'
    course = 'cloud_computing'
    grading_system.login(username, password)
    
    # grades obtained from the function
    grades = grading_system.usr.check_grades(course)

    # grades obrained from db
    db_grades = []
    for key in json_users()[username]['courses'][course]:
        db_grades.append([key, json_users()[username]['courses'][course][key]['grade']])
    
    assert grades == db_grades

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def json_users():
    with open('Data/users.json') as f:
        users = json.load(f)
    return users