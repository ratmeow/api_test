import numpy as np
from utils import request, request_binary

rng = np.random.default_rng()

api_name = "Comment"


def create_comment(
        text: str,
        graph_object_uuid: str,
        print_: bool = True):

    url = f'/{api_name}.create'

    params = {
        "text": text,
        "objectUuid": graph_object_uuid,
        "responseFormat": "unison"
    }

    response = request(url=url, params=params)

    if print_:
        print("CREATE---------\n", response.json())
    return response.json()


def get_comment(uuid: str,
               print_: bool = True):

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

