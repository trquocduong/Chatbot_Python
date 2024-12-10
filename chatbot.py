import openai
from dotenv import load_dotenv
import os

# Nạp các biến môi trường từ file .env
load_dotenv()

# Lấy API key từ biến môi trường
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot_with_python(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    while True:
        # Nhập dữ liệu từ người dùng
        user = input('You: ')
        if user.lower() == 'bye':
            print('Chatbot: Goodbye')
            break
        # Gọi hàm chatbot và in kết quả
        response = chatbot_with_python(user)
        print('Chatbot:', response)
