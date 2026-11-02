from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Location URL", validators=[DataRequired(), URL()])
    open_time = StringField("Opening time", validators=[DataRequired()])
    closing_time = StringField("Closing time", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee rating",
        choices=[(str(i), f"{i} ☕") for i in range(6)],
        validators=[DataRequired()],
    )

    wifi_rating = SelectField(
        "WiFi rating",
        choices=[(str(i), f"{i} 📶") for i in range(6)],
        validators=[DataRequired()],
    )

    power_rating = SelectField(
        "Power outlet rating",
        choices=[(str(i), f"{i} 🔌") for i in range(6)],
        validators=[DataRequired()],
    )
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open("cafe-data.csv", "a") as file:
            file.write(f"\n{form.cafe.data},"
                       f"{form.location.data},"
                       f"{form.open_time.data},"
                       f"{form.closing_time.data},"
                       f"{form.coffee_rating.data},"
                       f"{form.wifi_rating.data},"
                       f"{form.power_rating.data}")
        return redirect(url_for('cafes'))


    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run()
