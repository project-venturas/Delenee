import requests
import json




def post_message(message_body):
    WHATSAPP_BUSINESS_PHONE_NUMBER_ID = "600100246511541"
    AUTH_TOKEN = "EAAJJmhOHpsUBO9TgphJqMtVqhHMY061mgc6kJTR7P2XDnIVzPNeaqaBTH2Hs4qduebtDE191I8ECPINhjubIKwS4fiaZCICY84raW0ZC2xoEelZAkPdOxgq1QB93NZASsFuhfAAW0pZC47Jq1Y02EWn7bOTKsp63uzhhDs4Ak75nmY9VZBjveZACsg5WSIoioNwrcrtYitsRHCQtRp6HRNkcOdnQEPhVx3S6Rq4CwZDZD"
    response = requests.post(f"https://graph.facebook.com/v21.0/{WHATSAPP_BUSINESS_PHONE_NUMBER_ID}/messages", data=json.dumps(message_body), headers={"Content-Type": "application/json","Authorization": f"Bearer {AUTH_TOKEN}"})    
    print('send_message RESPONSE>>>>', response.reason, response.json())


def send_text_message(message, phone_number):   
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
    post_message(body)
    

def send_interactive_reply_button_message(text_message, button_list, phone_number):
    body = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": phone_number,
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {
                    "text": text_message
                    },
                    "action": {
                    "buttons": button_list
                    }
                 }
            }
    
    post_message(body)

def send_interactive_list_message(text_message, button_title, button_list, phone_number):
    body = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": phone_number,
                "type": "interactive",
                "interactive": {
                    "type": "list",
                    "body": {
                    "text": text_message
                    },
                    "action": {
                    "button": button_title,
                    "sections": button_list
                    }
                 }
            }
    
    post_message(body)

    

def handle_message(message):
    message=message[0]
    print(message, 'message>>>>')
    phone_number = message['from']
    # Assuming the message is a text message
    if message['type'] == 'text':
        # Extract the actual message content
        content = message['text']['body']
        # Perform any necessary actions based on the content
        if 'hi' in content.lower():
            button_list = [
                        {
                        "type": "reply",
                        "reply": {
                            "id": "place_order",
                            "title": "Place order"
                            }
                        },
                        {
                        "type": "reply",
                        "reply": {
                            "id": "view_order_status",
                            "title": "View orders"
                            }
                        }
                    ]
            send_interactive_reply_button_message("Hello, How can I help you!",button_list, phone_number)
        
        
        elif 'bye' in content.lower():
            send_text_message('Goodbye from Delenee!', phone_number)
        else:
            send_text_message(f'I didn\'t understand that. Please try again.', phone_number)
            
            
    elif message['type'] == 'interactive':
        if message['interactive']['type'] == 'button_reply':
            if message['interactive']['button_reply']['id'] == 'place_order':
                distributor_list =  [
                    {
                    "title": "Registered with you",
                    "rows": [
                        {
                        "id": "SECTION_1_ROW_1_ID",
                        "title": "SLV Distributors",
                        "description": "(HUL products)"
                        },
                        {
                        "id": "SECTION_1_ROW_2_ID",
                        "title": "RAM Agency",
                        "description": "(Cipla products)"
                        }
                    ]
                    },
                    {
                    "title": "Others near you",
                    "rows": [
                        {
                        "id": "SECTION_2_ROW_1_ID",
                        "title": "Manju Enterprises",
                        "description": "(Deals with Godrej products)"
                        },
                        {
                        "id": "SECTION_2_ROW_2_ID",
                        "title": "SRS Enterprises",
                        "description": "Generic medicines"
                        }
                    ]
                    }
                ]
                send_interactive_list_message('Please select a distributor to place an order', 'Choose Distributor', distributor_list, phone_number)
            elif message['interactive']['button_reply']['id'] == 'view_order_status':
                send_text_message('View order status', phone_number)
            else:
                send_text_message('Invalid option', phone_number)
            
        if message['interactive']['type'] == 'list_reply':
            if message['interactive']['button_reply']['id'] == 'SECTION_1_ROW_1_ID':
                distributor_list =  [
                    {
                    "title": "Registered with you",
                    "rows": [
                        {
                        "id": "SECTION_1_ROW_1_ID",
                        "title": "SLV Distributors",
                        "description": "(HUL products)"
                        },
                        {
                        "id": "SECTION_1_ROW_2_ID",
                        "title": "RAM Agency",
                        "description": "(Cipla products)"
                        }
                    ]
                    },
                    {
                    "title": "Others near you",
                    "rows": [
                        {
                        "id": "SECTION_2_ROW_1_ID",
                        "title": "Manju Enterprises",
                        "description": "(Deals with Godrej products)"
                        },
                        {
                        "id": "SECTION_2_ROW_2_ID",
                        "title": "SRS Enterprises",
                        "description": "Generic medicines"
                        }
                    ]
                    }
                ]
                send_interactive_list_message('Please select a distributor to place an order', 'Choose Distributor', distributor_list, phone_number)
            
            
            
            
def handle_status(status, recipient_id):
    print(f'STATUS UPDATE: Message {status} by {recipient_id}')