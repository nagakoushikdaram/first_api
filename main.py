from fastapi import FastAPI

app = FastAPI()

# This is the home page
@app.get("/")
def home():
    return "yeahhhh API is LIVEEE!"

# This is the endpoint that takes your input
@app.get("/chat")
def chat_endpoint(user_input: str = ""):
    if user_input.lower() == "hi":
        return "Hello Koushik!"
    
    # If they type anything else, we return something different
    return f"You said '{user_input}', but I am waiting for 'hi'."