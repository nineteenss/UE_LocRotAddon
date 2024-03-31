// Copyright Epic Games, Inc. All Rights Reserved.

#include "UE_LocRotResetCommands.h"

#define LOCTEXT_NAMESPACE "FUE_LocRotResetModule"

void FUE_LocRotResetCommands::RegisterCommands()
{
	UI_COMMAND(PluginAction, "UE_LocRotReset", "Execute UE_LocRotReset action", EUserInterfaceActionType::Button, FInputChord());
}

#undef LOCTEXT_NAMESPACE
