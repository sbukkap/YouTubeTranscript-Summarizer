from flask import Flask,redirect,abort,render_template,request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
# define a variable to hold you app
app = Flask(__name__)

# define your resource endpoints
@app.route('/home')
def index():
    return render_template('sample1.html')
@app.route('/verify',methods=['POST','GET'])
def verify():
    if request.method == 'POST':
        name = request.form['name']
        id = name.split("=")[1]
        return redirect(f"/transcript/{id}")
@app.route('/transcript/<id>')
def trancript_summarizer(id):
    transcript = YouTubeTranscriptApi.get_transcript(id)
    result = ''
    for i in transcript:
        result += ' ' + i['text']
    summarizer = pipeline("summarization")
    num_iters = int(len(result)/1000)
    summarized_text = []
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        out = summarizer(result[start:end],min_length = 130)
        out = out[0]
        out = out['summary_text']
        summarized_text.append(out)
    final_text=''
    for i in summarized_text:
        final_text+=i
        final_text+=' '
    return redirect(f"/display/{final_text}")
@app.route('/display/<final_text>')
def display(final_text):
    return render_template("display.html",text=final_text)



# server the app when this file is run
if __name__ == '__main__':
    app.run(debug=True)
