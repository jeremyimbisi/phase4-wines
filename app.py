# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# db = SQLAlchemy()
# migrate = Migrate()

# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Adjust the database URI as needed
#     db.init_app(app)
#     migrate.init_app(app, db)
#     return app


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(128), nullable=False)
#     completed = db.Column(db.Boolean, default=False)

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json  # Assuming the request data is in JSON format
    title = data.get('title')
    if title:
        task = Task(title=title)
        db.session.add(task)
        db.session.commit()
        return jsonify({"message": "Wine added successfully"}), 201
    else:
        return jsonify({"message": "Title is required"}), 400

@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Wine deleted successfully"}), 200
    else:
        return jsonify({"message": "Wine not found"}), 404



if __name__ == '__main__':
    app.run(debug=True)
