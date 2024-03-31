// Copyright Epic Games, Inc. All Rights Reserved.

#include "UE_LocRotResetStyle.h"
#include "UE_LocRotReset.h"
#include "Framework/Application/SlateApplication.h"
#include "Styling/SlateStyleRegistry.h"
#include "Slate/SlateGameResources.h"
#include "Interfaces/IPluginManager.h"
#include "Styling/SlateStyleMacros.h"

#define RootToContentDir Style->RootToContentDir

TSharedPtr<FSlateStyleSet> FUE_LocRotResetStyle::StyleInstance = nullptr;

void FUE_LocRotResetStyle::Initialize()
{
	if (!StyleInstance.IsValid())
	{
		StyleInstance = Create();
		FSlateStyleRegistry::RegisterSlateStyle(*StyleInstance);
	}
}

void FUE_LocRotResetStyle::Shutdown()
{
	FSlateStyleRegistry::UnRegisterSlateStyle(*StyleInstance);
	ensure(StyleInstance.IsUnique());
	StyleInstance.Reset();
}

FName FUE_LocRotResetStyle::GetStyleSetName()
{
	static FName StyleSetName(TEXT("UE_LocRotResetStyle"));
	return StyleSetName;
}


const FVector2D Icon16x16(16.0f, 16.0f);
const FVector2D Icon20x20(20.0f, 20.0f);

TSharedRef< FSlateStyleSet > FUE_LocRotResetStyle::Create()
{
	TSharedRef< FSlateStyleSet > Style = MakeShareable(new FSlateStyleSet("UE_LocRotResetStyle"));
	Style->SetContentRoot(IPluginManager::Get().FindPlugin("UE_LocRotReset")->GetBaseDir() / TEXT("Resources"));

	Style->Set("UE_LocRotReset.PluginAction", new IMAGE_BRUSH_SVG(TEXT("PlaceholderButtonIcon"), Icon20x20));
	return Style;
}

void FUE_LocRotResetStyle::ReloadTextures()
{
	if (FSlateApplication::IsInitialized())
	{
		FSlateApplication::Get().GetRenderer()->ReloadTextureResources();
	}
}

const ISlateStyle& FUE_LocRotResetStyle::Get()
{
	return *StyleInstance;
}
