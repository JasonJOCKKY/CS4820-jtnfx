import pytest
import System
import json

# Wrong password should not log into the system
def test_wrongPassword(grading_system):
    grading_system.login('saab','wrongpassword')
    assert grading_system.usr.name == 'saab'
    assert grading_system.usr.courses == json_users()['saab']['courses']


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