from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
import os

class OpenAI:
    """
    Static class containing LLM configurations and instances
    """
    

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
   
   
    
    @staticmethod
    def get_chat_model():
        return ChatOpenAI(
            model="gpt-4",
            openai_api_key=OpenAI.OPENAI_API_KEY,
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2
        )
    
    @staticmethod
    def get_embeddings_model():
        return OpenAIEmbeddings(
            model="text-embedding-ada-002",
            openai_api_key=OpenAI.OPENAI_API_KEY
        )
    
    @staticmethod
    def __get_whisper_model(model_size="base"):
        """
        Private method that returns a whisper model instance for speech recognition
        
        Args:
            model_size (str): Size of the whisper model ('tiny', 'base', 'small', 'medium', 'large')
            
        Returns:
            whisper.Whisper: A loaded whisper model instance
        """
        import whisper
        return whisper.load_model(model_size)

    @staticmethod
    def transcribe_audio(audio_path, model_size="base"):
        """
        Transcribes audio file using OpenAI's Whisper model
        
        Args:
            audio_path (str): Path to the audio file
            model_size (str): Size of the whisper model to use
            
        Returns:
            str: Transcribed text from the audio file
        """
        model = OpenAI.__get_whisper_model(model_size)
        return model.transcribe(audio_path, fp16=False)["text"].strip()