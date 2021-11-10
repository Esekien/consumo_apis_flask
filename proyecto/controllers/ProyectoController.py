from flask import Flask, request, redirect, url_for, flash, jsonify
from flask import Blueprint, render_template
import json
import requests

Route = Blueprint('Login',__name__)

class Loging():

    @Route.route('/',methods=['GET'])
    def index():
        url_api_pokemon = 'https://pokeapi.co/api/v2/pokemon/'
        url_api_rickandmorty = 'https://rickandmortyapi.com/api/character'
        url_api_gobierno = 'https://api.datos.gob.mx/v1/data-core'

        response_pokemon = requests.request("GET",url_api_pokemon)
        response_rickandmorty = requests.request("GET",url_api_rickandmorty)
        response_gobierno = requests.request("GET",url_api_gobierno)

        rick = response_rickandmorty.json()
        pokemon = response_pokemon.json()
        gobierno = response_gobierno.json()
        return render_template('index.html',datos_pokemon = pokemon, datos_rick = rick, datos_gobierno = gobierno)
        # response.json()