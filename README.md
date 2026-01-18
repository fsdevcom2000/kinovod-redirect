# Kinovod Auto-Domain Redirector

Этот проект — асинхронный сервис на Flask, который автоматически перенаправляет пользователя на актуальный рабочий домен `kinovod*.pro`. Проверяются домены за сегодня и до 5 дней назад, причём все запросы выполняются **параллельно** благодаря `aiohttp + asyncio`.

Если ни один домен не работает, отображается страница ошибки с тёмной темой, неоновым эффектом и адаптивной версткой.

## 🚀 Возможности

- Асинхронная проверка доменов
    
- Параллельные HTTP‑запросы через `aiohttp`
    
- Автоматический выбор самого первого доступного домена
    
- Кастомная страница ошибки:
    
    - Тёмная тема
        
    - Неоновая подсветка
        
    - SVG‑иконка
        
    - Плавная анимация появления
        
    - Адаптивность под мобильные устройства
        

## 📦 Требования

- Python 3.9+
    
- Flask
    
- aiohttp
    

Установка зависимостей:

```
pip install flask aiohttp
```

## ▶️ Запуск сервера


```
python app.py
```

Сервис будет доступен по адресу:

```
http://0.0.0.0:9999
```

## 📁 Структура проекта

```
project/
│
├── app.py                     # Основная логика Flask + маршруты + проверка доменов
│
├── templates/                 # HTML-шаблоны (рендерятся Flask)
│   ├── checking.html          # Страница "Ждите, идёт проверка..."
│   └── error.html             # Страница ошибки, если домен не найден
│
└── static/                    # Статические файлы (CSS, JS, изображения)
    ├── css/
    │   └── checking.css       # Стили для страницы проверки
    |   └── error.css          # Стили для страницы ошибки
    │
    └── js/
        └── checking.js        # Логика проверки доменов через /check
```

## 🌐 Как это работает

1. Генерируются 5 доменов:
    
    - Сегодня
        
    - Вчера
        
    - До 5 дней назад
        
2. Все домены проверяются **одновременно**.
    
3. Первый доступный домен выбирается.
    
4. Если ничего не найдено — показывается страница ошибки.

---

# Kinovod Auto-Domain Redirector

This project provides an asynchronous Flask-based service that automatically redirects users to the most recent available `kinovod*.pro` domain.  

It checks today's domain and up to 5 days back using fully parallel asynchronous requests (`aiohttp + asyncio`) for maximum speed.

If no domain is available, the user is shown a custom error page with a dark theme, neon styling, and adaptive layout.

---

## 🚀 Features

  

- Asynchronous domain checking (extremely fast)

- Parallel HTTP requests using `aiohttp`

- Automatic selection of the most recent working domain

- Custom error page with:

  - Dark theme

  - Neon glow effect

  - SVG icon

  - Smooth fade‑in animation

  - Mobile‑friendly adaptive layout

---

## 📦 Requirements

  

- Python 3.9+

- Flask

- aiohttp


Install dependencies:

```bash
pip install flask aiohttp
```
  

## ▶️  Running the Server

  ```bash
  python app.py
  ```

The service will start on:

```
http://0.0.0.0:9999
```

## 📁 Project Structure

```
project/
│
├── app.py                     # Main Flask logic + routes + domain checking
│
├── templates/                 # HTML templates (rendered by Flask)
│   ├── checking.html          # "Please wait, checking..." page
│   └── error.html             # Error page shown when no domain is found
│
└── static/                    # Static files (CSS, JS, images)
    ├── css/
    │   └── checking.css       # Styles for the checking page
    │   └── error.css          # Styles for the error page
    │
    └── js/
        └── checking.js        # Logic for domain checking via /check

```

## 🌐 How It Works

1. The server generates 5 possible domain names:
    
    - Today
        
    - Yesterday
        
    - Up to 5 days back
        
2. All domains are checked **simultaneously** using asynchronous requests.
    
3. The first working domain (HTTP 200) is selected.
    
4. If no domain is available, the user sees a styled error page.
