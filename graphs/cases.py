from api_graph import create_graph, get_graph
from api_folder import *
from api_mission import *
from api_comment import create_comment, get_comment
import time
# get_graph(uuid=, print_=True)


graph_uuid = "a9942526-3dc2-4735-a7fd-4285a11143be"
parent_folder = "aa68111f-e65b-4dd7-8ed9-57a257c67e56"
other_graph_uuid = "a2ffcaec-369d-4007-b2b7-d575cb10c478"

# create_mission(parent_folder_uuid=parent_folder)
# save_as_mission(parent_folder_uuid=parent_folder, mission_uuid="e85d1d70-8253-47d4-a5c3-06aa951e0457")

# update_mission(uuid="d0a9d9a4-a66a-4ef6-95b9-037d7ec6df41", data={"cpuPerNode": 64})
remove_folder(uuid="aa68111f-e65b-4dd7-8ed9-57a257c67e56")
