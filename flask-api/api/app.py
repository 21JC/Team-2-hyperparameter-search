from flask import Flask, request, jsonify, Response
import mysql.connector
import uuid
import json


app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database=""
)
mycursor = mydb.cursor()

@app.route('/updateDB', methods=['GET', 'POST'])
def updateDatabase():
    data = request.json
    study_name = data['study-name']
    search_space_hyperparamter = data['search-space-hyperparameter']
    search_space_solver = data['search-space-solver']
    hyperparameter = data['hyperparameter']
    solver = data['solver']
    stopping_criteria = data['stopping-criteria']
    number_trials = data['num-updates']
    trial_id = str(uuid.uuid4())
    performance = data['performance']
    sql = "INSERT INTO tuneDatabase(study_name, search_space_hyperparamter, search_space_solver, hyperparameter, solver, stopping_criteria, number_trials, trial_id, performance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    value = (study_name, search_space_hyperparamter, search_space_solver, hyperparameter, solver, stopping_criteria, number_trials, trial_id , performance)
    mycursor.execute(sql, value)
    mydb.commit()

@app.route('/getBestStudy', methods=['GET', 'POST'])
def getBestStudy():
  data = request.json
  study_name = data['study-name']
  sql = "SELECT hyperparameter, solver, performance FROM tuneDatabase WHERE study_name = '" + study_name + "' ORDER BY performance DESC LIMIT 1;" 
  mycursor.execute(sql)
  best = mycursor.fetchall()[0]
  hyperparameter = best[0]
  solver = best[1]
  performance = best[2]
  return jsonify({"hyperparameter": hyperparameter, "solver": solver, "performance": performance})


if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
