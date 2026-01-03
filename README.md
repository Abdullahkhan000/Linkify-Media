# 🎬 Linkify-Media

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-2ea44f?style=flat)](https://github.com/Abdullahkhan000/Linkify-Media/issues)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat)](LICENSE)

<div align="center">
  <img src="assets/banner.png" alt="Linkify Media Banner" width="100%" />
  <p>
    <b>Instant TMDB · IMDb · Rotten Tomatoes Links</b><br>
    Clean JSON · Zero 404s · API Ready
  </p>
</div>

---

## 📌 About

**Linkify Media** is a lightweight **CLI utility** that automatically fetches **official and verified links** for **Movies and TV Series** using the **TMDB API**.

It removes the pain of:
- Manual searching
- Broken Rotten Tomatoes URLs
- Inconsistent movie/TV naming

Perfect for **backend APIs**, **media platforms**, and **automation scripts**.

---

## ✨ Key Features

| Feature | Status | Description |
| :--- | :---: | :--- |
| **Smart Fetching** | ✅ | Uses official **TMDB IDs & titles** |
| **Multi-Platform Links** | 🔗 | Generates **TMDB**, **IMDb**, & **Rotten Tomatoes** |
| **RT URL Validation** | 🛡️ | Prevents broken / 404 RT links |
| **Movie + TV Support** | 📺 | Works for both Movies & TV Series |
| **Clean JSON Output** | 🎨 | Pretty-printed & API-friendly |

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

    git clone https://github.com/Abdullahkhan000/Linkify-Media
    cd your-repo

---

### 2️⃣ Set up Virtual Environment (Recommended)

**Windows**

    python -m venv venv
    venv\Scripts\activate

**Mac / Linux**

    python3 -m venv venv
    source venv/bin/activate

---

### 3️⃣ Install Dependencies

    pip install requests
    pip install django-decouple
    or use pip install - requirements.txt

---

### 4️⃣ Configure TMDB API Key

**Option A: Environment Variable (Recommended)**

**Mac / Linux**

    export TMDB_API_KEY="your_actual_api_key_here"

**Windows (CMD)**

    set TMDB_API_KEY="your_actual_api_key_here"

**Windows (PowerShell)**

    $env:TMDB_API_KEY="your_actual_api_key_here"

---

**Option B: `.env` File (Most Secure & Recommended)**

1. Create a `.env` file in the project root  
2. Add the following line:

    TMDB_API_KEY=your_actual_api_key_here

3. Load the key in your code:

    from decouple import config
    TMDB_API_KEY = config("TMDB_API_KEY")

> ⚠️ Always add `.env` to **.gitignore** to protect your API keys.

---

**Option C: Direct Edit (Quick Start / Not Recommended)**

    # Open movie_link_generator.py
    TMDB_API_KEY = "YOUR_ACTUAL_API_KEY_HERE"

---

### 5️⃣ Run the Script

    python main.py

---

## 📤 Sample Output

    {'Official Title': 'The Dark Knight Rises',
     'TMDB Link': 'https://www.themoviedb.org/movie/49026',
     'IMDb Link': 'https://www.imdb.com/title/tt1345836/',
     'Rotten Tomatoes Link': 'https://www.rottentomatoes.com/m/the_dark_knight_rises'}

---

## 🧩 Use Cases

- Backend movie / TV APIs
- Streaming & media platforms
- Automation scripts
- Freelance & portfolio projects
- Data scraping & enrichment pipelines

---

## 🛣️ Roadmap

- [ ] Batch processing support
- [ ] Optional caching
- [ ] Docker support
- [ ] PyPI package release

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository  
2. Create a new branch  
3. Commit your changes  
4. Open a Pull Request  

---

## ❤️ Support the Project

If this project saves you time or helps your work:

### 👉 Support via Patreon

[![Patreon](https://img.shields.io/badge/Support-Patreon-orange?style=flat&logo=patreon)](https://www.patreon.com/c/code2encoder)

Your support helps:
- Add new features
- Improve performance
- Maintain long-term updates

---

## 📄 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it.

---

⭐ If you find this project useful, don’t forget to **star the repository**!

---

<div align="center">
  <p>🚀 This project is proudly made by <b>code2encoder aka / Shadow Dev</b> 🚀</p>
</div>
