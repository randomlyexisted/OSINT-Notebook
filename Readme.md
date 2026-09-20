# OSINT Notebook 🔎

A personal OSINT (Open-Source Intelligence) research notebook for organizing investigations, people, organizations, sources, notes, and evidence in one place.

> This project is a research organization tool, not an automated "find everything about someone" tool.

## 🚧 Project Status

**Current Version: v0.1.2**

The project is currently under active development.

## ✨ Features

### v0.1.0 — Dashboard + Investigation Creation

- Dashboard
- Create investigations
- Investigation listing
- Initial Flask application structure
- Basic HTML/CSS interface

### v0.1.1 — SQLite Database

- Added SQLite database
- Investigation data is now persisted
- Connected the Flask application to the database
- Investigation records can be stored and retrieved

### v0.1.2 — Investigation Workspace

- Added an investigation workspace
- Users can open an individual investigation
- Added investigation description
- Added people to an investigation
- Investigation information is organized within the workspace

## 🛠️ Tech Stack

- Python
- Flask
- SQLite
- HTML
- CSS

## 📁 Project Structure

```text
osint-notebook/
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── create_investigation.html
│   ├── index.html
│   └── ...
│
├── .gitignore
├── app.py
├── requirements.txt
├── README.md
└── ...
```

## ⚙️ Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/randomlyexisted/OSINT-Notebook.git
cd OSINT-Notebook
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Then open the local address shown by Flask in your browser.

## 🗺️ Roadmap

Planned features include:

- More investigation workspace functionality
- People profiles
- Organizations
- Sources and references
- Notes
- Evidence management
- Relationships between entities
- Search and filtering
- Investigation timeline
- Improved UI
- Data persistence improvements
- Export functionality

## 📌 Version History

```text
v0.1.0 → Dashboard + Investigation Creation
v0.1.1 → SQLite Database
v0.1.2 → Investigation Workspace
```

### v0.1.0

Initial working milestone containing the dashboard and investigation creation functionality.

### v0.1.1

Introduced SQLite database integration for persistent investigation data.

### v0.1.2

Introduced the investigation workspace, allowing users to view an investigation, add a description, and add people associated with the investigation.

## ⚠️ Disclaimer

This project is intended for lawful research, investigation organization, education, and authorized OSINT activities.

Always respect applicable laws, privacy, terms of service, and the rights of individuals when conducting research.
