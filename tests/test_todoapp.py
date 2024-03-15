import pytest
from todowebapp import create_app, db
from todowebapp.models import User, Note
from werkzeug.security import generate_password_hash
from bs4 import BeautifulSoup

# Create test data
test_password = "Password1!"
test_user = User(
            email="test@test.com",
            firstName="Test",
            password=generate_password_hash(test_password,
                                            method='pbkdf2:sha256'))
test_note = "Test note"

@pytest.fixture(scope='session')
def app():
    app = create_app('sqlite:///:memory:')
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        yield app
        clean_up(app)


# Clean up and remove in memory database
def clean_up(app):
    db.drop_all()

    # Close the database connection
    db.session.close_all()
    db.engine.dispose()

    print("Database deleted successfully!")

@pytest.fixture(scope='function')
def client(app):
    with app.test_client() as client:
        yield client


# Test for a redirect to login page
def test_home_view_unauthenticated(client):
    response = client.get('/')
    # Check for successful redirect and redirect to loign page
    assert response.status_code == 302
    assert b'/login' in response.data


# Test user is presente with error message
# when the signup passwords don't match
def test_signup_passwords_not_match(client):
    response = client.post('/signup', data={"email": test_user.email,
                                            "firstName": test_user.firstName,
                                            "password1": test_password,
                                            "password2": "Password2!"})

    # Parse HTML content
    soup = BeautifulSoup(response.data, 'html.parser')

    # Find the div with id "message"
    content_div = soup.find('div', id='message')

    # Check if content_div exists and contains the correct message
    assert content_div is not None
    assert 'Passwords don\'t match.' in content_div.get_text()


# Test user is presented with error message
# when the email address is less than 6 characters
def test_signup_email_less_than_6(client):
    response = client.post('/signup', data={"email": "test",
                                            "firstName": test_user.firstName,
                                            "password1": test_password,
                                            "password2": test_password})

    # Parse HTML content
    soup = BeautifulSoup(response.data, 'html.parser')

    # Find the div with id "message"
    content_div = soup.find('div', id='message')

    # Check if content_div exists and contains the correct message
    assert content_div is not None
    assert 'Email must be greater than 6 characters.' in content_div.get_text()


# Test user is presented with error message
# when the name less than 2 characters
def test_signup_name_less_than_2(client):
    response = client.post('/signup', data={"email": test_user.email,
                                            "firstName": "T",
                                            "password1": test_user.password,
                                            "password2": test_user.password})

    # Parse HTML content
    soup = BeautifulSoup(response.data, 'html.parser')

    # Find the div with id "message"
    content_div = soup.find('div', id='message')

    # Check if content_div exists and contains the correct message
    assert content_div is not None
    assert 'First name must be greater than 1 character.' in \
        content_div.get_text()


# Test user is presented with error message when
# the password dosen't contain a number
def test_signup_password_no_number(client):
    response = client.post('/signup', data={"email": test_user.email,
                                            "firstName": test_user.firstName,
                                            "password1": "Password!",
                                            "password2": "Password!"})

    # Parse HTML content
    soup = BeautifulSoup(response.data, 'html.parser')

    # Find the div with id "message"
    content_div = soup.find('div', id='message')

    # Check if content_div exists and contains the correct message
    assert content_div is not None
    assert 'Password must contain at least 1 number.' in content_div.get_text()


# Test user is presented with error message when
# the password dosen't contain a special character
def test_signup_password_no_special_character(client):
    response = client.post('/signup', data={"email": test_user.email,
                                            "firstName": test_user.firstName,
                                            "password1": "Password1",
                                            "password2": "Password1"})

    # Parse HTML content
    soup = BeautifulSoup(response.data, 'html.parser')

    # Find the div with id "message"
    content_div = soup.find('div', id='message')

    # Check if content_div exists and contains the correct message
    assert content_div is not None
    assert 'Password must contain at leaset 1 special character.' in \
        content_div.get_text()


# Test user is presented with error message when
# the password is less than 8 characters
def test_signup_password_less_than_8(client):
    response = client.post('/signup', data={"email": test_user.email,
                                            "firstName": test_user.firstName,
                                            "password1": "Pass1!",
                                            "password2": "Pass1!"})

    # Parse HTML content
    soup = BeautifulSoup(response.data, 'html.parser')

    # Find the div with id "message"
    content_div = soup.find('div', id='message')

    # Check if content_div exists and contains the correct message
    assert content_div is not None
    assert 'Password must be greater than 8 characters.' in \
        content_div.get_text()


# Test sign up page
def test_signup_new_user(client):
    response = client.post('/signup', data={"email": test_user.email,
                                            "firstName": test_user.firstName,
                                            "password1": test_user.password,
                                            "password2": test_user.password})
    # Check user is redirected to home page
    assert response.status_code == 302
    assert b'/' in response.data
    # Check user has been stored in the database
    test_data = User.query.filter_by(email="test@test.com")
    assert test_data


# Check a user can login
def test_home_view_authenticated(client):

    # Log in the user
    response = client.post('/login',
                           data=dict(email=test_user.email,
                                     password=test_user.password),
                           follow_redirects=True)
    # Check request was successful
    assert response.status_code == 200


# Test that a logged in user can add a note
def test_add_note_authenticated(client):

    # Create a test note
    response = client.post('/', data={"note": test_note})

    # Check the note is succesfully submitted
    assert response.status_code == 200

    # Check the note is in the database
    check_test_note = Note.query.filter_by(data=test_note).first()
    assert check_test_note


# Test that a user can toggle a note completed
def test_toggle_note_complete(client):
    # Get the test note from database to pass the note id into the url
    check_test_note = Note.query.filter_by(data=test_note).first()
    done_status = check_test_note.done

    # Toggle the note
    response = client.get(f'/edit-note/{check_test_note.id}',
                          follow_redirects=True)

    # Check if the note is edited successfully
    assert response.status_code == 200
    assert check_test_note.done != done_status
