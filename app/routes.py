from flask import render_template, request, redirect, url_for, make_response, jsonify
from app import app, controller
import json
import ast

recipes = [] 

@app.route('/')
@app.route('/index')
def index():
    print("homepage")
    print(recipes)
    recipes.clear()
    return render_template('index.html')

@app.route('/ingredients')
def ingredients():
    recipes.clear()
    print("here1")
    for recipe in request.args.getlist("recipes"):
        print(recipe)
        recipes.append(ast.literal_eval(recipe))

    return render_template('ingredients.html', recipes = recipes)

@app.route('/search', methods=["POST"])
def post():
    if request.method == "POST":
        print(request)
        ingredients = request.get_json()
        recipes = controller.recipefinder(ingredients['meats'] , (ingredients['vegetables']))
    print('hello2')     
    print(recipes)

    response = make_response(
        jsonify(
            {
                "redirect_link": url_for('ingredients', recipes = recipes),
                "recipes": recipes
            }
        )
    )
    return response