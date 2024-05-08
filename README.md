# -telegram-exchange-rate-bot

У файлі README.md ви можете включити таку інформацію про ваш проект:
markdownCopy code# Telegram Exchange Rate Bot

Цей бот для Telegram дає змогу отримувати поточний курс долара США до української гривні з Google Finance і відправляє його користувачеві у вигляді файлу Excel.

## Вимоги

- Python 3.6 або вище
- Бібліотеки: requests, beautifulsoup4, python-telegram-bot, openpyxl

## Встановлення

1. Клонуйте цей репозиторій:
git clone https://github.com/your-username/telegram-exchange-rate-bot.git
Copy code
2. Створіть файл `.env` у кореневій директорії проєкту і додайте туди свій токен Telegram бота:
BOT_TOKEN=your_bot_token
Copy code
3. Встановіть необхідні бібліотеки Python:
pip install -r requirements.txt
Copy code
## Використання

1. Запустіть бота:
python main.py
Скопіюйте код
2. У Telegram знайдіть свого бота і надішліть йому команду `/get_exchange_rate`.

3 Бот надішле вам файл Excel із поточним курсом долара США до гривні.

## Ліцензія

Цей проект поширюється під ліцензією [MIT](LICENSE).

## Contributing

Будь ласка, дотримуйтесь інструкцій у [CONTRIBUTING.md](CONTRIBUTING.md) для отримання інформації щодо процесу внесення змін до цього проекту.

Translated with DeepL.com (free version)
