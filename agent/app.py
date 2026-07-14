import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "You are Nova, a helpful, friendly, and knowledgeable AI assistant. Your goal is to provide accurate, clear, and useful answers to questions on any topic. You can help with education, science, technology, programming, mathematics, history, languages, writing, brainstorming, travel, health information, business, and everyday life."
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
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(response)
        print('History:', history)
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
#Lab 2
# usage.input_tokens - the words/text the user sends to the chatbot 
# usage.output_tokens - the words/text the chatbot generates in response
# i put a long question to the chatbot and it answered me with a short answer. cuz  the max_tokens is set to 50 and its for the output tokens.
# the temperature controls the creativity of the chatbot's responses so a higher temperature will result in more creative and varied responses, while a lower temperature will result in more focused and deterministic responses thats why the bot was so creative and friendly in its answers when the temperature was set to 1 but when it was set to 0, it was more focused and deterministic
#there are 6 messages, because every turn contains one user message and one assistant response.
#because the API does not remember previous messages by itself. we must send the full history every time so the chatbot can understand the conversation and answer based on previous messages.
#refliction:
#1-tokens are like mobile data every message I send and every reply from the chatbot uses more tokens, just like every video or website uses more mobile data the longer the conversation continues, the more tokens are used and the higher the cost becomes.
#2-history.append({"role": "user", "content": user_input}) the AI would not receive my new message, so it would not know what I asked alsoThe input tokens would not include my latest message because it wasn’t sent.
#3-The chatbot stopped responding after I ran the program. First  i thought there was a problem with the API but I forgot to save the updated file.