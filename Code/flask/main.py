import os
import pytesseract
import speech_recognition as s_r
from PIL import Image
from flask import Flask, render_template, request, redirect
from googletrans import Translator
from langdetect import detect

app = Flask(__name__)

# image to translate
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, '/uploads/')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def ocr_core(filename):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename))
    return text


@app.route('/')
def homes():
    return render_template("home.html")


@app.route('/image', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', msg='No file')
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            text3 = ocr_core(file)
            if detect(text3) == 'te':
                translator = Translator()
                translation = translator.translate(text3, src='te', dest='en')
                translator1 = Translator()
                translation1 = translator1.translate(translation.text, src='en', dest='hi')
            elif detect(text3) != 'te':
                translator = Translator()
                translation = translator.translate(text3, src=detect(text3), dest='te')
                translator1 = Translator()
                translation1 = translator1.translate(translation.text, src='te', dest='hi')
            else:
                translation1 = "ERROR TRY AGAIN"
            return render_template('upload.html', msg='CODE-MIXING TRANSLATOR',
                                   extracted=translation1.text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    else:
        return render_template('upload.html')


# wav file to translate
@app.route("/file", methods=["GET", "POST"])
def index():
    translation1 = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = s_r.Recognizer()
            audioFile = s_r.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            text2 = str(recognizer.recognize_google(data, key=None))
            if detect(text2) == 'te':
                translator = Translator()
                translation = translator.translate(text2, src='te', dest='en')
                translator1 = Translator()
                translation1 = translator1.translate(translation.text, src='en', dest='hi')
                translation1 = translation1.text
            elif detect(text2) != 'te':
                translator = Translator()
                translation = translator.translate(text2, src='en', dest='te')
                translator1 = Translator()
                translation1 = translator1.translate(translation.text, src='te', dest='hi')
                translation1 = translation1.text
            else:
                translation1 = "ERROR TRY AGAIN"

    return render_template('audio.html', transcript=translation1)


# audio to translate

@app.route('/audio')
def index1():
    return render_template('file.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    global translation1
    if request.method == 'POST':
        text1 = str(request.form.getlist('Name'))
        text1 = text1.replace('[', '')
        text1 = text1.replace(']', '')
        if detect(text1) == 'te':
            translator = Translator()
            translation = translator.translate(text1, src='te', dest='en')
            translator1 = Translator()
            translation1 = translator1.translate(translation.text, src='en', dest='hi')
        elif detect(text1) != 'te':
            translator = Translator()
            translation = translator.translate(text1, src='en', dest='te')
            translator1 = Translator()
            translation1 = translator1.translate(translation.text, src='te', dest='hi')
        else:
            translation1 = "ERROR TRY AGAIN"
    return render_template("result.html", result=translation1.text)


# text to translate

@app.route("/text")
def customer():
    return render_template('text.html')


@app.route('/success', methods=['POST', 'GET'])
def home():
    global translation1
    translator = Translator()
    if request.method == 'POST':
        text = str(request.form.getlist("name"))
        text = text.replace('[','')
        text = text.replace(']','')
        if detect(str(text)) == 'te':
            translator = Translator()
            translation = translator.translate(str(text), src='te', dest='en')
            translator1 = Translator()
            translation1 = translator1.translate(translation.text, src='en', dest='hi')
        elif detect(str(text)) != 'te':
            translator = Translator()
            translation = translator.translate(str(text), src='en', dest='te')
            translator1 = Translator()
            translation1 = translator1.translate(translation.text, src='te', dest='hi')
        else:
            translation1 = "ERROR TRY AGAIN"
    return render_template("result_data.html", result=translation1.text)


if __name__ == '__main__':
    app.run(debug=True)
