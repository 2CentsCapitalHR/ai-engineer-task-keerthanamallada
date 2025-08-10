# ADGM Corporate Agent — Beginner-friendly repo

This is a small project to process `.docx` files and produce a reviewed `.docx` and a JSON report.

## What to do (super simple steps)

1. Download and unzip the project folder.
2. Install Python (if not installed). Check with `python --version`.
3. Open a terminal (Command Prompt / PowerShell on Windows).
4. Go into the project folder, create a virtual environment and install:
   - Windows (PowerShell):
     ```
     python -m venv venv
     venv\\Scripts\\activate
     pip install -r requirements.txt
     ```
   - Mac/Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     ```
5. Run the app:
   ```
   python app.py
   ```
   Gradio will open in your browser (or show a local URL like http://127.0.0.1:7860).
6. Upload one or more `.docx` files in the web UI and get the reviewed files in `reviewed_out/`.

## If you cannot run locally
- You can create a new GitHub repo and upload these files directly (use the GitHub web interface: New repo → Upload files → Commit).

## If any step is confusing, tell me and I will walk you through that step by step.