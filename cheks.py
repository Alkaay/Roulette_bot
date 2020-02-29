from models import User, Text, Bet

def wright_comment(message):
    return User.get_state(message.chat.id) == 1