from flash import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DB config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lessons.db'
db.init_app(app)


#Create tables and insert sample data
with app.app_context():
    db.create_all()
    if not Lesson.query.first():
        lesson1 = Lesson(content="Lesson 1: Basic Spanish Greetings")
        db.session.add(lesson1)
        db.session.commit()


@app.route('/') # Define the home route
def home():
    return render_template('landing_page.html')

@app.route('/lessons', methods=['GET']) #define the route to get lessons
def get_lessons():
    lessons = Lesson.query.all()
    return jsonify([{'id': lesson.id, 'content': lesson.content} for lesson in lessons])

if __name__ == '_main_':
    app.run(debug=True)