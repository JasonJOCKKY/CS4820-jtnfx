import pytest
import System

# Check different password formats
def test_checkPassword(grading_system):
    username = 'saab'
    password = 'boomr345'
    assert grading_system.check_password(username, password)
    assert grading_system.check_password(username, 'BOOMR345')
    assert grading_system.check_password(username, ' boomr345')


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem