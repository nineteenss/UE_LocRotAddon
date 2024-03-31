// Copyright Epic Games, Inc. All Rights Reserved.

#include "UE_LocRotReset.h"
#include "UE_LocRotResetStyle.h"
#include "UE_LocRotResetCommands.h"
#include "Misc/MessageDialog.h"
#include "ToolMenus.h"

#include "Editor/Blutility/Classes/EditorUtilityWidgetBlueprint.h"
#include "Editor/Blutility/Public/EditorUtilitySubsystem.h"
#include "Editor/Blutility/Classes/EditorUtilityWidget.h"

static const FName UE_LocRotResetTabName("UE_LocRotReset");

#define LOCTEXT_NAMESPACE "FUE_LocRotResetModule"

void FUE_LocRotResetModule::StartupModule()
{
	// This code will execute after your module is loaded into memory; the exact timing is specified in the .uplugin file per-module
	
	FUE_LocRotResetStyle::Initialize();
	FUE_LocRotResetStyle::ReloadTextures();

	FUE_LocRotResetCommands::Register();
	
	PluginCommands = MakeShareable(new FUICommandList);

	PluginCommands->MapAction(
		FUE_LocRotResetCommands::Get().PluginAction,
		FExecuteAction::CreateRaw(this, &FUE_LocRotResetModule::PluginButtonClicked),
		FCanExecuteAction());

	UToolMenus::RegisterStartupCallback(FSimpleMulticastDelegate::FDelegate::CreateRaw(this, &FUE_LocRotResetModule::RegisterMenus));
}

void FUE_LocRotResetModule::ShutdownModule()
{
	// This function may be called during shutdown to clean up your module.  For modules that support dynamic reloading,
	// we call this function before unloading the module.

	UToolMenus::UnRegisterStartupCallback(this);

	UToolMenus::UnregisterOwner(this);

	FUE_LocRotResetStyle::Shutdown();

	FUE_LocRotResetCommands::Unregister();
}

void FUE_LocRotResetModule::PluginButtonClicked()
{
	// Put your "OnButtonClicked" stuff here
	
	UObject* WidgetObj = LoadObject<UObject>(nullptr, TEXT("/UE_LocRotReset/EUW_LocRotReset.EUW_LocRotReset"));
	UEditorUtilityWidgetBlueprint* WidgetBP = static_cast<UEditorUtilityWidgetBlueprint*>(WidgetObj);
	UEditorUtilitySubsystem* EditorUtilitySubsystem = GEditor->GetEditorSubsystem<UEditorUtilitySubsystem>();
	EditorUtilitySubsystem->SpawnAndRegisterTab(WidgetBP);
	
}

void FUE_LocRotResetModule::RegisterMenus()
{
	// Owner will be used for cleanup in call to UToolMenus::UnregisterOwner
	FToolMenuOwnerScoped OwnerScoped(this);

	{
		UToolMenu* Menu = UToolMenus::Get()->ExtendMenu("LevelEditor.MainMenu.Window");
		{
			FToolMenuSection& Section = Menu->FindOrAddSection("WindowLayout");
			Section.AddMenuEntryWithCommandList(FUE_LocRotResetCommands::Get().PluginAction, PluginCommands);
		}
	}

	{
		UToolMenu* ToolbarMenu = UToolMenus::Get()->ExtendMenu("LevelEditor.LevelEditorToolBar.PlayToolBar");
		{
			FToolMenuSection& Section = ToolbarMenu->FindOrAddSection("PluginTools");
			{
				FToolMenuEntry& Entry = Section.AddEntry(FToolMenuEntry::InitToolBarButton(FUE_LocRotResetCommands::Get().PluginAction));
				Entry.SetCommandList(PluginCommands);
			}
		}
	}
}

#undef LOCTEXT_NAMESPACE
	
IMPLEMENT_MODULE(FUE_LocRotResetModule, UE_LocRotReset)