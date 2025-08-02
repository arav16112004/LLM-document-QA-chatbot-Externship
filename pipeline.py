import os
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.llms import ChatMessage


GOOGLE_API_KEY = "AIzaSyCj6NEAxuosAQ1fxK5jAG66NNBzciE4UNM" 
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


llm = GoogleGenAI(
    model="gemini-2.5-flash",
    contents = "Facts about the world"  # Can also use "models/GoogleGenAI-pro" if preferred

)
def chatbot():
    messages = []

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        messages.append(ChatMessage(role="user", content=user_input))
        try:
            response = llm.chat(messages)
            messages.append(ChatMessage(role="assistant", content=response.message.content))
            print(f"Chatbot {response}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    chatbot()