# Jarvis - A Virtual Assistant 🤖

## Features ✨
- 🌐 Open websites (Google, GitHub, YouTube, etc.)
- 🎵 Play music from a predefined library
- 📰 Read the latest news headlines
- 💬 Process general commands using OpenAI

## Installation 🛠️
1. Install PortAudio:
    ```bash
    sudo apt-get install portaudio19-dev
    ```
2. Install Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Dependencies 📦
- `annotated-types==0.7.0`
- `anyio==4.4.0`
- `certifi==2024.7.4`
- `charset-normalizer==3.3.2`
- `click==8.1.7`
- `distro==1.9.0`
- `exceptiongroup==1.2.2`
- `gTTS==2.5.2`
- `h11==0.14.0`
- `httpcore==1.0.5`
- `httpx==0.27.0`
- `idna==3.7`
- `jiter==0.5.0`
- `openai==1.40.0`
- `PyAudio==0.2.14`
- `pydantic==2.8.2`
- `pydantic_core==2.20.1`
- `pygame==2.6.0`
- `pyttsx3==2.90`
- `requests==2.32.3`
- `sniffio==1.3.1`
- `SpeechRecognition==3.10.4`
- `tqdm==4.66.5`
- `typing_extensions==4.12.2`
- `urllib3==2.2.2`

## Usage 🚀
Run the project with:
```bash
python3 main.py 2> >(grep -v 'ALSA lib' >&2)
```

## Configuration 🔧
- **OpenAI API Key**: Store in environment variable or replace in code.
- **NewsAPI Key**: Replace in code.

## Music Library 🎵
- "alone"
- "london bridge is falling down"
- "no friends"
- "angel with shotgun"
- "i see your monster"
- "man without love"

## Example Commands 🎤
- "Open Google"
- "Open YouTube"
- "Play [song_name]"
- "Tell me the news"

## Notes 📝
- **Dependencies**:
    - `pyttsx3` for text-to-speech
    - `webbrowser` for opening web pages
    - `speech_recognition` for recognizing speech
    - `gTTS` for Google Text-to-Speech (paid)
    - `pygame` for playing audio
    - `requests` for HTTP requests
    - `OpenAI` for processing commands (paid)
- **Suppress ALSA Errors**: Use `2> >(grep -v 'ALSA lib' >&2)`

## Licensing 📜
- Open-source. Contributions welcome!

## Acknowledgments 🙏
- OpenAI for their API.
- NewsAPI for news data.
- Various open-source libraries.

