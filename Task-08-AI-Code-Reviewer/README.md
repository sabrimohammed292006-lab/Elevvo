
# AI Code Reviewer

## Overview

A Python command-line application that uses a local DeepSeek model through Ollama to review Python source code and generate structured JSON reports.

---

## Features

- Reviews Python code using a local AI model.
- Identifies potential programming logic errors.
- Generates structured code review reports.
- Uses Ollama to run DeepSeek locally.
- Helps developers analyze potential code issues.

---

## Requirements

- Python 3 or a compatible Python 3 version.
- Ollama installed on your system.
- DeepSeek R1 1.5B model downloaded locally.

---

## Setup

### 1. Install Ollama

Download Ollama from the official website:

https://ollama.com/

### 2. Download the Model

```bash
ollama pull deepseek-r1:1.5b
```

### 3. Verify the Model

```bash
ollama run deepseek-r1:1.5b
```

---

## How to Run

From the Elevvo project folder, run the actual entry-point file.

For example, if the entry point is `main.py`:

```powershell
python .\Task-08-AI-Code-Reviewer\main.py
```

Make sure Ollama and the required model are available before running the application.

---

## Output

The application generates a structured JSON code review report. The exact report fields depend on the implementation.

---

## Important Notes

- AI-generated findings may be incomplete or incorrect.
- Review the results before applying suggested changes.
- The required local model must be installed before use.

---

## Learning Objectives

- Integrate a local language model into a Python application.
- Use Ollama to run AI models locally.
- Explore AI-assisted code analysis.
- Work with structured JSON reports.

---

## Author

Python Programming & AI Trainee
