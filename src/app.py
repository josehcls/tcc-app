from flask import Flask, request
import integration.recipe_integration as recipes
import integration.batch_integration as batches

app = Flask(__name__)

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
def get_recipes():
    query = request.args.get('query', default='', type = str)
    page = request.args.get('query', default='0', type = int)
    size = request.args.get('query', default='10', type = int)
    response = recipes.get_recipes(query, page, size)
    return app.response_class(
        response = response.text,
        status = response.status_code,
        mimetype = response.headers['Content-Type'],
    ) 

@app.route('/v1/recipes/<recipe_id>')
def get_recipe(recipe_id):
    response = recipes.get_recipe(recipe_id)
    return app.response_class(
        response = response.text,
        status = response.status_code,
        mimetype = response.headers['Content-Type'],
    ) 

@app.route('/v1/recipes', methods=['POST'])
def post_recipe():
    recipe = request.data
    response = recipes.post_recipe(recipe)
    return app.response_class(
        response = response.text,
        status = response.status_code,
        mimetype = response.headers['Content-Type'],
    ) 

@app.route('/v1/recipes/<recipe_id>', methods=['PUT'])
def put_recipe(recipe_id):
    recipe = request.data
    response = recipes.put_recipe(recipe_id, recipe)
    return app.response_class(
        response = request.text,
        status = response.status_code,
        mimetype = response.headers['Content-Type'],
    ) 

@app.route('/v1/recipes/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    response = recipes.delete_recipe(recipe_id)
    return app.response_class(
        response = response.text,
        status = response.status_code,
        mimetype = response.headers['Content-Type'],
    ) 

@app.route('/v1/recipes/<recipe_id>/batches')
def get_batches_from_recipe(recipe_id):
    query = request.args.get('query', default='', type = str)
    page = request.args.get('query', default='0', type = int)
    size = request.args.get('query', default='10', type = int)
    response = recipes.get_batches_from_recipe(recipe_id, query, page, size)
    return app.response_class(
        response = response.text,
        status = response.status_code,
        mimetype = response.headers['Content-Type'],
    ) 

@app.route('/v1/batches/<batch_id>')
def get_batch(batch_id):
    response = batches.get_batch(batch_id)
    return app.response_class(
        response = response.text,
        status = response.status_code,
        mimetype = response.headers['Content-Type'],
    ) 

@app.route('/v1/batches', methods=['POST'])
def post_batch():
    batch = request.data
    response = batches.post_batch(batch)
    return app.response_class(
        response = response.text,
        status = 200,
        mimetype = 'application/json'
    ) 

@app.route('/v1/batches/<batch_id>', methods=['PUT'])
def put_batch(batch_id):
    batch = request.data
    response = batches.put_batch(batch_id, batch)
    return app.response_class(
        response = response.text,
        status = response.status_code,
        mimetype = response.headers['Content-Type'],
    ) 

@app.route('/v1/batches/<batch_id>', methods=['DELETE'])
def delete_batch(batch_id):
    response = batches.delete_batch(batch_id)
    return app.response_class(
        response = response.text,
        status = response.status_code,
        mimetype = response.headers['Content-Type'],
    ) 

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = '*'
    header['Access-Control-Allow-Methods'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0')
