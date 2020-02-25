import pytest
import System
import json

# Check different password formats
def test_checkPassword(grading_system):
    for user in json_users():
        assert grading_system.check_password(user, json_users()[user]['password'])

    # assert grading_system.check_password('saab', 'boomr345')
    # assert grading_system.check_password('akend3', 'BOOMR345')
    # assert grading_system.check_password(username, ' boomr345')


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def json_users():
    with open('Data/users.json') as f:
        users = json.load(f)
    return users