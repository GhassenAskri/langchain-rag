from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings

class OpenAI:
    """
    Static class containing LLM configurations and instances
    """
    
    # Your OpenAI API key - Consider moving this to environment variables
    OPENAI_API_KEY = "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"
    
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