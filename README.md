# AskingOpenAI
Asking Questions to OpenAI

 My Flask App

This is a simple Flask web application that includes a home page and an about page.
La Home Page fue modificada para atraves de un Form se le puedan hacer preguntas a Open AI (GPT 4o)

## Project Structure

```
my-flask-app
├── app.py
├── templates
│   ├── base.html
│   ├── home.html
│   └── about.html
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── scripts.js
├── LICENSE
└── README.md
```

## Requirements

- Python 3.x
- Flask
- openAI

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-flask-app
   ```

2. Install the required packages:
   ```
   pip install Flask
   pip install openai
   ```

## Running the Application

To run the Flask application, execute the following command:

```
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Routes

- `/` - Home page
- `/about` - About page

## License

This project is licensed under the MIT License.
