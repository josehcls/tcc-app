import requests

SERVICE_URL = "http://tcc-recipe-service/recipe-service/v1/recipes"

def get_recipes(query, page, size):
    response = requests.get(
        SERVICE_URL, 
        params={'query': query, 'page': page, 'size': size},
    )
    return response

def get_recipe(recipe_id):
    response = requests.get(
        f'{SERVICE_URL}/{recipe_id}', 
    )
    return response

def post_recipe(recipe):
    response = requests.post(
        SERVICE_URL, 
        headers={'Content-Type':'application/json;charset=UTF-8'},
        data=recipe,
    )
    return response

def put_recipe(recipe_id, recipe):
    response = requests.put(
        f'{SERVICE_URL}/{recipe_id}', 
        headers={'Content-Type':'application/json;charset=UTF-8'},
        data=recipe,
    )
    return response

def delete_recipe(recipe_id):
    response = requests.delete(
        f'{SERVICE_URL}/{recipe_id}', 
    )
    return response

def get_batches_from_recipe(recipe_id, query, page, size):
    response = requests.get(
        f'{SERVICE_URL}/{recipe_id}/batches', 
        params={'query': query, 'page': page, 'size': size},
    )
    return response
