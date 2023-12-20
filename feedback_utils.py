
# utils/feedback_utils.py
# This file contains utility functions for handling user feedback.
def gather_user_feedback(user_input, chatbot_response, feedback):
    with open('user_feedback.txt', 'a') as f:
        f.write(f"User Input: {user_input}\nBot Response: {chatbot_response}\nFeedback: {feedback}\n\n")
