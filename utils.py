import pandas as pd
from typing import Union
import random
import requests

def convert_data_from_get_request(response: dict):
    points_data = response["result"]["data"]["item"][9]
    cols = [col[0] for col in response["result"]["data"]["item"][10]]
    data_df = pd.DataFrame(data=points_data, columns=cols)
    print(data_df)
    return data_df

def get_schema_from_df(df: pd.DataFrame) -> list:
    schema = []
    for col in df.columns:
        schema.append({
            "name": col,
            "type": type(df[col].values.tolist()[0]).__name__
        })

    return schema


def list_response_to_df(response: dict):
    points_list = response['result']['data']['list']
    if len(points_list) == 0:
        return []
    else:
        df = pd.DataFrame(columns=['uuid', 'data size'])
        for points in points_list:
            df.loc[len(df.index)] = [points[0], len(points[-2])]
        return df


def build_list_filter_by_uuid(uuid: Union[str, list[str]]):
    list_filter_by_uuid = {}

    if isinstance(uuid, str):
        list_filter_by_uuid["uuid"] = {"$eq": uuid}
    else:
        if random.choice([0, 1]) == 0:
            print("IN")
            list_filter_by_uuid["uuid"] = {"$in": uuid}
        else:
            print("NIN")
            list_filter_by_uuid["uuid"] = {"$nin": uuid}

    return list_filter_by_uuid


HOST_PORT = 'localhost:8095'


def request(url: str, token: str = None, params: dict = None, address=HOST_PORT):
    answer = requests.post(
        url=f"http://{address}/api/rpc{url}",
        headers={"authorization": token} if token else {},
        json={
            "jsonrpc": "2.0",
            "id": 0,
            "method": f"{url.split('/')[-1]}",
            "params": params,
        },
    )
    return answer


def request_binary(
    url: str,
    token: str = None,
    params: dict = None,
    address=HOST_PORT,
    files=None,
):

    kwargs = {
        "url": f"http://{address}/api/binary{url}",
        "headers": (
            {"authorization": token, "Content-Type": "application/json"}
            if token
            else {}
        ),
    }
    if files is None:
        kwargs["json"] = params
    else:
        kwargs["data"] = params
        kwargs["files"] = files
    answer = requests.post(**kwargs)
    return answer


def convert_unison_dict_to_dict(d):
    data = d["item"]
    schema = d["schema"]
    return _unite_items_and_schema(data, schema)


def _unite_items_and_schema(items, schema):
    result_dict = {}
    if schema is None:
        if items == []:
            return {}
        return items
    for i in range(len(schema)):
        if schema[i]["type"] == "item":
            result_dict[schema[i]["name"]] = _unite_items_and_schema(
                items=items[i], schema=schema[i]["schema"]
            )
        elif schema[i]["type"] == "list":
            result_dict[schema[i]["name"]] = [
                _unite_items_and_schema(items=items[i][x], schema=schema[i]["schema"])
                for x in range(len(items[i]))
            ]
        else:
            try:
                result_dict[schema[i]["name"]] = items[i]
            except IndexError:
                result_dict[schema[i]["name"]] = None
    return result_dict

def convert_unison_list_to_list(li):
    data = li["list"]
    schema = li["schema"]
    return [_unite_items_and_schema(items=dat, schema=schema) for dat in data]


def get_idx(in_list, name):
    try:
        return [i["name"] for i in in_list].index(name)
    except ValueError:
        return -1

def zip_list_with_schema(lst, schema):
    item = {}
    for i in range(len(lst)):
        if schema[i].get("schema", None) is not None:
            item[schema[i]["name"]] = zip_list_with_schema(lst[i], schema[i]["schema"])
        else:
            item[schema[i]["name"]] = lst[i]
    return item


def item_from_unison(answer, is_list=False):
    result = answer.get("result", {})
    data = result.get("data", {})
    schema = data.get("schema", [])
    if is_list:
        lst = data.get("list", [])
    else:
        lst = [data.get("item", [])]
    next_lst = []
    for i in range(len(lst)):
        next_lst.append(zip_list_with_schema(lst[i], schema))
    if is_list:
        return next_lst
    return next_lst[0]