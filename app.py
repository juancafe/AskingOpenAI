import os
from flask import Flask, render_template, request, redirect, url_for, flash
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flashing messages

token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['POST'])
def submit():
    question = request.form['question']
    response = client.chat.completions.create(
            messages=[{"role": "user", "content": question}],
            model=model_name,
            temperature=0.7
    )
    answer = response.choices[0].message.content
    return f"Question: {question} <br> Answe: {answer}"

if __name__ == '__main__':
    app.run(debug=True)
