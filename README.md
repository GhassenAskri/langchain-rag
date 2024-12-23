# Youtube retreiver augmented genenration api 

A Flask api that expose a retreival augmented generation task based an audio transcription.

<img width="919" alt="image" src="https://github.com/user-attachments/assets/43caafe4-6fc6-4f3e-80f0-8dec670e5fab" />


## Features

- Download audio from YouTube videos in MP3 format
- Automatic file caching (prevents re-downloading the same video)
- Audio transcription support
- Ask openai llm a question based on the audio transcription as context 

## Installation

1. Install FFmpeg
    - **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html) and add to PATH
    - **Mac**: `brew install ffmpeg`
    - **Linux**: `sudo apt-get install ffmpeg`

2. Clone the repository:
```bash
git clone https://github.com/GhassenAskri/langchain-rag.git
```
3. Install the required dependencies:
```bash
pip install requirements
```
4. Set your openai key as environement variable
    - **Mac/Linux**: `export OPENAI_API_KEY='your-api-key'`
    - **Windows**: `set OPENAI_API_KEY=your-api-key`


## Dependencies

- yt-dlp: for YouTube video downloading
- FFmpeg: for audio processing (must be installed on your system)
- langchain/langchain.community for orchestrating and tooling llm models
- whisper openai transcription model
- openai embedding (transform a text to a vector)



