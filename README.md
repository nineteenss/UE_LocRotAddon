# UE_LocRotAddon
Blender addon and Unreal Engine pluing for exporting objects Location and Rotation data to UE and resetting objects Rotation and Location in the UE's viewport.

**Before we start:** during this guide - we will be using **"Assets Export"** folder as a "default" folder and path for the entire process of data extraction from Blender and actors location and rotation reset in Unreal Engine.

## 1. Installation:
- Download **"UE_LocRot_Addon_v1_341.zip"** and **"UE_Plugin_v1_532.zip"** from [Releases](https://github.com/nineteenss/UE_LocRotAddon/releases) section.
- Create an empty folder and rename it to your liking, for example **"Assets Export"**. We will use it later for export and import process. You can put this folder anywhere you like, so location doesn't matter.

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/folder_created.png?raw=true)

- For convenience, you can place the downloaded files in the newly created folder:

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/folder_1.png?raw=true)

- Add-on and Plug-in installation steps below.

## 2. Blender:

- Open Blender and go to **"Edit > Preferences > Add-ons"**;
- Find **"Install"** button (top right corner) and locate **"Assets Export"** folder you created earlier;
- Choose **"UE_LocRot_Addon_v1_341.zip"** from file explorer and press **"Install Add-on"**.

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/blender_addon_setup.png?raw=true)

- After installation complete, addon will appear in the list-view of your Add-ons tab;
- Press arrow and click on the check-box near the name of the addon in order to activate addon;
- After activation, go down to **"Preferences"** and find **"FILE PATH"**, here you must set any desired folder path you will use for data export (I will set **"Assets Export"**, that I created earlier).

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/blender_addon_setup_1.png?raw=true)

- Now, after installation is complete and addon was set up for work - save preferences and close the window.

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/blender_addon_setup_3.png?raw=true)

- You can locate installed addon in tools panel **(Press "N")** and find **"UE_LRE"**.

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/addon_ui.png?raw=true)

**Description:**
- Here you can see three steps to follow:  
  - Step one - Export data from selected objects:
       - **"Invert Y,Z (Rotation)"** - Inverts rotation of selected objects in **"LocRotData.txt"** on export (I don't know why, but Unreal Engine uses inverted Y and Z rotation than Blender. I left that option "False" by default, so if you know how to avoid that difference in rotation, you can leave it unchecked).
       - **"Invert Y (Location)"** - Inverts location of selected objects in **"LocRotData.txt"** on export (It's the same as in rotation, Unreal Engine uses inverted Y rotation than Blender. I left that option "False" by default, so if you know how to avoid that difference in location, you can leave it unchecked).
       - **"Export Data"** - Export **Location (X,Y,Z)** and **Rotation (X,Y,Z)** of your objects to data file called **"LocRotData.txt"** located in the **"Assets Export"** folder (since we use it as a default path and folder for this guide):
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

Now blender setup is ready, but before we proceed with data export, I recommend you to finish Unreal Engine plugin installation, so then we will be able to perform complete process of data export and import.

## 3. Unreal Engine:

- Go to the Unreal Projects folder and select the project you want to install the plugin in;
- Create new folder and rename it to **"Plugins"** if it doesn't exists.

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/project_location_folder_creation.png?raw=true)

- Now open folder **"Assets Export"** that we created earlier and extract **"UE_Plugin_v1_532.zip"** file.

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/plugin_extract.png?raw=true)

- Move inside extracted **"UE Plugin"** folder and copy **"UE_LocRotReset"** folder from it;

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/copy_plugin.png?raw=true)

- Head back to your UE project folder and go inside **"Plugins"** folder we created before and paste copied **"UE_LocRotReset"** folder inside of it. 

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/paste_plugin.png?raw=true)

- And now, after you did all these steps, installation is almost complete. You can Run your Unreal project through *.uproject file or Unreal Engine launcher;
- Then, go to **"Edit > Plugins"**

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/unreal_edit_plugins.png?raw=true)

- You will see **"Plugins"** window.
- You need to make sure to enable **"Python"** inside Unreal Engine.
- To do that - in the search field type in word **"Python"** and enable following dependacies (Could be already active by default in UE 5.3. If so, skip to the next part):

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/python_enable.png?raw=true)

- Right after, clear the search bar and go to **"Other"** tab on the left (right under **"Installed"** header);
- Find there **"UE_LocRotReset"** and enable it by clicking onto the check-box and restart Unreal Engine project (If it's already active - skip that part and close **"Plugins"** window).

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/enable_plugin.png?raw=true)

- Now you can see, that your editor toolbar have one more button with "LRR" signature on it;
- By clicking on it you will get window opened:

![image](https://github.com/nineteenss/UE_LocRotAddon_README_Assets/blob/main/toolbar_icon.png?raw=true)

**It means that the installation of addon and plugin is complete and now we're ready for assets data transfer.**

## 4. Usage:

