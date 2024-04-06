from flask import Flask, render_template

app = Flask(__name__)


culturals = [ {'title': 'dance'}, {'title': 'cultural'}, {'title': 'ted talks'}, {'title': 'singing'}, {'title': 'clasical dance'}]

eventdesc = {
    "dance":{ 'title':'dance', 'coordinator':'someone1', 'faculty':'faculty-name'},
    "cultural":{ 'title':'dance', 'coordinator':'someone1', 'faculty':'faculty-name'},
    "singing":{ 'title':'dance', 'coordinator':'someone1', 'faculty':'faculty-name'}
}



@app.route('/')
def home():
    return render_template('home.html', events = culturals)

@app.route('/event/<eventDetail>')
def eventDetails(eventDetail):
    return render_template('eventDetails.html', event = eventdesc[eventDetail])

if __name__ == "__main__":
    app.run(debug=True)