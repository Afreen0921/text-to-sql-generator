# Text-to-SQL Generator

## Overview
This project converts natural language questions into SQL queries using Generative AI.

## Features
- Natural Language to SQL conversion
- Structured JSON output
- Schema-aware query generation
- Ambiguity handling
- Streamlit user interface

## Technologies Used
- Python
- Streamlit
- Groq API
- Llama 3.1
- Pydantic

## Project Structure

text-to-sql-generator/
│
├── app.py
├── model.py
├── prompt.py
├── parser.py
├── requirements.txt
├── README.md
└── screenshots/

## Run Locally

1. Clone repository

```bash
git clone YOUR_REPO_LINK
```

2. Create virtual environment

```bash
python -m venv venv
```

3. Activate environment

```bash
venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run application

```bash
streamlit run app.py
