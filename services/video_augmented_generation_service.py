from Tools.youtube import Youtube
from Tools.openai import OpenAI
from Helpers.FileHelpers import FileHelpers
from Tools.splitters import Splitters
from Tools.inMemoryVectors import InMemoryVectorDb
from Tools.chains import Chains

class VideoAugmentedGenerationService:
    @staticmethod
    def answerToQuestionFromVideoTranscription(question: str, url: str) -> str:
        
        audioPath,transcriptionPath = Youtube.download_youtube_audio(url)

        
        transcription = OpenAI.transcribe_audio(audioPath)
        
        FileHelpers.write_to_file(transcriptionPath, transcription)
        
        documents = Splitters.load(transcriptionPath).splitUsingRecursiveCharacterTextSplitter(1000, 20)
        vectorstore = InMemoryVectorDb.search_from(documents)
        
        return Chains.setup(vectorstore.as_retriever()).invoke(question)