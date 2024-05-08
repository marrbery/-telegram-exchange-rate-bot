# -telegram-exchange-rate-bot

В файле README.md вы можете включить следующую информацию о вашем проекте:
markdownCopy code# Telegram Exchange Rate Bot

Этот бот для Telegram позволяет получать текущий курс доллара США к украинской гривне из Google Finance и отправляет его пользователю в виде файла Excel.

## Требования

- Python 3.6 или выше
- Библиотеки: requests, beautifulsoup4, python-telegram-bot, openpyxl

## Установка

1. Клонируйте этот репозиторий:
git clone https://github.com/your-username/telegram-exchange-rate-bot.git
Copy code
2. Создайте файл `.env` в корневой директории проекта и добавьте туда свой токен Telegram бота:
BOT_TOKEN=your_bot_token
Copy code
3. Установите необходимые библиотеки Python:
pip install -r requirements.txt
Copy code
## Использование

1. Запустите бота:
python main.py
Copy code
2. В Telegram найдите своего бота и отправьте ему команду `/get_exchange_rate`.

3. Бот отправит вам файл Excel с текущим курсом доллара США к гривне.

## Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE).

## Contributing

Пожалуйста, следуйте инструкциям в [CONTRIBUTING.md](CONTRIBUTING.md) для получения информации о процессе внесения изменений в этот проект.
