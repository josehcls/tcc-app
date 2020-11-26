import requests

SERVICE_URL = "http://localhost:8082/recipe-service/v1/recipes"

def getRecipes(query, page, size):
    response = requests.get(
        SERVICE_URL, 
        params={'query': query, 'page': page, 'size': size},
    )
    return response.text

def getRecipe(recipe_id):
    response = requests.get(
        f'{SERVICE_URL}/{recipe_id}', 
    )
    return response.text

def postRecipe(recipe):
    response = requests.post(
        SERVICE_URL, 
        headers={'Content-Type':'application/json;charset=UTF-8'},
        data=recipe,
    )
    print(response.text)
    return response.text

def putRecipe(recipe_id, recipe):
    response = requests.put(
        f'{SERVICE_URL}/{recipe_id}', 
        headers={'Content-Type':'application/json;charset=UTF-8'},
        data=recipe,
    )
    return response.text

def deleteRecipe(recipe_id):
    response = requests.delete(
        f'{SERVICE_URL}/{recipe_id}', 
    )
    return response.text

# def getBatchesFromRecipe(recipeId):
#     pass
