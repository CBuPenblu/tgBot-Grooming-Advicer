import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('7116024501:AAFX4ufUkHwBqdL9HQaikNI-i2w6Ctxj0jQ')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Hi, I am chat bot that will advice you about your pet grooming')
    reminder_thread = threading.Thread(target=sent_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['fact'])
def fact_message(message):
    list = ["Pet grooming includes services such as bathing, brushing, clipping nails, and trimming fur to keep pets clean and healthy.",
            "Regular grooming can help prevent skin infections, matting, and other health issues in pets.",
            "Some grooming salons offer additional services like teeth cleaning, ear cleaning, and flea and tick treatments.",
            "Grooming can also help identify any lumps, bumps, or abnormalities on your pet's skin that may require veterinary attention.",
            "Different breeds require different grooming techniques and tools, so it's important to find a groomer who is knowledgeable about your pet's specific needs.",
            "Some pets may be anxious or fearful about grooming, so it's important to find a groomer who is patient and experienced in handling nervous animals.",
            "Regular grooming can also help reduce shedding and minimize the amount of pet hair in your home",
            "Grooming can be a bonding experience for pet owners and their pets, as it provides an opportunity for physical touch and affection.",
            "Some pet grooming salons offer mobile grooming services, where the groomer comes to your home in a specially equipped van.",
            "In addition to traditional grooming services, some pet grooming salons also offer spa treatments such as aromatherapy baths, pawdi\cures, and fur dyeing."]
    random_fact = random.choice(list)
    bot.reply_to(message, f'One of the facts about pet grooming: {random_fact}')

def sent_reminders(chat_id):
    first_rem = "01:03"
    second_rem = "14:00"
    end_rem = "18:00"
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "Reminders - Make an appointment, its time to groom your pet!")
            time.sleep(61)
        time.sleep(1)


bot.polling(none_stop=True)