import pytest
import System
import json

# Login as a student and submit an assignment, check the submission and submission date
def test_submitAssignment(grading_system):
    username = 'akend3'
    password = '123454321'
    course = 'comp_sci'
    assignment = 'assignment2'
    submission = 'New Submission'
    submission_date = '4/10/20'
    grading_system.login(username, password)
    grading_system.usr.submit_assignment(course,assignment,submission,submission_date)
    assert json_users()[username]['courses'][course][assignment]['submission'] == submission
    assert json_users()[username]['courses'][course][assignment]['submission_date'] == submission_date

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def json_users():
    with open('Data/users.json') as f:
        users = json.load(f)
    return users