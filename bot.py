from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import web


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'wanni_bot',
    user = 'wanni',
    pw = 'wanni.2019',
    port = 3306
    )

#wanni_bot 
token = '658343220:AAHGBbO_T5tR6lMaSzt3Uxefo4IBdT7QwPo'


def start(bot, update):
    username = update.message.from_user.username
    update.message.reply_text('Hola, Quieres saber de enfermedades{} usa estos comandos:\n/info llave #busca_informacion'.format(username))

def help(bot, update):
    username = update.message.from_user.username
    update.message.reply_text('Hola {} usa estos comandos:\n/info llave #busca_informacion'.format(username))

def search(update):
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        id_enfermedad = (text[1]) # cast para convertir str a int
        print "Send info to {}".format(username)
        print "Key search {}".format(id_enfermedad)
        result = db.select('enfermedades', where='id_enfermedad=$id_enfermedad', vars=locals())[0]
        print result
        respuesta =  (result.nombre) + ", " + (result.causas) + ", " + (result.sintomas)
        
        update.message.reply_text('Hola {}\nEsta es la informacion que buscas:\n{}'.format(username, respuesta))
    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('La llave {} es incorreta'.format(id_enfermedad))

def info(bot, update):
    search(update)

def echo(bot, update):
    update.message.reply_text(update.message.text)
    print update.message.text
    print update.message.date
    print update.message.from_user
    print update.message.from_user.username
    
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

    
def main():
    
    try:
        print 'Wanni init token'
        
        updater = Updater(token)

        
        dp = updater.dispatcher

        print 'Wanni init dispatcher'

       
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("info", info))        

      
        dp.add_handler(MessageHandler(Filters.text, echo))

      
        dp.add_error_handler(error)

        
        updater.start_polling()

       
        print 'Wanni ready'
        updater.idle()
    except Exception as e:
        print "Error 100: ", e.message

if __name__ == '__main__':
    main()
