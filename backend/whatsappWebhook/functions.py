import requests
import json

def send_message(message, phone_number):
    WHATSAPP_BUSINESS_PHONE_NUMBER_ID = "600100246511541"
    AUTH_TOKEN = "EAAJJmhOHpsUBOzVaTEpK1tGuxs7uzVqOZAvVh9PgZCoNDpPPZADKKmvGoMiTbeiYaXZBaredebs6MwSqsQooKr43AeJmQk00PfWjgZBOiv8z9vXF9EZAcVSGujXZAhHZAwIZALVzNvyodUbnxfVfN3wPmxZBDusFCn9ebpXyZAD4Y4xqGYJWsK2xK0yGuvViEsS8tDaPEl9brV9ijWIu97XaV4QxEl2EZC2ZAjfAo4d0ZD"
    body = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": phone_number,
    "type": "text",
    "text": { 
        "preview_url": True,
        "body": message,
        }
    }
    response = requests.post(f"https://graph.facebook.com/v21.0/{WHATSAPP_BUSINESS_PHONE_NUMBER_ID}/messages", data=json.dumps(body), headers={"Content-Type": "application/json","Authorization": f"Bearer {AUTH_TOKEN}"})    
    print('send_message RESPONSE>>>>', response.reason)
    
def handle_message(message):
    message=message[0]
    print(message, 'message>>>>')
    # Assuming the message is a text message
    if message['type'] == 'text':
        # Extract the phone number from the sender
        phone_number = message['from']
        # Extract the actual message content
        content = message['text']['body']
        # Perform any necessary actions based on the content
        if 'hi' in content.lower():
            send_message(f'Hello from Delenee! How can I help you?', phone_number)
        elif 'bye' in content.lower():
            send_message('Goodbye from Delenee!', phone_number)
        else:
            send_message(f'I didn\'t understand that. Please try again.', phone_number)
            
def handle_status(status, recipient_id):
    print(f'STATUS UPDATE: Message {status} by {recipient_id}')