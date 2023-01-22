from decouple import config
import openai

# Set the API key
openai.api_key = config("API")

# Use the ChatGPT model to generate text
model_engine = "text-davinci-002"

while model_engine == "text-davinci-002":
    prompt = input("ChatGPT: ")
    if prompt == "q": quit()
    completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.7)
    message = completion.choices[0].text
    print(message + "\n")