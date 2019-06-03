chat_id = 800152701
from telegram.ext import Updater, MessageHandler, Filters

updater = Updater(token='858673203:AAEZ9ldakIPE3ZHYpJH8VgNIB3tbJ6hpZQw')
dispatcher = updater.dispatcher
updater.start_polling()

def handler(bot, update):
  text = update.message.text
  chat_id = update.message.chat_id

  if '강동구' in text:
    bot.send_photo(chat_id=chat_id, photo=open('img/gd.jpg', 'rb'))
    bot.send_message(chat_id=chat_id, text='의심지역이에요!                                                                                                     총 유동인구는 1193580이며 남성 : 579408, 여성 : 614173 입니다')
  elif '송파구' in text:
    bot.send_photo(chat_id=chat_id, photo=open('img/sp.jpg', 'rb'))
    bot.send_message(chat_id=chat_id, text='의심지역이에요!                                                                                                     총 유동인구는 1360461이며 남성 : 685860, 여성 : 674601 입니다')
  elif '강남구' in text:
    bot.send_photo(chat_id=chat_id, photo=open('img/gn.jpg', 'rb'))
    bot.send_message(chat_id=chat_id, text='위험지역이에요!                                                                                                     총 유동인구는 1372994이며 남성 : 685990, 여성 : 687003 입니다')
  else:
    bot.send_photo(chat_id=chat_id, photo=open('img/abc.jpg', 'rb'))
    bot.send_message(chat_id=chat_id, text='너의 힘으로 한번 찾아보세요')

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
