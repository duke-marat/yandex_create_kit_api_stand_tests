import configuration
import requests
import data

def post_new_client_kit(kit_body, auth_token):
    headers_with_token = data.headers.copy()
    headers_with_token["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body, headers=headers_with_token)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

def get_new_user_token(user_body):
    response = post_new_user(user_body)
    auth_token = response.json().get("authToken")
    return auth_token


