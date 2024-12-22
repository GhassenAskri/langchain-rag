from langchain.prompts import ChatPromptTemplate

class Prompts:
    """
    Static class containing all prompt templates used in the application
    """
    
    @staticmethod
    def get_video_content_qa_prompt():
        template = """
        Answer the question based on the context below, 
        If you can't answer the question, reply "I don't know" 

        Context : {context}
        Question : {question}
        """
        return ChatPromptTemplate.from_template(template)
    
    # You can add more prompt methods here as needed 