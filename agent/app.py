import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    goal = input('What is your goal for this agent ? ')
    system_message = f"You are Sherlock-X, the world's smartest detective AI. Every question is a mystery waiting to be solved. You analyze clues, connect hidden patterns, and reason step by step before reaching a conclusion. Whether the user asks about science, history, programming, math, or everyday problems, treat each request like a detective case. Ask insightful questions when evidence is missing, challenge weak assumptions politely, and explain your deductions in a clear and engaging way. Stay calm, clever, and observant, but never invent evidence or facts. If information is incomplete, say exactly what is missing and build the most reasonable conclusion from the available clues. Your goal is {goal}."
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
            temperature=0,
           # system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(response)
        print('History:', history)
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()
#Lab 1
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

#Lab 2
# usage.input_tokens - the words/text the user sends to the chatbot 
# usage.output_tokens - the words/text the chatbot generates in response
# i put a long question to the chatbot and it answered me with a short answer. cuz  the max_tokens is set to 50 and its for the output tokens.
# the temperature controls the creativity of the chatbot's responses so a higher temperature will result in more creative and varied responses, while a lower temperature will result in more focused and deterministic responses thats why the bot was so creative and friendly in its answers when the temperature was set to 1 but when it was set to 0, it was more focused and deterministic
#there are 6 messages, because every turn contains one user message and one assistant response.
#because the API does not remember previous messages by itself. we must send the full history every time so the chatbot can understand the conversation and answer based on previous messages.

#lab 3
#refliction:
#1-tokens are like mobile data every message I send and every reply from the chatbot uses more tokens, just like every video or website uses more mobile data the longer the conversation continues, the more tokens are used and the higher the cost becomes.
#2-history.append({"role": "user", "content": user_input}) the AI would not receive my new message, so it would not know what I asked alsoThe input tokens would not include my latest message because it wasn’t sent.
#3-The chatbot stopped responding after I ran the program. First  i thought there was a problem with the API but I forgot to save the updated file.
#refliction:
#1- the system massege is like cake ingredients, it sets the tone and rules for the conversation, guiding the AI's behavior and responses. it's invisible to the user like the ingredients in a cake, but it shapes how the AI interacts with them. it helps the AI understand its role and how to respond appropriately to the user's requests.
#2- if i dleted system=system_message the AI would not know its role or how to respond appropriately, leading to confusion and irrelevant answers. the system message is crucial for guiding the AI's behavior and ensuring it provides helpful and contextually appropriate responses.And when i run the agent without the system massage, the AI's responses were less relevant .
#3- i didn't have any errors.