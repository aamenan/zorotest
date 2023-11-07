from flask import Flask, render_template, url_for
import pyodbc

app = Flask(__name__)
DSN = 'Driver={SQL Server};Server=DESKTOP-2B6AD73\\SQLEXPRESS;Database=zorotest;'
conn = pyodbc.connect(DSN)
cursor = conn.cursor()
# uid = <username>;
# pwd = <password>;

@app.route("/")
def connexion():
   return render_template('connexion.html')

@app.route("/accueil/")
def accueil():
   return render_template('accueil.html')

# supprimer page



#@app.route("/suppression")
#def enrSupprimer():
   #return render_template("enrSup.html")
   

if __name__ == "__main__":
    app.run(debug=True)