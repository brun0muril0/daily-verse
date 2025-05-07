import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def get_env_variable(var_name: str) -> str:
    value = os.getenv(var_name)
    if not value:
        raise EnvironmentError(f"A variável de ambiente '{var_name}' não está definida.")
    return value

def get_random_verse() -> dict:
    try:
        response = requests.get('https://bible-api.com/data/almeida/random', timeout=10)
        response.raise_for_status()
        data = response.json()
        return data['random_verse']
    except (requests.RequestException, KeyError) as e:
        raise RuntimeError(f"Erro ao obter versículo: {e}")

def format_message(verse: dict) -> str:
    return (
        "📖 *Versículo do Dia* 📖\n\n"
        f"_{verse['text'].strip()}_\n\n"
        f"📚 *{verse['book']}* {verse['chapter']}:{verse['verse']}\n"
        f"📅 {datetime.now().strftime('%d/%m/%Y')}"
    )

def get_recipient_numbers() -> list:
    raw_numbers = get_env_variable('RECIPIENT_NUMBERS')
    return [number.strip() for number in raw_numbers.split(',') if number.strip()]

def send_whatsapp_message(body: str, recipients: list) -> None:
    client = Client(get_env_variable('TWILIO_ACCOUNT_SID'), get_env_variable('TWILIO_AUTH_TOKEN'))
    for number in recipients:
        message = client.messages.create(
            body=body,
            from_=get_env_variable('TWILIO_WHATSAPP_NUMBER'),
            to=number
        )
        print(f"✅ Mensagem enviada para {number}! SID: {message.sid}")

def main():
    print("🔄 Buscando versículo aleatório...")
    verse = get_random_verse()
    message_body = format_message(verse)
    recipients = get_recipient_numbers()
    print(f"📤 Enviando mensagem para {len(recipients)} número(s)...")
    send_whatsapp_message(message_body, recipients)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")
