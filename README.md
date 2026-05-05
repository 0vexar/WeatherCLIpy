# 🔐 Weather CLI

> Weather app made in Python

![Status](https://img.shields.io/badge/status-In%20Development%20\(WIP\)-orange)
![Language](https://img.shields.io/badge/language-Python-blue)
![License](https://img.shields.io/badge/license-MIT-green)
[![uv](https://img.shields.io/badge/managed%20by-uv-261230?style=flat&logo=uv&logoColor=black)](https://docs.astral.sh/uv/)

---

## 📌 Overview
A command line weather app made with the Python Requests library and the [OpenWeatherMap API](https://openweathermap.org)

---

## 🚀 Features
- [X] 🛜 API Calls
- [ ] 🔢 Current Weather
- [ ] ☁️ 5-Day Forecast
- [ ] 🟰 Backend Logic
  - [ ] Fuzzy Search
  - [ ] Search Error Handling
- [ ] 💻 Textual TUI
  - [ ] Current Conditions Display
  - [ ] Forecast Display
  - [ ] City Details

---

## 🧰 Tech Stack
- Language: `Python`
- Tools: `Git`, `uv`
- Libraries: `Requests`, `Textual`, `iso3166`, `typing`

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