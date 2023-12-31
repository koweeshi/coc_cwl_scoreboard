import pandas as pd
from flask import Flask, render_template
from datetime import date

month = date.today().strftime("%b-%Y")
app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'

@app.route('/') 
def scoreboard():
    df = pd.read_csv(f"{month}_Summary.csv")
    limited_data = df.head(25).to_dict(orient='records')  # First 15 rows
    full_data = df.to_dict(orient='records')  # All rows
    return render_template('scoreboard.html', limited_data=limited_data, full_data=full_data)
