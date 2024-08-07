import os
import google.generativeai as genai

# Set your API key
api_key = "YOUR_API_KEY"

# Configure the Google Generative AI client
genai.configure(api_key=api_key)


def generate_response(command):
    try:
        # Create the model configuration
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        # Initialize the model
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            # safety_settings = Adjust safety settings
            # See https://ai.google.dev/gemini-api/docs/safety-settings
        )

        # Generate content
        response = model.generate_content(
            f"You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give pointwise, short, and simple responses, please. {command}"
        )

        return response.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
