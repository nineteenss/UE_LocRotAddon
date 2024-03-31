# UE_LocRotAddon
Blender addon and Unreal Engine pluing for exporting objects Location and Rotation data to UE and resetting objects Rotation and Location in the UE's viewport.

**Before we start:** during this guide i will be using **"Assets Export"** folder as a "default" folder and path for the entire process of data extraction from Blender and actors location and rotation reset in Unreal Engine.

## Installation:
- Download **"UE_LocRot_Addon_v1.0_3.4.1.zip"** and **"UE_Plugin_v1.0_5.3.2.zip"** from [Releases](https://github.com/nineteenss/UE_LocRotAddon/releases) section.
- Create an empty folder and rename it to your liking, for example **"Assets Export"**. We will use it later for export and import process. You can put this folder anywhere you like, so location doesn't matter.

![image](https://github.com/nineteenss/UE_LocRotAddon/assets/26834864/b61c0e78-bee6-474c-8c78-f3c6f9a29c51)

- For convenience, you can place the downloaded files in the newly created folder:

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/folder_1.png?raw=true)

- Add-on and Plug-in installation steps below.

## Blender:

- Open Blender and go to **"Edit > Preferences > Add-ons"**;
- Find **"Install"** button (top right corner) and locate **"Assets Export"** folder you created earlier;
- Choose **"UE_LocRot_Addon_v1.0_3.4.1.zip"** from file explorer and press **"Install Add-on"**.

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/blender_addon_setup.png?raw=true)

![image](https://github.com/nineteenss/UE_LocRotAddon/assets/26834864/a48593ae-0ae8-48c5-8a6b-725260f8c3d9)

- After installation complete, addon will appear in the list-view of your Add-ons tab;
- Press arrow and click on the check-box near the name of the addon in order to activate addon;
- After activation, go down to **"Preferences"** and find **"FILE PATH"**, here you must set any desired folder path you will use for data export (I will set **"Assets Export"**, that I created earlier).

![image](https://github.com/nineteenss/UE_LocRotAddon/assets/26834864/8006e2b9-b218-4a50-82c6-4b391e71f959)

- Now, after installation is complete and addon was set up for work - save preferences and close the window.

![image](https://github.com/nineteenss/UE_LocRotAddon/assets/26834864/70c042d6-ebe9-4698-9319-558900c6695b)

- Then locate installed addon in tools panel **(Press "N")** and find **"UE_LRE"**.

![image](https://github.com/nineteenss/UE_LocRotAddon/assets/26834864/2d50465d-68e0-4eae-bd04-2119bdf3d6b7)

- Here you can see three steps to follow:  
  - Step one - Export data from selected objects:
       - **"Invert Y,Z (Rotation)"** - Inverts rotation of selected objects in **"LocRotData.txt"** on export (I don't know why, but Unreal Engine uses inverted Y and Z rotation than Blender. I left that option "False" by default, so if you know how to avoid that difference in rotation, you can leave it unchecked).
       - **"Invert Y (Location)"** - Inverts location of selected objects in **"LocRotData.txt"** on export (It's the same as in rotation, Unreal Engine uses inverted Y rotation than Blender. I left that option "False" by default, so if you know how to avoid that difference in location, you can leave it unchecked).
       - **"Export Data"** - Export **Location (X,Y,Z)** and **Rotation (X,Y,Z)** of your objects to data file called **"LocRotData.txt"** located in the **"UE_LocRotExport_Tools"** folder (since we use it as a default path and folder for this guide):
  - Step two - Prepare objects to export from blender:    
       - **"Remove Name Dots"** - Since UE replaces dots **'.'** with underscores **'_'**, you can do that manually before export to FBX (this also helps to restore objects position in blender using **"Reset Objects"** button).
       - **"Apply Modifiers"** - In order to make proper object placements all modifiers should be applied, for example: Mirror, Subdivision, Bevel etc. It also checks if selected objects contain "Curves" and converts them into "Mesh".
       - **"Clear Rotation"** - Clears rotation of selected objects.
       - **"Move to WO"** - Sets cursor to World Origin and moves all selected objects to cursor.
  - Step three - Export objects using FBX as a single file:
       - **"Export FBX"** - Opens standard "Export as FBX" Blender window.
       - Of course, you can export objects using other file formats or methods of your choice. But i haven't tested it myself yet, so you can try and give your feedback to me.
  - **"Reset Objects"** - Resets default selected objects position from the **"LocRotData.txt"** we exported data to earlier (It uses data from "LocRotData.txt", so it won't work before you export data to file):
       - **"Replace '.' (dots) with '_' (underscore)"** - If you haven't replaced dots in the names of your objects inside Blender during mesh export process **(Step two)**, it will do it automatically on objects reset process. Set to **"True"** by default.
   

## Unreal Engine:

In order to make plugin work, make sure you enabled python dependancy in plugins section of your project.

![image](https://github.com/nineteenss/UE_LocRotAddon/assets/26834864/9a78d457-585b-45df-b01a-3d68ac02f644)
