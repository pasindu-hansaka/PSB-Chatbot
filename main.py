name = input("Please enter your name: ")
print(f"Welcome to the PSB Academic Chatbot, {name}! How can I assist you today?")

question = input("Ask a question: ").lower().strip()
if question == "hello":
    print("Hello! How can I help you?")

elif question == "internship":
    print("The internship takes place in the 5th semester.")
else:
    print("Sorry, I don't understand your question yet.")