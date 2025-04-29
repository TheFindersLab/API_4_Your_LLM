from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
import os
import dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the API key from environment variable
API_KEY = os.getenv("API_KEY")

app = FastAPI()

# Dependency to check for API key
def check_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY: 
        raise HTTPException(status_code=403, detail="Forbidden: Invalid API Key")
    return x_api_key

model = "llama2"  # Specify the model you want to use

@app.post("/generate")
def generate(prompt: str, x_api_key: str = Depends(check_api_key)):
    """
    Generate a response from the model using the provided prompt.
    """
    # Call the Ollama API to generate a response
    response = ollama.chat(model=model, message=[{"role": "user", "content": prompt}])
    
    # Return the generated response
    return {"response": response["message"]["content"]}