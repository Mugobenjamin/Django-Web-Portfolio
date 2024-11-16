# README.md

## Django Portfolio Website

### Description
This project is a personal portfolio website built using the Django framework. It showcases skills, projects, and professional experience, making it an ideal tool for sharing professional profiles online. The front-end design is created using HTML, CSS, and Bootstrap for a responsive and visually appealing layout, while Python is used on the back-end for robust functionality.

---

### Features
- **Home Page**: A welcoming introduction with a brief bio.
- **About Section**: Detailed information about education, skills, and personal interests.
- **Portfolio**: Highlights of completed projects with descriptions and images.
- **Contact Form**: A fully functional contact form to receive messages via email.
- **Responsive Design**: Optimized for viewing on both desktop and mobile devices.

---

### Technologies Used
- **Framework**: Django (Python)
- **Front-End**:
  - HTML5
  - CSS3
  - Bootstrap
- **Back-End**: Python (Django)
- **Database**: SQLite (default Django database)

---

### Installation

#### Prerequisites
- Python 3.x installed on your system
- Django installed (`pip install django`)
- A text editor or IDE (e.g., VSCode, PyCharm)

#### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Mugobenjamin/Django-Web-Portfolio.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Django-Web-Portfolio
   ```


3. Run the Django migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

5. Open a browser and visit:
   ```
   http://127.0.0.1:8000/
   ```

---

### Project Structure
```
project_directory/
│
├── portfolio/                # Django app
│   ├── templates/            # HTML templates
│   ├── static/               # Static files (CSS, JS, Images)
│   ├── views.py              # Views for handling requests
│   └── models.py             # Database models
│
├── manage.py                 # Django management script
├── db.sqlite3                # SQLite database
```

---

### Customization
You can customize the portfolio content by modifying:
- **Templates**: Edit the HTML files in the `templates/` directory.
- **Static Files**: Add or modify CSS and JS in the `static/` folder.
- **Database**: Update models in `models.py` and run migrations to apply changes.

---

### Contribution
Contributions are welcome! Feel free to submit a pull request or open an issue for feature suggestions or bug fixes.

---

### License
This project is licensed under the [MIT License](LICENSE).

---
