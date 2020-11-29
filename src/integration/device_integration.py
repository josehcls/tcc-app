import requests

SERVICE_URL = "http://tcc-recipe-service/register-service/v1/devices"

def get_devices(page, size):
    response = requests.get(
        SERVICE_URL, 
        params={'page': page, 'size': size},
    )
    return response
