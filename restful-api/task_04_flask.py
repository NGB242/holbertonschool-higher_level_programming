#!/usr/bin/env python3
from flask import Flask, jsonify, request
"""
Instanciation d'un serveur web Flask
"""
app = Flask(__name__)

"""
Dictionnaire pour stocker les utilisateurs en mémoire
"""
users = { "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

"""
Définition d'une route pour l'URL racine ("/")
"""
@app.route("/")
def home():
    return "Welcome to the Flask API!"

"""
Route pour servir des données JSON
"""
@app.route("/data")
def data():
usernames = list(users.keys())
return jsonify(usernames)

"""
Route pour vérifier le statut de l'API
"""
@app.route("/status")
def status():
    return "OK"

"""
Route pour obtenir les informations d'un utilisateur spécifique
"""
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
    return jsonify(user)
    else:
    return jsonify({"error": "User not found"}), 404

"""
Route pour ajouter un nouvel utilisateur via une requête POST
"""
@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    username = user_data.get("username")
    
    if username in users:
        return jsonify({"error": "User already exists"}), 400

users[username] = 
    "name": user_data.get("name"),
    "age": user_data.get("age"),
    "city": user_data.get("city")
    
    return jsonify({"message": "User added successfully", "user": users[username]}), 201

"""
Exécution du serveur de développement Flask
"""
if __name__ == "__main__":
    app.run()
