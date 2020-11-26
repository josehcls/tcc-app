from flask import Flask, request
# from flask_cors import CORS, cross_origin
import integration.recipe_integration as recipes

app = Flask(__name__)
# cors - CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/robots.txt')
def robots():
    data = '''
        User-Agent: *
        Disallow: /
    '''
    response = app.response_class(
        response=data,
        status=200,
        mimetype='text/plain'
    )
    return response

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/v1/recipes')
def getRecipes():
    query = request.args.get('query', default='', type = str)
    page = request.args.get('query', default='0', type = int)
    size = request.args.get('query', default='10', type = int)
    return app.response_class(
        response = recipes.getRecipes(query, page, size),
        status = 200,
        mimetype = 'application/json'
    ) 

@app.route('/v1/recipes/<recipe_id>')
def getRecipe(recipe_id):
    return app.response_class(
        response = recipes.getRecipe(recipe_id),
        status = 200,
        mimetype = 'application/json'
    ) 

@app.route('/v1/recipes', methods=['POST'])
def postRecipe():
    recipe = request.data
    print(recipe)
    return app.response_class(
        response = recipes.postRecipe(recipe),
        status = 200,
        mimetype = 'application/json'
    ) 

@app.route('/v1/recipes/<recipe_id>', methods=['PUT'])
def putRecipe(recipe_id):
    recipe = request.data
    return app.response_class(
        response = recipes.putRecipe(recipe_id, recipe),
        status = 200,
        mimetype = 'application/json'
    ) 

@app.route('/v1/recipes/<recipe_id>', methods=['DELETE'])
def deleteRecipe(recipe_id):
    return app.response_class(
        response = recipes.deleteRecipe(recipe_id),
        status = 200,
        mimetype = 'application/json'
    ) 

@app.after_request # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = '*'
    header['Access-Control-Allow-Methods'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0')
