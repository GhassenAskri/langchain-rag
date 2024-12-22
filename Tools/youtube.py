import yt_dlp
import os

class Youtube:

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'TempFiles/%(title)s.%(ext)s',  # Save in TempFile directory # Save file with video title
        'quiet': True  # Suppress output
    }

    def _create_file_path(filename, extension):
        """
        Create a file path with the given filename and extension.
        
        Args:
            filename (str): Base filename without extension
            extension (str): File extension (e.g., 'mp3', 'txt')
            
        Returns:
            str: Complete file path
        """
        return os.path.splitext(filename)[0] + f".{extension}"
    
    
    @staticmethod
    def download_youtube_audio(video_url):
        """
        Download a YouTube video and extract its audio.
        
        Args:
            video_url (str): The URL of the YouTube video.
            output_format (str): The desired audio format (e.g., 'mp3', 'm4a').
            
        Returns:
            str: Path to the downloaded audio file.
        """
        with yt_dlp.YoutubeDL(Youtube.ydl_opts) as ydl :
            info = ydl.extract_info(video_url, download=False)
            filename = ydl.prepare_filename(info)
            audio_file = Youtube._create_file_path(filename, 'mp3')
            transcription_file = Youtube._create_file_path(filename, 'txt')
            if not os.path.exists(audio_file):
                ydl.extract_info(video_url, download=True)
            return audio_file,transcription_file