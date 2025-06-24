# My project for the cyber security course project 1

For this project I used Python s my coding langugae and Flask as my framework.
I used html and css for the front end of the application.

My application is a very small and simple app that let's the user make a profile that other users can view.
The application has vulnerabilities on purpose, and the correct secure way of doing things are commented out.

# Installation Instructions

## PostgreSQL Installation Guide:

First open a terminal and type in: (make sure to have this open the whole time, do not close it while running the application, otherwise the database cannot connect to the application)

```sh
$ start--pg.sh
```

Then open another terminal where you will create a database in PostgreSQL for testing, use the following commands:

```sh
$ psql
user=# CREATE DATABASE database_name;
```

Replace `database_name` with the actual name of your database.

---

## Repository Installation Guide:

### 1. Create a directory for this repository:

```sh
mkdir test
```

### 2. Navigate into the directory:

```sh
cd test
```

### 3. Clone the repository to your local machine:

```sh
git clone https://github.com/LauraImmonen/cyber-security-project-1.git
```

### 4. Move into the cloned repository:

```sh
cd test/
```

To verify that you are inside the correct repository, list the files:

```sh
ls
```

You should see files like `app.py`, `schema.sql`, etc.

---

## Setup Environment Variables

### 1. Create a `.env` file inside the repository and add your secret key:

```sh
SECRET_KEY=your_secret_key_here
```

### 2. Also add your database URL to the `.env` file:

If you created a database named `test`, your `.env` file should contain:

```sh
DATABASE_URL=postgresql:///test
```

---

## Setup Database and Virtual Environment

### 1. Create the database schema:

```sh
psql -d database_name < schema.sql
```

Replace `database_name` with the actual name of your database.

### 2. Set up a virtual environment with Linux and Mac:

```sh
python3 -m venv venv
```

### 3. Activate the virtual environment:

#### On **Linux/macOS**:

```sh
source venv/bin/activate
```

#### On **Windows**:

```sh
venv\Scripts\activate
```

---

## Install Dependencies

### 1. Install required dependencies:

```sh
pip install -r requirements.txt
```

---

## Start the Application

Run the Flask application with:

```sh
flask run
```
