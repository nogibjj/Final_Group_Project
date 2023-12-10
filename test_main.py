import os
import tempfile
import pytest
from main import app, get_daily_schedule
from dotenv import load_dotenv
import openai

# Load environment variables for the OpenAI API key
load_dotenv()
openai.api_key = os.getenv("API_TOKEN")


def test_html_files_exist(directory="templates/"):
    """Check if HTML files exist in the specified directory."""
    html_files = ['index.html', 'schedule_form.html', 'schedule.html']
    for html_file in html_files:
        file_path = os.path.join(directory, html_file)
        assert os.path.exists(file_path) and os.path.isfile(file_path)


def test_openai_api_call():
    """Test the OpenAI API call for generating a schedule."""
    test_tasks = "Task 1: Code review\nTask 2: Team meeting\nTask 3: Write documentation"
    schedule = get_daily_schedule(test_tasks)
    assert schedule is not None and len(schedule) > 0


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_index_page(client):
    """Test the index page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Your Daily Schedule Planner" in response.data


def test_schedule_form_page(client):
    """Test the schedule form page."""
    response = client.get('/schedule')
    assert response.status_code == 200
    assert b"Input Your Tasks for Today" in response.data

if __name__ == "__main__":
    test_html_files_exist()
    test_openai_api_call()
