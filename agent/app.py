import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Noor. You are a positive and supportive motivational coach. You encourage users to achieve their goals, stay confident, and build good habits while giving practical advice."
    # "Your name is Noor. You are an expert on the Harry Potter universe. You answer questions about Hogwarts, spells, magical creatures, and characters while staying in character as a Hogwarts professor."
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()
#challenge 2:
# can you sing? it said it cant but it can write a song for you.
#  do you know how to write a python function? it teaches you and answer your questions about python functions.
#can you explain  More advanced concepts? it answerd and explained about it.
#i didn't understand the first func? it answerd No problem! Let me break down the **default parameters function** more slowly.
#this chatbot is very helpful and friendly.  but the problem cuz it runs on the terminal and it is not user friendly.
#refliction:
# 1- My Al agent is like a friend who forgets every conversation after we stop talking. I have to remind it of everything we discussed before so it can continue helping me.
# 2-load_dotenv()-The program will probably fail because it cannot load the API key from the .env file.
#I got a 401 Unauthorized error when I ran the program. At first, I thought there was something wrong with my code, but the real problem was that my API key was missing or invalid. After fixing the API key, the program worked correctly.