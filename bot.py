
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

updater = Updater(TOKEN, use_context=True)


# обработка команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Я бот, который может подсказать погоду и новости. Напишите /help, чтобы узнать все мои команды.")

# обработка команды /help
def help(update, context):
    help_text = "Я могу выполнить следующие команды:\n\n"
    help_text += "/start - запуск бота\n"
    help_text += "/help - вывод всех команд\n"
    help_text += "/weather <город> - погода в указанном городе\n"
    help_text += "/news - последние новости\n"
    context.bot.send_message(chat_id=update.message.chat_id, text=help_text)

# обработка команды /weather
def weather(update, context):
    city = context.args[0]
    weather_api_key = os.environ['WEATHER_API_KEY']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}'
    response = requests.get(url)
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    weather_text = f'Погода в городе {city}: температура {temperature}°C, влажность {humidity}%'
    context.bot.send_message(chat_id=update.message.chat_id, text=weather_text)

# обработка команды /news
def news(update, context):
    news_api_key = os.environ['NEWS_API_KEY']
    url = f'https://newsapi.org/v2/top-headlines?country=ru&apiKey={news_api_key}'
    response = requests.get(url)
    news_data = response.json()
    articles = news_data['articles']
    news_text = ''
    for article in articles:
        news_text += f"\n{article['title']}\n{article['url']}\n"
    context.bot.send
git push origin main
