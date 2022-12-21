from flask import Flask,jsonify,request
import random
import os
import json
import shutil

app = Flask(__name__)
PATH="/home/gabrielpclinux/Downloads/chat/static/upload"

@app.route("/new_conversation",methods=["GET"])
def new_conversation():
    room_key = random.randint(10,100)
    os.mkdir(f"{PATH}/{room_key}")
    path_folder = f'{PATH}{room_key}'
    print(path_folder)
    return jsonify(path=path_folder)

@app.route("/join_room",methods=["GET","POST"])
def join_room():
    if request.method =="POST":
        cod_room = request.json["data"]
        print(cod_room)
        NEWPATH = f'{PATH}/{cod_room}'
        if os.path.exists(NEWPATH):
            message = {"message":True}
            return jsonify(message)
        message = {"message":False}
        return jsonify(message)
    
@app.route("/new_message",methods=["POST"])
def new_message():
    path_picture = request.json["file"]
    code_room = request.json["code_room"]
    user = request.json["user"]
    print(user)
    if user =="user1":
        shutil.copy(
        path_picture,
        "/home/gabrielpclinux/Downloads/chat/static/upload/"+code_room)
    if user =="user2":
        shutil.copy(
        path_picture,
        "/home/gabrielpclinux/Downloads/chat/static/upload/"+code_room)
            
    return

@app.route("/get_message",methods=["GET"])
def get_message():
    user="user1"
    cod_room=92
    if user =="user1":
        path={
            "path":"/home/gabrielpclinux/Downloads/chat/static/upload/"+str(cod_room)+"/user2.png"
        }
        return jsonify(path)
    if user =="user2":
        path={
            "path":"/home/gabrielpclinux/Downloads/chat/static/upload/"+str(cod_room)+"/user1.png"
        }
        return jsonify(path)
    
    

if __name__=='__main__':
    app.run(debug=True)