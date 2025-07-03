# Online Innovators & Business Portal 🌐

 A Django-based web platform that connects innovative idea creators with business professionals. Innovators can upload and showcase their ideas, while business users can browse, connect, and invest in promising concepts.

A Django‑based web platform that bridges the gap between **innovators** and **businessperson**.  
Innovators post fresh business ideas, while investors browse, filter, and connect to fund the best concepts.  
Secure logins, role‑based dashboards, and a clean Bootstrap UI keep everything simple and fast.

---

## ✨ Key Features
- **Dual roles** → Innovator & Businessperson, each with its own dashboard.  
- Post, edit, or delete ideas with file uploads & rich‑text descriptions.  
- Category / sub‑category filters for quick idea discovery.  
- Inquiry system so investors can contact innovators in‑app.  
- Basic payment‑flow stub.

---

## 🛠 Tech Stack
| Layer           | Tools                    |
|-----------------|--------------------------|
| Backend         | **Python 3**, **Django 4** |
| Front‑end       | HTML, CSS, **Bootstrap 5** |
| Database (dev)  | MYSQL |
| Auth / Security | Django auth + CSRF + env‑based secrets |

---

## 🚀 Local Setup
1. **Clone repo**  
   ```bash
   git clone https://github.com/mamta-codehub/online-innovators-business-portal.git
   cd online-innovators-business-portal
2. **Create & activate virtualenv → python -m venv env && source env/Scripts/activate**

3. **Install deps → pip install -r requirements.txt**

4. **Env vars → copy .env.example to .env & add your SECRET_KEY.**

5. **Run → python manage.py migrate && python manage.py runserver**


