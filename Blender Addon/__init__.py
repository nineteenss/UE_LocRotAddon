bl_info = {
    "name": "UE 5.3.2 Location-Rotation Export Tool",
    "author": "Sergey Smetannikov (nineteenss)",
    "version": (1, 0),
    "blender": (3, 4, 1),
    "description": "Export selected objects location and rotation info to file.",
    "warning": "",
    "doc_url": "",
    "category": "Generic",
    "location": "View3D"
}

import bpy
import json
from bpy.types import Panel, Operator, AddonPreferences
from bpy.props import StringProperty, BoolProperty
from math import degrees, radians

# constants
FILE_NAME = 'LocRotData.txt'
SCALE_MULTIPLY = 100

class Preferences(AddonPreferences):
    bl_idname = __name__
    file_path: StringProperty(
        name="EXPORT PATH",
        subtype='FILE_PATH',
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Requirements: Blender version - 3.4.1, UE version - 5.3.2 (tested on)")
        layout.label(text="Don't forget to setup export path below in order to be able to export your data to file!")
        layout.prop(self, "file_path")

class ApplyModifiersOperator(Operator):
    bl_idname = "object.apply_modifiers"
    bl_label = "Apply Modifiers"
    bl_description = "Apply all modifiers for selected objects"
      
    def execute(self, context):
        if not bpy.context.selected_objects:
            self.report({'INFO'}, "No objects selected!")
            return {'CANCELLED'}
        
        for obj in bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = obj
            # Check if the object is a curve and convert it to a mesh if it is
            if obj.type == 'CURVE':
                bpy.ops.object.convert(target='MESH')
            for modifier in obj.modifiers:
                bpy.ops.object.modifier_apply(modifier=modifier.name)

        return {'FINISHED'}

class ClearRotationOperator(Operator):
    bl_idname = "object.clear_rotation"
    bl_label = "Clear Rotation"
    bl_description = "Clear rotation for selected objects"

    def execute(self, context):
        if not bpy.context.selected_objects:
            self.report({'INFO'}, "No objects selected!")
            return {'CANCELLED'}
        
        for obj in bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.rotation_clear(clear_delta=False)
            
        return {'FINISHED'}

class MoveToWOOperator(Operator):
    bl_idname = "object.move_to_wo"
    bl_label = "Move to WO"
    bl_description = "Set cursor to world origin and move selected objects to cursor position"

    def execute(self, context):
        if not bpy.context.selected_objects:
            self.report({'INFO'}, "No objects selected!")
            return {'CANCELLED'}
        
        bpy.ops.view3d.snap_cursor_to_center()
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
        
        return {'FINISHED'}

class ExportDataOperator(Operator):
    bl_idname = "object.export_data"
    bl_label = "Export Data"
    bl_description = "Export location and rotation data for selected objects"

    def execute(self, context):
        if not bpy.context.selected_objects:
            self.report({'INFO'}, "No objects selected!")
            return {'CANCELLED'}

        file_name = FILE_NAME
        user_preferences = context.preferences
        addon_prefs = user_preferences.addons[__name__].preferences
        file_path = fr'{addon_prefs.file_path}\{file_name}'

        object_list = []
        
        invert_y = context.scene.invert_y
        invert_rot_yz = context.scene.invert_rot_yz
        
        for obj in bpy.context.selected_objects:
            obj_name = obj.name
            if '.' in obj_name:
                obj_name = obj_name.replace('.', '_')
            object_list.append(obj_name)
            if invert_y: # self.invert_y
                location_dict = {'x': f'{obj.location[0] * SCALE_MULTIPLY}', 'y': f'{obj.location[1] * SCALE_MULTIPLY * -1}', 'z': f'{obj.location[2] * SCALE_MULTIPLY}'}
            else:
                location_dict = {'x': f'{obj.location[0] * SCALE_MULTIPLY}', 'y': f'{obj.location[1] * SCALE_MULTIPLY}', 'z': f'{obj.location[2] * SCALE_MULTIPLY}'}
            if invert_rot_yz:
                rotation_dict = {'x': f'{degrees(obj.rotation_euler[0])}', 'y': f'{degrees(obj.rotation_euler[1]) * -1}', 'z': f'{degrees(obj.rotation_euler[2]) * -1}'}
            else:
                rotation_dict = {'x': f'{degrees(obj.rotation_euler[0])}', 'y': f'{degrees(obj.rotation_euler[1])}', 'z': f'{degrees(obj.rotation_euler[2])}'}
            object_list.append(location_dict)
            object_list.append(rotation_dict)
        
        with open(bpy.path.abspath(file_path), 'w') as file:
            file.write(json.dumps(object_list))

        self.report({'INFO'}, f"Export process completed! Data saved to {file_name}.")
        return {'FINISHED'}
    
class ExportFBXOperator(Operator):
    bl_idname = "object.export_fbx"
    bl_label = "Export FBX"
    bl_description = "Export selected objects to FBX format. Opens default in-editor FBX export window"

    def execute(self, context):
        if not bpy.context.selected_objects:
            self.report({'INFO'}, "No objects selected!")
            return {'CANCELLED'}

        bpy.ops.export_scene.fbx('INVOKE_DEFAULT')

        self.report({'INFO'}, "Export to FBX initiated!")
        return {'FINISHED'}
    
class ResetObjectsOperator(Operator):
    bl_idname = "object.reset_objects"
    bl_label = "Reset Objects"
    bl_description = "Reset selected objects' location and rotation data from file"

    def execute(self, context):
        if not bpy.context.selected_objects:
            self.report({'INFO'}, "No objects selected!")
            return {'CANCELLED'}

        file_name = FILE_NAME
        user_preferences = context.preferences
        addon_prefs = user_preferences.addons[__name__].preferences
        file_path = fr'{addon_prefs.file_path}\{file_name}'

        with open(bpy.path.abspath(file_path), 'r') as file:
            object_list = json.loads(file.read())
            
        invert_y = context.scene.invert_y
        invert_rot_yz = context.scene.invert_rot_yz
        replace_dots = context.scene.replace_dots
        
        if replace_dots:            
            for obj in bpy.context.selected_objects:
                if '.' in obj.name:
                    obj.name = obj.name.replace('.', '_')

        for i in range(0, len(object_list), 3):
            obj_name = object_list[i]
            location_dict = object_list[i+1]
            rotation_dict = object_list[i+2]

            for obj in bpy.context.selected_objects:
                if obj.name == obj_name:
                    obj.location[0] = float(location_dict['x']) / SCALE_MULTIPLY
                    if invert_y:
                        obj.location[1] = float(location_dict['y']) / SCALE_MULTIPLY * -1
                    else:
                        obj.location[1] = float(location_dict['y']) / SCALE_MULTIPLY
                    obj.location[2] = float(location_dict['z']) / SCALE_MULTIPLY
                    obj.rotation_euler[0] = radians(float(rotation_dict['x']))
                    if invert_rot_yz:
                        obj.rotation_euler[1] = radians(float(rotation_dict['y'])) * -1
                        obj.rotation_euler[2] = radians(float(rotation_dict['z'])) * -1
                    else:
                        obj.rotation_euler[1] = radians(float(rotation_dict['y']))
                        obj.rotation_euler[2] = radians(float(rotation_dict['z']))

        return {'FINISHED'}
    
class RemoveNameDotsOperator(Operator):
    bl_idname = "object.remove_name_dots"
    bl_label = "Remove Name Dots"
    bl_description = "Replace dots in the names of selected objects with underscores"

    def execute(self, context):
        if not bpy.context.selected_objects:
            self.report({'INFO'}, "No objects selected!")
            return {'CANCELLED'}
        
        for obj in bpy.context.selected_objects:
            if '.' in obj.name:
                obj.name = obj.name.replace('.', '_')
                
        return {'FINISHED'}

class ExportDataPanel(Panel):
    bl_category = 'UE_LRE'
    bl_label = "UE Location-Rotation Export Tool"
    bl_idname = "OBJECT_PT_export_data"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        layout.label(text="1. Export data from selected objects.")
        layout.prop(context.scene, "invert_rot_yz")
        layout.prop(context.scene, "invert_y")
        layout.operator("object.export_data")
        layout.label(text="2. Prepare objects to export from Blender.")
        layout.operator("object.remove_name_dots")
        layout.operator("object.apply_modifiers")
        layout.operator("object.clear_rotation")
        layout.operator("object.move_to_wo")
        layout.label(text="3. Then export objects using FBX as a single file.")
        layout.operator("object.export_fbx")
        layout.label(text="You can export objects using other file formats or methods of your choice")
        layout.prop(context.scene, "replace_dots")
        layout.operator("object.reset_objects")

def register():
    bpy.utils.register_class(Preferences)
    bpy.utils.register_class(ApplyModifiersOperator)
    bpy.utils.register_class(ClearRotationOperator)
    bpy.utils.register_class(MoveToWOOperator)
    bpy.utils.register_class(ExportDataOperator)
    bpy.utils.register_class(ExportFBXOperator)
    bpy.utils.register_class(ResetObjectsOperator)
    bpy.utils.register_class(RemoveNameDotsOperator)
    bpy.types.Scene.invert_y = BoolProperty(name="Invert Y (Location)", default=False)
    bpy.types.Scene.invert_rot_yz = BoolProperty(name="Invert Y,Z (Rotation)", default=False)
    bpy.types.Scene.replace_dots = BoolProperty(name="Replace '.' (dots) with '_' (underscore)", default=True)
    bpy.utils.register_class(ExportDataPanel)

def unregister():
    bpy.utils.unregister_class(Preferences)
    bpy.utils.unregister_class(ApplyModifiersOperator)
    bpy.utils.unregister_class(ClearRotationOperator)
    bpy.utils.unregister_class(MoveToWOOperator)
    bpy.utils.unregister_class(ExportDataOperator)
    bpy.utils.unregister_class(ExportFBXOperator)
    bpy.utils.unregister_class(ResetObjectsOperator)
    bpy.utils.unregister_class(RemoveNameDotsOperator)
    del bpy.types.Scene.invert_y
    del bpy.types.Scene.invert_rot_yz
    del bpy.types.Scene.replace_dots
    bpy.utils.unregister_class(ExportDataPanel)

if __name__ == "__main__":
    register()