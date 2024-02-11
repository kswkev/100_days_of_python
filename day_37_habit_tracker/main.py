#https://pixe.la/@kswkev
import requests
import datetime as dt


API_TOKEN = "E42h9kw1HQ57ab"
PIXELA_USERNAME = "kswkev"
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"


def create_pixela_user(token, username):
    #https://docs.pixe.la/entry/post-user
    user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    return requests.post(url=PIXELA_ENDPOINT, json=user_params)


def create_pixela_graph(token, username, graph_id, name, unit, unit_type, color):
    #https://docs.pixe.la/entry/post-graph
    pixela_graphs_endpoint =  f"{PIXELA_ENDPOINT}/{username}/graphs"

    graph_config = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": unit_type,
        "color": color
    }

    headers = {
        "X-USER-TOKEN": token
    }

    return requests.post(url=pixela_graphs_endpoint, json=graph_config, headers=headers)


def add_pixel_to_graph(token, username, graph_id, date, quantity):
    #https://docs.pixe.la/entry/post-pixel
    pixela_pixel_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}"

    pixel_config = {
        "date": date,
        "quantity": quantity
    }

    headers = {
            "X-USER-TOKEN": token
    }

    return requests.post(url=pixela_pixel_endpoint, json=pixel_config, headers=headers)


def update_pixel(token, username, graph_id, date, quantity):
    #https://docs.pixe.la/entry/put-pixel
    pixela_pixel_put_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}/{date}"

    pixel_config = {
        "quantity": quantity
    }

    headers = {
            "X-USER-TOKEN": token
    }

    return requests.put(url=pixela_pixel_put_endpoint, json=pixel_config, headers=headers)


def delete_pixel(token, username, graph_id, date):
    #https://docs.pixe.la/entry/delete-pixel
    pixela_pixel_delete_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}/{date}"

    headers = {
        "X-USER-TOKEN": token
    }

    return requests.delete(url=pixela_pixel_delete_endpoint, headers=headers)


# create_user_response = create_pixela_user(API_TOKEN, PIXELA_USERNAME)
# print(create_user_response.text)

# create_graph_response = create_pixela_graph(API_TOKEN, PIXELA_USERNAME, GRAPH_ID, "Python Coding Graph", "hours", "int", "ajisai")
# print(create_graph_response.text)

# formatted_date = dt.datetime.now().strftime("%Y%m%d")
# add_pixel_response = add_pixel_to_graph(API_TOKEN, PIXELA_USERNAME, GRAPH_ID, formatted_date, "1")
# print(add_pixel_response.text)

# formatted_date = dt.datetime.now().strftime("%Y%m%d")
# update_pixel_response = update_pixel(API_TOKEN, PIXELA_USERNAME, GRAPH_ID, formatted_date, "2")
# print(update_pixel_response.text)

formatted_date = dt.datetime.now().strftime("%Y%m%d")
delete_pixel_response = delete_pixel(API_TOKEN, PIXELA_USERNAME, GRAPH_ID, formatted_date)
print(delete_pixel_response.text)