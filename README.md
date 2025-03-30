# AI Chatbot with Flask and Gemini AI

## Overview
This project is a simple AI chatbot built using Flask, Google Gemini AI, and Bootstrap. The chatbot allows users to send messages and receive AI-generated responses in real-time.

## Features
- AI-powered responses using Google Gemini AI.
- Interactive chatbot interface with Bootstrap.
- Flask backend to handle requests.
- Responsive and styled UI.

## Project Structure
```
|-- app.py           # Flask backend
|-- templates/
|   |-- index.html   # Frontend UI
|-- static/
|   |-- style.css    # Styling for UI
```

## Requirements
- Python 3
- Flask
- Google Generative AI SDK

## Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd <project-folder>
   ```

2. Install dependencies:
   ```sh
   pip install flask google-generativeai
   ```

3. Set up your Google Gemini AI API key in `app.py`:
   ```python
   API_KEY = ""
   ```

4. Run the Flask app:
   ```sh
   python app.py
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Usage
- Type a message in the input box.
- Click "Send" to receive a response from the AI.
- The conversation appears dynamically on the page.

## Technologies Used
- Flask (Backend)
- Google Gemini AI (AI Responses)
- Bootstrap (Frontend UI)
- HTML/CSS/JavaScript (Frontend Implementation)

## Future Improvements
- Add user authentication.
- Store chat history.
- Improve UI/UX with animations.

## License
This project is open-source and free to use.

