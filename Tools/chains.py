from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from Tools.prompts import Prompts
from Tools.openai import OpenAI
from Tools.parsers import Parser

class Chains:

    chain = None

    @classmethod
    def setup(cls, retriever):
        """
        Sets up the chain with the given retriever
        
        Args:
            retriever: The retriever to use for context
            
        Returns:
            self for method chaining
        """
        cls.chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | Prompts.get_video_content_qa_prompt()
            | OpenAI.get_chat_model() 
            | Parser.from_ai_message_to_string()
        )
        return cls
    
    @classmethod
    def invoke(cls, question):
        """
        Invokes the chain with the given question
        
        Args:
            question: The question to ask
            
        Returns:
            self for method chaining
        """
        return  cls.chain.invoke(question)