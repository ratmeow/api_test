import numpy as np
from utils import request, request_binary

rng = np.random.default_rng()

api_name = "GraphFolder"


def create_folder(
        parent_folder_uuid: str,
        graph_uuid: str,
        name: str = "Folder",
        description: str = "Folder description",
        print_: bool = True):

    url = f'/{api_name}.create'

    data = {
        "parentFolderUuid": parent_folder_uuid,
        "graphUuid": graph_uuid,
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


def get_folder(uuid: str,
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


def remove_folder(uuid: str,
                  print_: bool = True):

    url = f'/{api_name}.remove'
    params = {
            "uuid": uuid,
            "codec": "",
            "api_version": "0.1"
    }

    response = request(url=url, params=params)
    if print_:
        print('---REMOVE---\n', response.json())
    return response.json()