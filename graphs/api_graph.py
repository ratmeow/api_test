import numpy as np
from utils import request, request_binary

rng = np.random.default_rng()

api_name = "Graph"


def create_graph(name: str = "New Graph",
                 description: str = "Graph description",
                 print_: bool = False):

    url = f'/{api_name}.create'

    data = {
        "projectUuid": "00000000-0000-0000-0000-000000000001",
        "name": name,
        "description": description
    }
    params = {
        "data": data,
        "responseFormat": "unison"
    }

    response = request(url=url, params=params)

    if print_:
        print("CREATE---------\n", response.json())
    return response.json()


def get_graph(uuid: str,
        print_: bool = False):

    url = f'/{api_name}.get'
    params = {
            "uuid": uuid,
            "codec": "",
            "api_version": "0.1"
    }

    response = request(url=url, params=params)
    if print_:
        print('---GET---\n', response.json())
    return response.json()