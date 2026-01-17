# Kinovod Auto-Domain Redirector

Этот проект — асинхронный сервис на Flask, который автоматически перенаправляет пользователя на актуальный рабочий домен `kinovod*.pro`. Проверяются домены за сегодня и до 10 дней назад, причём все запросы выполняются **параллельно** благодаря `aiohttp + asyncio`.

Если ни один домен не работает, отображается красивая страница ошибки с тёмной темой, неоновым эффектом и адаптивной версткой.

## 🚀 Возможности

- Асинхронная проверка доменов (очень быстро)
    
- Параллельные HTTP‑запросы через `aiohttp`
    
- Автоматический выбор самого свежего доступного домена
    
- Кэширование результата в памяти
    
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
├── app.py
├── templates/
│   └── error.html
└── static/
    └── style.css
```

## 🌐 Как это работает

1. Генерируются 10 доменов:
    
    - Сегодня
        
    - Вчера
        
    - До 10 дней назад
        
2. Все домены проверяются **одновременно**.
    
3. Первый доступный домен выбирается.
    
4. Результат кэшируется.
    
5. Если ничего не найдено — показывается страница ошибки.

---

# Kinovod Auto-Domain Redirector

This project provides an asynchronous Flask-based service that automatically redirects users to the most recent available `kinovod*.pro` domain.  

It checks today's domain and up to 10 days back using fully parallel asynchronous requests (`aiohttp + asyncio`) for maximum speed.

If no domain is available, the user is shown a custom error page with a dark theme, neon styling, and adaptive layout.

---

## 🚀 Features

  

- Asynchronous domain checking (extremely fast)

- Parallel HTTP requests using `aiohttp`

- Automatic selection of the most recent working domain

- In-memory caching to avoid repeated lookups

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
  python3 app.py
  ```

The service will start on:

```
http://0.0.0.0:9999
```

## 📁 Project Structure

```
project/
│
├── app.py
├── templates/
│   └── error.html
└── static/
    └── style.css
```

## 🌐 How It Works

1. The server generates 10 possible domain names:
    
    - Today
        
    - Yesterday
        
    - Up to 10 days back
        
2. All domains are checked **simultaneously** using asynchronous requests.
    
3. The first working domain (HTTP 200) is selected.
    
4. The result is cached for future requests.
    
5. If no domain is available, the user sees a styled error page.