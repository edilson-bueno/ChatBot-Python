import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
def chat_with_gpt(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Erro ao chamar a API]: {e}"
if __name__ == "__main__":
    print("Chat iniciado. Digite 'sair', 'exit' ou 'bye' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "bye"]:
            print("Chatbot: Até mais!")
            break
        resposta = chat_with_gpt(user_input)
        print("Chatbot:", resposta)