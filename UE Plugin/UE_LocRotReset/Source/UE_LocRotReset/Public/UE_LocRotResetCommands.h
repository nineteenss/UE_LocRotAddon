// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Framework/Commands/Commands.h"
#include "UE_LocRotResetStyle.h"

class FUE_LocRotResetCommands : public TCommands<FUE_LocRotResetCommands>
{
public:

	FUE_LocRotResetCommands()
		: TCommands<FUE_LocRotResetCommands>(TEXT("UE_LocRotReset"), NSLOCTEXT("Contexts", "UE_LocRotReset", "UE_LocRotReset Plugin"), NAME_None, FUE_LocRotResetStyle::GetStyleSetName())
	{
	}

	// TCommands<> interface
	virtual void RegisterCommands() override;

public:
	TSharedPtr< FUICommandInfo > PluginAction;
};
