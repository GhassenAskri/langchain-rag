from flask import Flask, request, jsonify
from langchain_openai import ChatOpenAI
from langchain.prompts import  ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from operator import itemgetter
import whisper


import yt_dlp
import os

app = Flask(__name__)

# Initialize the OpenAI LLM // https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html

llmEngine = ChatOpenAI(
    model="gpt-4o",
    openai_api_key = "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", 
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

template = """

Answer the question based on the context below, 
If you can't answer the question, reply "I don't know" 

Context : {context}
Question : {question}

"""

prompt = ChatPromptTemplate.from_template(template); 

translationPrompt = ChatPromptTemplate.from_template("translate{answer} to {language}")


parser = StrOutputParser()



#translationChain =( {"answer" : chain ,"language" : itemgetter("language")} | translationPrompt | llmEngine | parser)



url = "https://www.youtube.com/watch?v=BrsocJb-fAo&t=1574s"

embedding = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key="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")





def download_youtube_audio(video_url, output_format="mp3"):
    """
    Download a YouTube video and extract its audio.
    
    Args:
        video_url (str): The URL of the YouTube video.
        output_format (str): The desired audio format (e.g., 'mp3', 'm4a').
        
    Returns:
        str: Path to the downloaded audio file.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': output_format,
            'preferredquality': '192',
        }],
        'outtmpl': f'%(title)s.%(ext)s',  # Save file with video title
        'quiet': True  # Suppress output
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        filename = ydl.prepare_filename(info)
        audio_file = os.path.splitext(filename)[0] + f".{output_format}"
        return audio_file


audio_model = whisper.load_model("base")






@app.route('/process', methods=['POST'])
def process_text():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        if 'text' not in data:
            return jsonify({'error': 'No text field in request'}), 400
        
        # Get the input text
        question = data['text']
        url = data['url']

        audio =  download_youtube_audio(url)
        transcription = audio_model.transcribe(audio, fp16=False)["text"].strip()

        with open("transcription.txt", "w") as file:
            file.write(transcription)

        loader = TextLoader("transcription.txt")
        text_documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size= 1000, chunk_overlap=20)
        documents = text_splitter.split_documents(text_documents)
        vectorstore = DocArrayInMemorySearch.from_documents(documents, embedding)
        
        #setup = RunnableParallel(context= vectorstore.as_retreiver(), question = RunnablePassthrough())

        chain = (
            {"context": vectorstore.as_retriever(), "question": RunnablePassthrough()}
            | prompt
            | llmEngine 
            | parser
        ) 

        result= chain.invoke(question) 
        
        # Return the result
        return jsonify({
            'input': question,
            'output': result
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)