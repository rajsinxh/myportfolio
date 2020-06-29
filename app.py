from flask import Flask , render_template,url_for,request,redirect
import csv

app = Flask(__name__)

@app.route('/')
def dirc():
	return render_template('index.html')

def write_to_csv(data):
	with open('database.csv',newline='', mode='a') as database:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		csv_writer=csv.writer(database ,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])
