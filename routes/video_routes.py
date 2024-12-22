from flask import request, jsonify
from services.video_augmented_generation_service import VideoAugmentedGenerationService

def register_routes(app):

    @app.route('/process', methods=['POST'])
    def process_text():
        try:
            data = request.get_json()
            
            if 'text' not in data:
                return jsonify({'error': 'No text field in request'}), 400
            
            question = data['text']
            url = data['url']

            result = VideoAugmentedGenerationService.answerToQuestionFromVideoTranscription(
                question, 
                url
            )
        
            return jsonify({
                'input': question,
                'output': result
            })
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500 