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
- `cachetools==5.4.0`
- `certifi==2024.7.4`
- `charset-normalizer==3.3.2`
- `click==8.1.7`
- `distro==1.9.0`
- `exceptiongroup==1.2.2`
- `google-ai-generativelanguage==0.6.6`
- `google-api-core==2.19.1`
- `google-api-python-client==2.140.0`
- `google-auth==2.33.0`
- `google-auth-httplib2==0.2.0`
- `google-generativeai==0.7.2`
- `googleapis-common-protos==1.63.2`
- `grpcio==1.65.4`
- `grpcio-status==1.62.3`
- `gTTS==2.5.2`
- `h11==0.14.0`
- `httpcore==1.0.5`
- `httplib2==0.22.0`
- `httpx==0.27.0`
- `idna==3.7`
- `jiter==0.5.0`
- `proto-plus==1.24.0`
- `protobuf==4.25.4`
- `pyasn1==0.6.0`
- `pyasn1_modules==0.4.0`
- `PyAudio==0.2.14`
- `pydantic==2.8.2`
- `pydantic_core==2.20.1`
- `pygame==2.6.0`
- `pyparsing==3.1.2`
- `pyttsx3==2.90`
- `requests==2.32.3`
- `rsa==4.9`
- `sniffio==1.3.1`
- `SpeechRecognition==3.10.4`
- `tqdm==4.66.5`
- `typing_extensions==4.12.2`
- `uritemplate==4.1.1`
- `urllib3==2.2.2`

## Usage 🚀
Run the project with:
```bash
python3 main.py 2> >(grep -v 'ALSA lib' >&2)
```

## Configuration 🔧
- **OpenAI API Key**: Store in environment variable or replace in code.
- **NewsAPI Key**: Replace in code.
- **Google Generative AI Key**: Store in environment variable or replace in code.

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
    - `Google Generative AI` for advanced AI capabilities (paid)
- **Suppress ALSA Errors**: Use `python3 main.py 2> >(grep -v 'ALSA lib' >&2)`

## Licensing 📜
- Open-source. Contributions welcome!

## Acknowledgments 🙏
- OpenAI for their API.
- NewsAPI for news data.
- Google Generative AI for advanced AI capabilities.
- Various open-source libraries.
