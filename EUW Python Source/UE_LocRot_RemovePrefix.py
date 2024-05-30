import unreal
import json
import re

# get EditorActorSubsystem
editor_actor_utils = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

# get all selected actors on scene
selected_actors = editor_actor_utils.get_selected_level_actors()
selected_assets = unreal.EditorUtilityLibrary.get_selected_asset_data()

def serialize_json(json_string):
    json_string = re.sub(r'(\w+)(\s*:\s*)', r'"\1"\2', json_string)
    json_string = re.sub(r':\s*([^"\d\{\}\[\],\s]+)', r': "\1"', json_string)
    return json_string

if drawer_rename == True:
    if not selected_assets:
        print("No assets were selected.")
    else:
        assets_list = str(selected_assets)
        valid_json = serialize_json(assets_list)
        selected_assets_data = json.loads(valid_json)
        
        for asset in selected_assets_data:
            package_path = asset['package_path']
            asset_og_name = asset['asset_name']
            if prefix in asset_og_name:
                old_name = f'{package_path}/{asset_og_name}.{asset_og_name}'
                new_name = old_name.replace(prefix, "")
                unreal.EditorAssetLibrary.rename_asset(old_name, new_name)

if not selected_actors:
    print("No actors were selected.")
else:   
    for actor in selected_actors:
        # getting actor label
        actor_name = actor.get_actor_label()
        if prefix in actor_name:
            new_name = actor_name.replace(prefix, "")
            actor.set_actor_label(new_name)