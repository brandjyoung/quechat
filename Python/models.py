from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

# Define the Lesson model
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Unique ID for each lesson
    content = db.Column(db.Text, nullable=False) # Content of the lesson

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Unique ID for each quiz
    question = db.Column(db.Text, nullable=False) # Question text
    answer = db.Column(db.Text, nullable=False) # Correct answer
    lesson_id = db.Column(db.Integer, gb.ForeignKey('lesson.id'), nullable=False) #Foreign key to the lesson