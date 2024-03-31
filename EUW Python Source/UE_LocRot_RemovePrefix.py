import unreal

# get EditorActorSubsystem
editor_actor_utils = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

# get all selected actors on scene
selected_actors = editor_actor_utils.get_selected_level_actors()

if not selected_actors:
    print("No actors were selected.")
else:
    for actor in selected_actors:
        # getting actor label
        actor_name = actor.get_actor_label()
        if prefix in actor_name:
            new_name = actor_name.replace(prefix, "")
            actor.set_actor_label(new_name)