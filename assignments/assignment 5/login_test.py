import pytest
import System
import json

# Test if the login creates the right user
def test_login(grading_system):
    for user in json_users():
        grading_system.login(user, json_users()[user]['password'])
        assert grading_system.usr.name == user
        assert grading_system.usr.courses == json_users()[user]['courses']
    
    # # Test Professor
    # grading_system.login('saab','boomr345')
    # assert grading_system.usr.name == 'saab'
    # assert grading_system.usr.courses == json_users()['saab']['courses']

    # # Test Student
    # grading_system.login('akend3','123454321')
    # assert grading_system.usr.name == 'akend3'
    # assert grading_system.usr.courses == json_users()['akend3']['courses']

    # # Test TA
    # grading_system.login('cmhbf5','bestTA')
    # assert grading_system.usr.name == 'cmhbf5'
    # assert grading_system.usr.courses == json_users()['cmhbf5']['courses']


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