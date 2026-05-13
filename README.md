# 🔍 OSINT

> An open-source intelligence tool — search usernames across the web, dig into Telegram and GitHub profiles, and uncover publicly available information in seconds.

![OSINT](https://github.com/user-attachments/assets/34c4e205-45b4-49ba-844c-ae1b418b2204)

🌐 **Live Demo:** [osint-osint.up.railway.app](https://osint-osint.up.railway.app)

---

## ✨ Features

### 🌐 Web Surfer
- Enter any username and the app searches **49 platforms** simultaneously
- Returns **Found** with a direct link or **Not Found** for each platform
- Platforms include social media, forums, developer sites, and more

### 💬 Telegram Lookup
- Enter a Telegram username
- App scrapes and parses publicly available information about that user
- Results are **saved to the database** for future reference

### 🐙 GitHub Lookup
- Enter a GitHub username
- App fetches and parses public profile data, repositories, and activity
- Results are **saved to the database** for future reference

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | Bootstrap, HTML, CSS, SCSS, JavaScript |
| Database | SQLite |
| Web Scraping | BeautifulSoup4, Requests |
| Static Files | WhiteNoise |
| Hosting | Railway |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Shishikon/osint.git
cd osint

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## ⚙️ Environment Variables

Set these in your hosting dashboard or a `.env` file:

```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=yourpassword
DJANGO_SUPERUSER_EMAIL=admin@example.com
```

---

## 📁 Project Structure

```
osint/
├── project/        # Django project settings
├── OSINT/          # Main app (models, views, templates)
│   ├── static/     # CSS, SCSS, JS, images
│   └── templates/  # HTML templates
├── requirements.txt
├── build.sh        # Railway build script
└── manage.py
```

---

## 🖼️ How It Works

### Web Surfer
1. User enters a username
2. App checks the username across **49 platforms**
3. Returns a list with ✅ Found (with link) or ❌ Not Found for each platform

### Telegram & GitHub Lookup
1. User enters a username
2. App scrapes and parses all publicly available data
3. Displays the results on screen
4. Saves the search results to the database

---

## ⚠️ Disclaimer

This tool is intended for **educational and ethical research purposes only**. Only publicly available information is accessed. Always respect privacy laws and platform terms of service.

---

## 👨‍💻 Author

**Shishikon** — Trilingual Python Developer
- GitHub: [@Shishikon](https://github.com/Shishikon)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
