import pyautogui
import pyperclip
import subprocess
import time
import google.generativeai as genai

# Set your API key
api_key = "YOUR_API_KEY"

# Configure the Google Generative AI client
genai.configure(api_key=api_key)

# Open the application using subprocess
subprocess.Popen(["flatpak", "run", "io.github.mimbrero.WhatsAppDesktop"])

# Pause for a few seconds to ensure the application has time to open
time.sleep(10)

# Drag from (691, 157) to (1830, 1059)
pyautogui.moveTo(x=691, y=157)
pyautogui.dragTo(x=1830, y=1059, duration=2)  # Adjust duration if needed

# Copy the selected text to clipboard
pyautogui.hotkey("ctrl", "c")

# Wait a moment to ensure the clipboard operation completes
time.sleep(1)

# Retrieve the copied text from clipboard
Chat_History = pyperclip.paste()

# Print the copied text to verify
print("Copied Text:", Chat_History)


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
            f"You are a person named Sandy who speaks Hindi, Gujarati, as well as English. You are from India and are a coder. Analyze the chat history and respond like this: {command}"
        )

        return response.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def respond_if_last_message_is_not_from_sandy(chat_text):
    # Split the chat text into lines
    lines = chat_text.strip().split("\n")

    if not lines:
        return "No messages to process."

    # Extract the last message line
    last_line = lines[-1]

    # Check if the last message is not from "Sandy"
    if last_line.startswith("[") and "Sandy:" not in last_line:
        print("Responding to the last message since it's not from Sandy.")

        # Open the application using subprocess
        subprocess.Popen(["flatpak", "run", "io.github.mimbrero.WhatsAppDesktop"])

        # Pause for a few seconds to ensure the application has time to open
        time.sleep(10)

        # Click at (902, 1032)
        pyautogui.click(x=902, y=1032)

        # Type out the copied text
        pyautogui.write(Responce)

        # Press Enter
        pyautogui.press("enter")
    else:
        return "Last message is from Sandy or there are no messages."


# Generate a response based on the copied chat history
Responce = generate_response(Chat_History)

print(Responce)

# Respond if the last message is not from Sandy
respond_if_last_message_is_not_from_sandy(Responce)
