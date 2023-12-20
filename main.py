
# main.py
# This file contains the main execution script.
from chatbot.chatbot import Chatbot
from chatbot.adapter import LogicAdapter
import time

if __name__ == "__main__":
    chatbot_instance = Chatbot()

    while True:
        user_input = input("User: ")
        chatbot_instance.handle_user_input(user_input)
        time.sleep(1)
