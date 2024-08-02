# CareerWise - An Intelligent Career Guidance System

## Overview
CareerWise is an innovative career guidance system designed to help individuals identify suitable career paths based on their unique skills and interests. By inputting their skill levels into the system, users receive personalized career recommendations, empowering them to make informed decisions about their professional futures.

## Features
- User Registration and Login
- Profile Management
- Skill Assessment
- Personalized Career Recommendations
- Progress Tracking
- Secure Data Handling

## Requirements
- Python 3.x
- Virtual Environment
- MySQL
- `requirements.txt` file with necessary dependencies

## Installation

### Clone the Repository
```bash
https://github.com/KelvinAndzie/Mini-Project
cd CareerWise
```

### Create and Activate Virtual Environment
```bash
python -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### MySQL Setup
1. **Install MySQL**: Ensure MySQL is installed on your machine. You can download it from [MySQL Downloads](https://dev.mysql.com/downloads/).

2. **Create Database**:
   - Log into MySQL:
     ```bash
     mysql -u root -p
     ```
   - Create a new database:
     Copy career_guidance.sql from database directory

3. **Modify Database Configuration**:
   - Open `databases.py` and update the following fields with your MySQL credentials:
     ```python
     host = "your_mysql_host"
     user = "your_mysql_username"
     password = "your_mysql_password"
     database = "careerwise_db"
     ```

## Usage
After installing the dependencies and setting up MySQL, you can run the project using the following command:
```bash
python app.py
```

## Development
For development, ensure you follow these steps to maintain code quality and consistency:
1. Follow the project's coding standards.
2. Write and run tests to ensure code functionality.
3. Document your code and update this `README.md` as necessary.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any questions or feedback, please contact:
- **Developer:** Andzie Kelvin Takyi
- **Supervisor:** Dr. Asamoah
- **Institution:** Kwame Nkrumah University of Science and Technology
