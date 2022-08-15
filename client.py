import os
import uuid
from flask import Flask, render_template, request
from server import Diarization

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_files():

    if not os.path.exists(app.config['UPLOAD_PATH']):
        os.makedirs(app.config['UPLOAD_PATH'])

    uploaded_files = request.files.getlist('file')
    for uploaded_file in uploaded_files:
        file_extension = os.path.splitext(uploaded_file.filename.lower())[-1]
        filename = str(uuid.uuid4()) + file_extension
        document_path = os.path.join(app.config['UPLOAD_PATH'], filename)
        uploaded_file.save(document_path)
        #if file_extension == '.m4a':
         # ffmpeg.input(document_path).output(filename[:-4]+'wav', format = 'wav', acodec = 'pcm_s16le', ac = 1, ar = '16k').overwrite_output().run()
        diar = Diarization(document_path)
        diar.predict()
        s = diar.file()

    return s