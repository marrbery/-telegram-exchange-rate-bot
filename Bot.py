import requests
from bs4 import BeautifulSoup
import datetime
import schedule
import sqlite3
import telebot
import openpyxl
import logging

# Налаштування логування
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# URL для парсингу курсу долара до гривні
EXCHANGE_RATE_URL = "https://www.google.com/finance/quote/USD-UAH"

# Ініціалізація бота
bot = telebot.TeleBot("ВАШ_ТОКЕН_ТЕЛЕГРАМ_БОТА")

def parse_exchange_rate():
    """
    Функція для парсингу курсу долара до гривні.
    Відправляє запит на сайт, отримує курс та зберігає в базі даних.
    """
    try:
        response = requests.get(EXCHANGE_RATE_URL)
        response.raise_for_status()  # Перевірка на наявність помилок у запиті

        soup = BeautifulSoup(response.text, "html.parser")
        exchange_rate_element = soup.select_one('div[data-reload-url="/search?q=USD+UAH"]')
        if exchange_rate_element:
            exchange_rate = exchange_rate_element.text.strip()

            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            save_to_database(current_time, exchange_rate)
    except requests.exceptions.RequestException as e:
        logging.error(f"Помилка при отриманні курсу: {e}")
    except Exception as e:
        logging.error(f"Сталася помилка: {e}")

def save_to_database(timestamp, rate):
    """
    Функція для зберігання даних про курс в базі даних.
    """
    try:
        conn = sqlite3.connect('exchange_rates.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS exchange_rates (
                            id INTEGER PRIMARY KEY,
                            timestamp TEXT,
                            rate TEXT
                          )''')

        cursor.execute("INSERT INTO exchange_rates (timestamp, rate) VALUES (?, ?)", (timestamp, rate))
        
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        logging.error(f"Помилка при роботі з базою даних: {e}")
    except Exception as e:
        logging.error(f"Сталася помилка: {e}")

def parse_exchange_rate():
    """
    Функція для парсінгу курсу долара до гривні.
    """
    try:
        response = requests.get(EXCHANGE_RATE_URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        exchange_rate_element = soup.select_one('div[data-reload-url="/search?q=USD+UAH"]')
        if exchange_rate_element:
            exchange_rate = exchange_rate_element.text.strip()

            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Збереження даних у базі даних з новим часом
            save_to_database(current_time, exchange_rate)
    except requests.exceptions.RequestException as e:
        logging.error(f"Помилка при отриманні курсу: {e}")
    except Exception as e:
        logging.error(f"Сталася помилка: {e}")

def send_exchange_rate(bot, chat_id):
    """
    Функція для відправлення курсу користувачеві в форматі XLSX.
    """
    try:
        conn = sqlite3.connect('exchange_rates.db')
        cursor = conn.cursor()

        cursor.execute("SELECT timestamp, rate FROM exchange_rates ORDER BY timestamp DESC LIMIT 1")
        row = cursor.fetchone()

        if row:
            timestamp, rate = row

            workbook = openpyxl.Workbook()
            worksheet = workbook.active
            worksheet['A1'] = 'Час'
            worksheet['B1'] = 'Курс'
            worksheet.append([timestamp, rate])

            file_path = f'exchange_rate_{timestamp}.xlsx'
            workbook.save(file_path)

            # Відправлення XLSX-файлу користувачеві
            bot.send_document(chat_id, open(file_path, 'rb'))

            # Оновлення бази даних з поточним часом
            save_to_database(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rate)
    except sqlite3.Error as e:
        logging.error(f"Помилка при роботі з базою даних: {e}")
    except telebot.apihelper.ApiException as e:
        logging.error(f"Помилка при відправленні курсу: {e}")
    except Exception as e:
        logging.error(f"Сталася помилка: {e}")
    finally:
        conn.close()


def schedule_job():
    """
    Функція для обмеження регулярного оновлення курсу.
    """
    schedule.every().hour.do(parse_exchange_rate)

def start_telegram_bot():
    """
    Функція для запуску Telegram-бота.
    """
    @bot.message_handler(commands=['get_exchange_rate'])
    def handle_get_exchange_rate(message):
        send_exchange_rate(bot, message.chat.id)

    bot.polling()

if __name__ == "__main__":
    schedule_job()
    start_telegram_bot()

