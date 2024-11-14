from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# 업로드된 파일을 저장할 폴더 경로
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # uploads 폴더가 없으면 생성합니다.
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'musicFile' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['musicFile']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)  # 파일을 서버에 저장합니다.

    # 테스트 응답
    return jsonify({"message": "File uploaded successfully", "filename": file.filename})

if __name__ == "__main__":
    app.run(debug=True)