from langchain_core.output_parsers import StrOutputParser

class Parser:
    @staticmethod
    def from_ai_message_to_string():
        """
        Creates a string output parser that converts AI messages to strings
        Returns:
            StrOutputParser: A parser that converts AI messages to strings
        """
        return StrOutputParser()