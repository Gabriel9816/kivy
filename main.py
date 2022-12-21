from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import AsyncImage
from kivy.app import App
from kivy.lang import Builder
import os
import random
import requests


end_ip = "http://192.168.0.191:5000"
user1 = None
user2 = None


class Manager(ScreenManager):
    pass


class Home(Screen):
    pass


""" class Chat(Screen):
  pass

class CameraClick(Screen):
  pass """


class MyApp(App):
    def build(self):
        self.file = Builder.load_file("main.kv")
        return self.file

    def new_conversation(self):
        request = requests.get(end_ip+"/new_conversation")
        json = request.json()
        room_key = json['path']
        self.file.get_screen(
            'home').ids['idsala'].text = f'Codigo da sala: {room_key}'
        return

    def join_room(self):
        cod_room = {"data": self.file.get_screen(
            'home').ids["inpt_codigo_room"].text}
        print(cod_room)
        response = requests.post(end_ip+"/join_room", json=cod_room)
        message = response.json()
        if message['message'] == True:
            print(message['message'])
        if message['message'] == False:
            self.file.get_screen(
                'home').ids['idsala'].text = f'codigo da sala inexistente'

    def capture(self):
        cod_room = self.file.get_screen('home').ids["inpt_codigo_room"].text
        user = "user2"
        print(cod_room)
        if user == "user1":
            camera = self.file.get_screen('camera').ids['camera']
            camera.export_to_png("user1.png")
            files = {
                "file": "/home/gabrielpclinux/Downloads/chat/static/upload/user1.png",
                "code_room": cod_room,
                "user": user
            }
        if user == "user2":
            camera = self.file.get_screen('camera').ids['camera']
            camera.export_to_png("user2.png")
            files = {
                "file": "/home/gabrielpclinux/Downloads/chat/static/upload/user2.png",
                "code_room": cod_room,
                "user": user
            }
        print(files)
        requests.post(end_ip+"/new_message", json=files)

    def capture(self):
        cod_room = self.file.get_screen('home').ids["inpt_codigo_room"].text
        user = "user2"
        print(cod_room)
        if user == "user1":
            camera = self.file.get_screen('home').ids['camera']
            camera.export_to_png("user1.png")
            files = {
                "file": "/home/gabrielpclinux/Downloads/chat/user1.png",
                "code_room": cod_room,
                "user": user
            }
        if user == "user2":
            camera = self.file.get_screen('home').ids['camera']
            camera.export_to_png("user2.png")
            files = {
                "file": "/home/gabrielpclinux/Downloads/chat/user2.png",
                "code_room": cod_room,
                "user": user
            }
        print(files)
        requests.post(end_ip+"/new_message", json=files)

    def get_message(self):
        request = requests.get(end_ip+"/get_message")
        json = request.json()
        room_key = json['path']
        print(room_key)
        self.file.get_screen('home').ids['imguser'].source = room_key


MyApp().run()
