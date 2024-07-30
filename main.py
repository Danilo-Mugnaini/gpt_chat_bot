import os
import openai

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
  print(
    "API key not found. Make sure it's set correctly in the environment variables."
  )
  exit(1)

openai.api_key = api_key

while True:
  question = input("\033[34mWhat is your question?\n\033[0m")

  if question.lower() == "exit":
    print("\033[31mGoodbye!\033[0m")
    break

  try:
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{
        "role":
        "system",
        "content":
        "You are a helpful assistant. Answer the given question."
      }, {
        "role": "user",
        "content": question
      }])
    print("\033[32m" + completion.choices[0].message.content + "\n")
  except openai.error.RateLimitError:
    print("Rate limit exceeded. Please check your plan and billing details.")
  except Exception as e:
    print(f"An error occurred: {e}")
