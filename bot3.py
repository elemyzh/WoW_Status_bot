import requests
import telebot


#3. Configura tu bot de Telegram con PyTelegramBotAPI:

API_TOKEN = '6342601545:AAEBTt-f9JlgLOLOee_xVADM8W-vsV2H9KQ'
bot = telebot.TeleBot(API_TOKEN)


#4. Define el comando que activará la consulta a la API. En este caso, utilizaremos /mop como ejemplo:

@bot.message_handler(commands=['mop'])
def handle_mop_command(message):
    # Aquí es donde realizarás la petición a la API
    response = requests.get('https://api.rogwow.com/realm/mop/status/v3/')
    
    # Accede a los datos de la respuesta de la API y envía la información al grupo de Telegram
    data = response.json()

     # Obtiene la información de la API
    realm_status = data['realm_status']
    realm_characters = data['realm_characters']
    alliance = realm_characters['alliance']
    horde = realm_characters['horde']
    realm_max_characters = data['realm_max_characters']
    realm_diff = data['realm_diff']



    #bot.send_message(message.chat.id, f'Realm Characters:\nAlliance: {alliance}\nHorde: {horde}\nRealm Max Characters: {realm_max_characters}\nRealm Diff: {realm_diff}\nrealm_status: {realm_status}')
    bot.send_message(message.chat.id, f'\nServidor MoP: {realm_status}\nPj Alianza: {alliance}\nPj Horda: {horde}\nLatencia Mundo: {realm_diff}')


#5. Finalmente, inicia el bot para que esté listo para responder a los comandos de Telegram:

if __name__ == '__main__':
    bot.polling()
