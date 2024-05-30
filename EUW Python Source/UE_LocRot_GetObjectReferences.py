import unreal

NAME_REF = 'OffsetRef'

# get EditorActorSubsystem
editor_actor_utils = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

# Get a list of all actors in the level
all_actors = editor_actor_utils.get_all_level_actors()
ref_names = []

# Iterate through all actors
for actor in all_actors:
    # Get the folder path of the actor
    full_name = actor.get_actor_label()
    if NAME_REF in full_name:
        ref_names.append(full_name)
        
unreal_array = unreal.Array(str)

for el in ref_names:
    unreal_array.append(el)