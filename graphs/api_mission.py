import numpy as np
from typing import Optional
from utils import request, request_binary

rng = np.random.default_rng()

api_name = "GraphMission"


def create_mission(
        parent_folder_uuid: str,
        name: str = "Mission",
        description: str = "Mission description",
        print_: bool = True):

    url = f'/{api_name}.create'

    data = {
        "parentFolderUuid": parent_folder_uuid,
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


def get_mission(uuid: str,
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



def save_as_mission(
        parent_folder_uuid: str,
        mission_uuid: str,
        print_: bool = True):

    url = f'/{api_name}.saveAs'

    data = {
        "parentFolderUuid": parent_folder_uuid,
        "missionUuid": mission_uuid,
    }
    params = {
        "data": data,
        "responseFormat": "unison"
    }

    response = request(url=url, params=params)

    if print_:
        print("SAVE AS---------\n", response.json())
    return response.json()


def update_mission(uuid: str,
                   name: Optional[str] = None,
                   data: Optional[dict] = None,
                   print_: bool = True):

    url = f'/{api_name}.update'

    params = {
        "uuid": uuid,
        "data": data,
        "responseFormat": "unison"
    }

    response = request(url=url, params=params)

    if print_:
        print("UPDATE---------\n", response.json())
    return response.json()
