import unreal

REFERENCE = box_selection

plain_vec_x = 0.0
plain_vec_y = 0.0
plain_vec_z = 0.0

vector = unreal.Vector(0.0, 0.0, 0.0)

editor_actor_utils = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

all_actors = editor_actor_utils.get_all_level_actors()

for actor in all_actors:
    full_name = actor.get_actor_label()
    if REFERENCE == full_name:
        vector = actor.get_actor_location()
        
        plain_vec_x = vector.x
        plain_vec_y = vector.y
        plain_vec_z = vector.z
