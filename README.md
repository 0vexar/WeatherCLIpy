# 🔐 Weather CLI

> Weather app made in Python

![Status](https://img.shields.io/badge/status-In%20Development%20\(WIP\)-orange)
![Language](https://img.shields.io/badge/language-Python-blue)
![License](https://img.shields.io/badge/license-MIT-green)
[![uv](https://img.shields.io/badge/managed%20by-uv-261230?style=flat&logo=uv&logoColor=black)](https://docs.astral.sh/uv/)

---

## 📌 Overview
A command line weather app made with the Python Requests library and the [OpenWeatherMap API](https://openweathermap.org)

### ⭐ Credits
- This application uses [Nominatim)](https://nominatim.org/) for geocoding. 
Data is provided by [**OpenStreetMap**](https://www.openstreetmap.org/copyright) 
under the ODbL license.

---

## 🚀 Features
- [X] 🛜 API Calls
- [ ] 🔢 Current Weather
- [ ] ☁️ 5-Day Forecast
- [ ] 🟰 Backend Logic
  - [X] Fuzzy search (API built in)
  - [X] Clock backend
- [ ] 💻 Textual TUI
  - [ ] Current conditions display
  - [ ] Forecast display
  - [ ] Location details
    - [X] Name, country, state, etc
    - [ ] Population details
    - [ ] Government details
  - [X] Local clock

---

## 🧰 Tech Stack
- Language: `Python`
- Tools: `Git`, `uv`
- Libraries: `Requests`, `Textual`

---

## ⚙️ Setup

[**Get OpenWeather API key**](https://home.openweathermap.org/api_keys)

---

### With [uv](https://docs.astral.sh/uv/)
*(Recommended)*

1. Run `uv sync`
2. Run `uv run main.py`

---

### With pip

1. Make a `.env` file in the main folder
>Set `APPID` to your OpenWeatherMap API key in the .env file (`APPID=...`)
1. Run `python -m venv .venv` to set up venv
2. Activate venv (`.\.venv\Scripts\Activate.ps1` for Powershell)
3. Run `pip install -r requirements.txt` or `uv add -`
4. Run `py main.py`

---
