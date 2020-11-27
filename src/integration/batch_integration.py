import requests

SERVICE_URL = "http://localhost:8082/recipe-service/v1/batches"

def get_batch(batch_id):
    response = requests.get(
        f'{SERVICE_URL}/{batch_id}', 
    )
    return response

def post_batch(batch):
    response = requests.post(
        SERVICE_URL, 
        headers={'Content-Type':'application/json;charset=UTF-8'},
        data=batch,
    )
    return response

def put_batch(batch_id, batch):
    response = requests.put(
        f'{SERVICE_URL}/{batch_id}', 
        headers={'Content-Type':'application/json;charset=UTF-8'},
        data=batch,
    )
    return response

def delete_batch(batch_id):
    response = requests.delete(
        f'{SERVICE_URL}/{batch_id}', 
    )
    return response
