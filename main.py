from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
import openai

# Load environment variables
load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("API_TOKEN")

@app.route("/")
def index():
    """Return the index page."""
    return render_template("index.html")

def get_daily_schedule(tasks):
    """
    Generate a daily schedule based on the list of tasks.
    """
    prompt = f"Create a daily schedule based on these tasks:\n{tasks}\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route("/schedule", methods=["GET", "POST"])
def schedule():
    """
    Handle the scheduling functionality.
    """
    if request.method == "POST":
        tasks = request.form.get("tasks")
        schedule = get_daily_schedule(tasks)
        return render_template("schedule.html", schedule=schedule)
    return render_template("schedule_form.html")

if __name__ == "__main__":
    app.run(debug=True)
