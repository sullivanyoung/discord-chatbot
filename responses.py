import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey beautiful <3'
    
    if p_message == 'roll':
        return str(random.randint(1, 6))
    
    if p_message == 'hello there':
        return 'GENERAL KENOBI'
    
    if p_message == '!help':
        return 'This is a help test message.'
    
    return 'I didn\'t understand what you said.'