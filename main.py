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


class Gerenciador(ScreenManager):
    pass


class Home(Screen):
    pass


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
        user = "user1"
        print(cod_room)
        if user == "user1":
            camera = self.file.get_screen('home').ids['camera']
            camera.export_to_png("/sdcard/user1.png")
            data = {"code_room": cod_room, "user": user}
            print(data)
            file = {'file': open('/sdcard/user1.png', 'rb')}
            requests.post(end_ip+"/new_message", files=file, data=data)
        if user == "user2":
            camera = self.file.get_screen('home').ids['camera']
            camera.export_to_png("/sdcard/user2.png")
            data = {"code_room": cod_room, "user": user}
            file = {'file': open('/sdcard/user2.png', 'rb')}
            requests.post(end_ip+"/new_message", files=file, data=data)

    def get_message(self):
        cod_room = {"cd_room": self.file.get_screen(
            'home').ids["inpt_codigo_room"].text}
        request = requests.post(end_ip+"/get_message", json=cod_room)
        json = request.json()
        room_key = json['path']
        self.file.get_screen('home').ids['imguser'].source = room_key


MyApp().run()
