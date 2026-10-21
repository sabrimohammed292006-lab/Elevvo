AI Code Reviewer
Overview
A command-line Python application that uses a local AI model to review Python source code and identify potential bugs, runtime errors, style violations, and maintainability issues.
The application runs locally using Ollama and the DeepSeek R1 1.5B model.
Features

Reviews Python code using a local AI model.
Identifies potential logic bugs and runtime errors.
Suggests improvements for code quality and maintainability.
Assigns severity levels: High, Medium, and Low.
Validates the AI-generated JSON report.
Checks issue line numbers against the source file range.
Removes duplicate findings.
Saves the results to review_report.json.
Handles invalid files, empty files, connection errors, and invalid AI responses.

Requirements

Python 3.10 or newer.
Ollama installed and running.
The deepseek-r1:1.5b model downloaded locally.
No third-party Python packages required.

Setup
Install Ollama from:
https://ollama.com/
Download the model:
ollama pull deepseek-r1:1.5b

Make sure Ollama is running before starting the application.
How to Run
python main.py

Enter the path to the Python file you want to review.
Alternatively, provide the file path as an argument:
python main.py sample.py

Output
The application prints the review summary, detected issues, severity levels, line numbers, and suggested fixes.
It also generates review_report.json in the same directory as the reviewed Python file.
Limitations

AI-generated findings may be inaccurate or incomplete.
Line-number validation confirms that a line is within the file range; it does not guarantee that the finding points to the exact source location.
The application requires a running local Ollama service and the selected model.
The tool does not automatically modify or execute the reviewed source code.

License
For educational purposes.
