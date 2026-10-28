# 💊 MediFind — Medicine Substitute Finder

### Find affordable medicine alternatives with the same composition.

MediFind is a database-driven web application developed using **Python, Flask, MySQL, HTML, and CSS**. It helps users search for medicines and identify potentially cheaper alternatives with the same composition, making medicine price comparison simpler and more accessible.

The project demonstrates how database management, backend development, and web technologies can be integrated to solve a practical healthcare-related problem.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [System Architecture](#-system-architecture)
- [Database Design](#-database-design)
- [Project Structure](#-project-structure)
- [Installation and Setup](#-installation-and-setup)
- [Running the Application](#-running-the-application)
- [How It Works](#-how-it-works)
- [Future Enhancements](#-future-enhancements)
- [Disclaimer](#-disclaimer)
- [Author](#-author)

---

## 🔍 Overview

Medicine prices can vary significantly between brands, even when medicines contain the same active composition. Finding a more affordable option can therefore be challenging.

**MediFind** addresses this problem by allowing users to search for a medicine and compare its price with other medicines listed in the database that have the same composition.

The application uses Flask to handle requests, MySQL to store and retrieve medicine and supplier information, and HTML to provide the user interface.

### 🎯 Project Objectives

- Develop a web-based medicine search and comparison system.
- Store medicine and supplier information in a relational database.
- Retrieve medicines with matching compositions.
- Identify potentially cheaper alternatives using database queries.
- Demonstrate the integration of SQL, Python, Flask, and frontend technologies.

---

## ✨ Key Features

- **🔎 Medicine Search:** Search for medicines using their names.
- **💰 Price Comparison:** Compare medicine prices to identify lower-cost options.
- **🧪 Composition-Based Matching:** Find listed medicines that share the same composition.
- **🏷️ Alternative Suggestions:** Display potentially cheaper alternatives based on available database records.
- **🏥 Supplier Information:** Maintain supplier details in the database.
- **➕ Medicine Management:** Support adding medicine records through the application.
- **🗄️ Relational Database:** Use MySQL to store and manage structured medicine data.
- **🌐 Web Interface:** Access the application through a browser using a Flask-powered backend.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| MySQL | Relational database management |
| SQL | Database creation, querying, and manipulation |
| HTML | Web page structure |
| CSS | User interface styling |
| mysql-connector-python | Python–MySQL connectivity |
| Git and GitHub | Version control and source code hosting |

---

## 🏗️ System Architecture

MediFind follows a simple three-layer architecture.

```text
┌───────────────────────────────────┐
│          Presentation Layer       │
│          HTML / CSS               │
│          User Interface           │
└─────────────────┬─────────────────┘
                  │ HTTP Requests
                  ▼
┌───────────────────────────────────┐
│          Application Layer        │
│          Python + Flask           │
│     Search and Comparison Logic   │
└─────────────────┬─────────────────┘
                  │ SQL Queries
                  ▼
┌───────────────────────────────────┐
│           Database Layer          │
│              MySQL                │
│       Det and Supplier Tables     │
└───────────────────────────────────┘
```

**Workflow:** User input → Flask processing → MySQL query → Result processing → Results displayed in the browser.

---

## 🗄️ Database Design

The project uses a MySQL database named `MediFindDB`.

### Database Tables

#### 1. `Det` — Medicine Details

Stores information about the medicines available for searching and comparison.

| Column | Description |
|---|---|
| `Med_ID` | Medicine identifier |
| `Med_Name` | Name of the medicine |
| `Composition` | Medicine composition |
| `Med_Type` | Type or category of medicine |
| `Disease` | Associated disease or condition |
| `Price` | Listed medicine price |

#### 2. `Supplier` — Supplier Details

Stores supplier-related information associated with the medicine database.

> Refer to `MediFindDB.sql` for the exact table definitions, column names, constraints, and sample records.

### Database Operations

The project uses SQL operations to support:

- Database and table creation
- Inserting medicine and supplier records
- Retrieving medicine details
- Filtering medicines by composition
- Comparing medicine prices
- Managing medicine records

---

## 📁 Project Structure

```text
Medicine-Substitute-Finder/
│
├── templates/
│   └── user.html          # Web interface
│
├── MediFindDB.sql         # Database schema and sample data
├── user.py                # Flask application and backend logic
├── requirements.txt       # Python dependencies
├── .gitignore             # Files excluded from version control
├── .gitattributes         # GitHub language detection settings
└── README.md              # Project documentation
```

---

## ⚙️ Installation and Setup

Follow these steps to run MediFind on your local machine.

### Prerequisites

Install the following:

- Python 3
- MySQL Server
- MySQL Workbench (recommended)
- Git (optional, for cloning the repository)

### 1. Clone the Repository

```bash
git clone https://github.com/ShounakRoy23062/Medicine-Substitute-Finder.git
```

Navigate to the project directory:

```bash
cd Medicine-Substitute-Finder
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

If you use Command Prompt instead of PowerShell:

```bat
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Set Up the MySQL Database

1. Open MySQL Workbench.
2. Connect to your local MySQL Server.
3. Open `MediFindDB.sql`.
4. Execute the SQL script.
5. Confirm that the `MediFindDB` database and its tables have been created.

If the script does not create or select the database automatically, create it first:

```sql
CREATE DATABASE IF NOT EXISTS MediFindDB;
USE MediFindDB;
```

Run the remaining table-creation and data-insertion statements from the project SQL file.

### 5. Configure Database Credentials

For local testing, the application needs the correct MySQL host, username, password, port, and database name.

**Recommended:** Store credentials in environment variables instead of hardcoding them in `user.py`.

In PowerShell, set the variables in the same terminal you will use to launch Flask:

```powershell
$env:DB_HOST = "localhost"
$env:DB_USER = "root"
$env:DB_PASSWORD = "YOUR_MYSQL_PASSWORD"
$env:DB_NAME = "MediFindDB"
$env:DB_PORT = "3306"
```

Replace `YOUR_MYSQL_PASSWORD` with your actual local MySQL password. Do not commit real passwords or credentials to GitHub.

The database connection in `user.py` should read these variables using Python's `os.getenv()`.

---

## ▶️ Running the Application

After installing the dependencies and configuring the database, run:

```bash
python user.py
```

Open your browser and visit:

**http://127.0.0.1:5000/**

The Flask application should load, allowing you to interact with the medicine search interface.

> If the application cannot connect to MySQL, verify that MySQL Server is running, the database exists, and your connection credentials are correct.

---

## 🔄 How It Works

1. **Search:** The user enters the name of a medicine.
2. **Retrieve:** Flask receives the request and queries the MySQL database.
3. **Match:** The application identifies medicines with matching compositions.
4. **Compare:** The prices of matching medicines are compared.
5. **Display:** The application presents the available medicine information and potentially cheaper alternatives.

The results depend on the medicine records and prices stored in the database.

---

## 🚀 Future Enhancements

Potential improvements include:

- **Expanded Medicine Database:** Add more medicine records and verified composition information.
- **Advanced Search:** Search by medicine name, composition, category, or associated condition.
- **Improved UI:** Develop a responsive interface with better search results and comparison tables.
- **Supplier Comparison:** Include more supplier information and availability details.
- **User Authentication:** Introduce secure user accounts and role-based access.
- **Real-Time Pricing:** Integrate reliable, authorized data sources for updated medicine prices.
- **Testing and Validation:** Add automated tests for database queries, search logic, and Flask routes.
- **Deployment:** Host the application on a suitable server with secure configuration.

---

## ⚠️ Disclaimer

MediFind is an educational database project intended to demonstrate medicine information retrieval and price comparison.

**A matching composition in a database does not, by itself, establish that two medicines are interchangeable.** Formulation, strength, dosage, release mechanism, contraindications, and other clinical factors may differ. Always consult a qualified healthcare professional or pharmacist before changing medicines.

Prices and medicine information are limited to the records available in the application's database and should not be treated as real-time or independently verified information.

---

## 👨‍💻 Author

**Shounak Roy**

- GitHub: [@ShounakRoy23062](https://github.com/ShounakRoy23062)
- Project Repository: [Medicine Substitute Finder](https://github.com/ShounakRoy23062/Medicine-Substitute-Finder)

---

⭐ If you find this project interesting, consider starring the repository!

**Built with Python, Flask, MySQL, and SQL.**