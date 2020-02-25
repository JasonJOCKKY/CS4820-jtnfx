import pytest
import System
import json

# Login as a student, test the check_ontime() function
def test_checkOntime(grading_system):
    username = 'akend3'
    password = '123454321'
    grading_system.login(username, password)

    # check_ontime(submission_date, due_date)
    assert grading_system.usr.check_ontime('2/3/20', '3/4/20')
    assert grading_system.usr.check_ontime('5/3/20', '3/4/20') == False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def json_users():
    with open('Data/users.json') as f:
        users = json.load(f)
    return users