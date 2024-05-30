import unreal
import json
import os

FILE_NAME = 'LocRotData.txt'
DATA_PATH = data_path

# making script reading local data file
file_path = fr"{DATA_PATH}\{FILE_NAME}"
not_found = f"{FILE_NAME} found."

if os.path.isfile(file_path):

    # read data from file
    with open(file_path, 'r') as data:
        ol = json.load(data)

    # get EditorActorSubsystem
    editor_actor_utils = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

    # get all selected actors on scene
    selected_actors = editor_actor_utils.get_selected_level_actors()

    # check actors being selected
    if not selected_actors:
        print("No actors were selected")
    else:
        # setting up new location и rotation for each selected actor
        for actor in selected_actors:
            # getting actor label
            actor_name = actor.get_actor_label()
            # check if the actor name is exactly in the list
            if actor_name in ol[::3]:
                # getting actor name index in the list
                index = ol.index(actor_name)
                # getting new location и rotation values
                if offset_use_check == True:
                    new_location = unreal.Vector(float(ol[index + 1]['x']) + plain_vec_x, float(ol[index + 1]['y']) + plain_vec_y, float(ol[index + 1]['z']) + plain_vec_z)
                else:
                    new_location = unreal.Vector(float(ol[index + 1]['x']), float(ol[index + 1]['y']), float(ol[index + 1]['z']))
                new_rotation = unreal.Rotator(float(ol[index + 2]['x']), float(ol[index + 2]['y']), float(ol[index + 2]['z']))
                # setting new location и rotation values
                actor.set_actor_location(new_location, False, False)
                actor.set_actor_rotation(new_rotation, False)
                
    # + unreal.Vector(float(-5630.0),float(-4990.0),float(0.0))
else:
    not_found = f"File '{FILE_NAME}' not found in the '{DATA_PATH}' directory. Please check if you set correct path."