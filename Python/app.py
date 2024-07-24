from flash import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing_page.htm')

if __name__ == '_main_':
    app.run(debug=True)