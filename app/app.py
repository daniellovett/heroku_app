from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///wine.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], {})

@app.route("/")
def home():
    with engine.connect() as conn:
        df = pd.read_sql('wines', conn)
        html = df.to_html()
    return html

if __name__ == "__main__":
    app.run()
