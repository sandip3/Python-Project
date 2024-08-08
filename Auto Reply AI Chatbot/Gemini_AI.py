import os
import google.generativeai as genai

# Set your API key
api_key = "YOUR_API_KEY"

# Configure the Google Generative AI client
genai.configure(api_key=api_key)

chat = """
[12:26 AM, 8/5/2024] Jenil: https://ca.indeed.com/career-advice/resumes-cover-letters/writing-a-resume-with-no-experience
[12:26 AM, 8/5/2024] Sandy: But can you suggest some projects for beginners?
[12:26 AM, 8/5/2024] Jenil: Check the experience section
[12:28 AM, 8/5/2024] Jenil: Anything is fine...from creating simple to-do to full fledged webapp or mobile apps
[12:28 AM, 8/5/2024] Jenil: Whatever you feel like
[12:28 AM, 8/5/2024] Sandy: ok
[12:28 AM, 8/5/2024] Jenil: You can ask chatgpt or bing or whatever for the project ideas
[12:29 AM, 8/5/2024] Jenil: You can create something related to ai/ml as well
[12:29 AM, 8/5/2024] Jenil: If you are interested in that
[12:29 AM, 8/5/2024] Jenil: Whatever you're interested in..do that
[12:30 AM, 8/5/2024] Sandy: It's lot hard last time have creted it it took lo's of time and still not working
[12:30 AM, 8/5/2024] Sandy: just small portion is working
[12:31 AM, 8/5/2024] Jenil: Yaah... that's the thing...you have to invest your time in that
[12:31 AM, 8/5/2024] Jenil: So that way you get the experience
[12:31 AM, 8/5/2024] Jenil: Think of it as you are doing a job
[12:32 AM, 8/5/2024] Jenil: And they asked you to create that for the company
[12:32 AM, 8/5/2024] Sandy: Ok
[12:32 AM, 8/5/2024] Jenil:
"""


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
            f"You are person named sandip Who speaks hindi as well as english.he is from India and is a coder. you analyze chat history and respond like him {command}"
        )

        return response.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

reponce = generate_response(chat)

print(reponce)
