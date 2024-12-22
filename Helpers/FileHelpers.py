class FileHelpers:
    @staticmethod
    def write_to_file(transcriptionPath: str, content: str) -> None:
        """
        Write content to a file, creating the TempFiles directory if it doesn't exist.
        
        Args:
            filename (str): The name/path of the file to write to
            content (str): The content to write to the file
            
        Returns:
            None
        """
        try:
            with open(transcriptionPath, "w") as file:
                file.write(content)
        except Exception as e:
            raise Exception(f"Error writing to file {transcriptionPath}: {str(e)}") 