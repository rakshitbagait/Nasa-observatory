# 🌌 NASA Observatory
![NASA Logo](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDcwaTN3dHptYW5hbWVxY213MXA5OXZ5MnkxYzF0ZGRzcWJidnNxZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gkgwQkzP3lN5u/giphy.gif)


**NASA Observatory** is a beginner-friendly web application built using **Flask** that allows users to explore the universe through real data provided by **NASA Open APIs**. The project focuses on learning **API handling**, **backend–frontend integration**, and **dynamic content rendering** using Python and Jinja templates.

---

## 🚀 Project Overview

NASA Observatory enables users to:
- View NASA’s **Astronomy Picture of the Day (APOD)** with scientific explanations
- Search for **stars, galaxies, nebulae, and planets**
- Explore authentic space images and descriptions curated by NASA

The application is intentionally kept simple so developers can clearly understand how APIs are consumed and how data flows from backend to frontend.

---

## 🖼️ Application Screenshots

### Home Page – APOD View
![Home Page](/assets/home_page.png)

### Search Results Page
![Search Results](/assets/image.png)

---

## 🧠 Technologies Used

### 🔹 Backend
- **Python 3** – Core programming language
- **Flask** – Lightweight web framework for routing and rendering templates
- **Requests** – To make HTTP requests to external APIs
- **python-dotenv** – For secure environment variable management

### 🔹 Frontend
- **HTML5** – Structure of the web pages
- **CSS3** – Styling and layout (space-themed UI)
- **Jinja2** – Template engine for dynamic content rendering

---

## 🛰️ APIs Used

### 1️⃣ NASA Astronomy Picture of the Day (APOD) API

**Endpoint:**
```
https://api.nasa.gov/planetary/apod
```

**Purpose:**
- Displays a daily image or video of the universe
- Provides scientifically accurate explanations written by NASA experts

**Data Used:**
- Image/Video URL
- Title
- Date
- Explanation
- Media type (image or video)

---

### 2️⃣ NASA Image and Video Library API

**Endpoint:**
```
https://images-api.nasa.gov/search?q={query}
```

**Purpose:**
- Allows users to search for space-related objects
- Returns multiple images with metadata

**Data Used:**
- Image URLs
- Titles
- Descriptions
- NASA-curated metadata

---

## 🔑 API Authentication

The project uses a **free NASA API key**, generated from:
👉 https://api.nasa.gov

The API key is stored securely using environment variables (`.env` file) to follow best security practices.

---

## 📂 Project Structure

```
nasa-observatory/
│── static/
│   └── styles.css
│── templates/
│   ├── index.html
│   └── results.html
│── assets/
│   ├── nasa_logo.png
│   ├── home_page.png
│   └── search_results.png
│── app.py
│── .env
│── README.md
```

---

## 🎯 Learning Outcomes

- Understanding REST APIs and JSON responses
- Flask routing and request handling
- Conditional rendering in Jinja templates
- Handling external media (images & embedded videos)
- Clean separation of frontend and backend logic

---

## 🌟 Future Enhancements

- Pagination for search results
- Mobile-responsive UI
- Favorites feature
- Deployment on cloud platforms (Render/Railway)

---

## 📜 License

This project is for educational purposes and uses publicly available NASA APIs.

---

**Built with curiosity, code, and the cosmos 🚀**

