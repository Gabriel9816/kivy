from flask import Flask, jsonify, request
import random
import os
from PIL import Image
import io

app = Flask(__name__)
PATH = "/home/gabriel/Downloads/apk/static/upload/"


@app.route("/new_conversation", methods=["GET"])
def new_conversation():
    room_key = random.randint(10, 100)
    os.mkdir(f"{PATH}{room_key}")
    path_folder = f'{PATH}{room_key}'
    print(path_folder)
    return jsonify(path=path_folder)


@app.route("/join_room", methods=["GET", "POST"])
def join_room():
    if request.method == "POST":
        cod_room = request.json["data"]
        print(cod_room)
        NEWPATH = f'{PATH}{cod_room}'
        if os.path.exists(NEWPATH):
            message = {"message": True}
            return jsonify(message)
        message = {"message": False}
        return jsonify(message)


@app.route("/new_message", methods=["POST"])
def new_message():
    path_picture = request.files['file']
    print(path_picture)
    code_room = request.form.get('code_room')
    user = request.form.get('user')
    print(user)
    if user == "user1":
        picture = Image.open(io.BytesIO(path_picture.stream.read()))
        path = "/home/gabriel/Downloads/apk/static/upload/" + \
            str(code_room)+"/"+str(user)+".png"
        picture.save(path)
    if user == "user2":
        picture = Image.open(io.BytesIO(path_picture.stream.read()))
        print(picture)
        path = "/home/gabriel/Downloads/apk/static/upload/" + \
            str(code_room)+"/"+str(user)+".png"
        picture.save(path)
    return


@app.route("/get_message", methods=["POST"])
def get_message():
    user = "user2"
    cod_room = request.json['cd_room']
    print(cod_room)
    if user == "user1":
        path = {
            "path": "/home/gabriel/Downloads/apk/static/upload/"+str(cod_room)+"/user2.png"
        }
        return jsonify(path)
    if user == "user2":
        path = {
            "path": "/home/gabriel/Downloads/apk/static/upload/"+str(cod_room)+"/user1.png"
        }
        return jsonify(path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
