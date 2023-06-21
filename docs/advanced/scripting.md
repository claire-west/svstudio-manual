# Scripting

!!! note "Pro Feature"

    The features described below require Synthesizer V Studio Pro.

Synthesizer V Studio Pro supports scripting with JavaScript and LUA. Users can augment the features of the editor with their own scripts.

## Using Scripts

Some scripts are included with Synthesizer V Studio Pro. These scripts can be accessed via the "Scripts" top menu.

Select a script from the dropdown to execute it.

![Scripts Dropdown](../img/advanced/scripts.png)

### Adding New Scripts

Selecting "Open Scripts Folder" will open your operating system's file browser with the scripts folder highlighted.

Drag any new scripts into this "scripts" folder and then select "Rescan" or restart Synthesizer V Studio. The new scripts will now appear in the dropdown.

![Scripts Folder](../img/advanced/scripts-open-folder.png)

### Assigning Keybinds to Scripts

Scripts can be assigned a hotkey from the Keybinds section at the bottom of the Settings panel.

![Assigning Hotkeys to Scripts](../img/advanced/scripts-keybind.png)

## Creating Scripts

Visit the [official scripting manual](https://resource.dreamtonics.com/scripting/) for information on creating your own scripts.

### Undocumented Functions and Properties

There are some scripting capabilities not mentioned in the official documentation.

#### Tone Shift and Vocal Modes

!!! info

    Scripts using Tone Shift should declare a `minEditorVersion` of at least **65792**.

    Scripts using Vocal Modes should require a version of **67072** or higher.

The Tone Shift and Vocal Mode Automation definitions are as follows:

|`displayName`|`typeName`|`range`|`defaultValue`|
|---|---|---|---|
|"Tone Shift"|"toneShift"|-800, 800|0|
|"`<Vocal Mode Name>`"|"vocalMode_`<Vocal Mode Name>`"|-150, 150|0|

For example, when fetching a `NoteGroup`'s Automation object for the "Soft" vocal mode, the function would be `noteGroup.getParameter("vocalMode_Soft")`.

!!! warning

    Using `getParameter()` for a vocal mode will automatically initialize it for the track, even if the provided vocal mode name does not exist.

#### `Note` properties and functions

In version 1.9.0b2 some additional bindings were added to the `Note` class to enable scripting access to note-level language selection, pitch modes, and rap features.

!!! info

    Scripts using these additional bindings should declare a `minEditorVersion` of at least **67840**.

`note.getRapAccent()` returns an integer from 1-5 (only applicable for Mandarin Chinese rap).

`note.setRapAccent(integer)` (only applicable for Mandarin Chinese rap).

`note.getMusicalType()` returns a string ("sing" or "rap") based on the selected pitch mode.

`note.setMusicalType(string)`

`note.getPitchAutoMode()` returns an integer indicating whether the pitch mode is set to manual (0) or auto (1).

`note.setPitchAutoMode(integer)`

`note.getLanguageOverride()` returns a string representing the note's selected language ("japanese", "english", "mandarin", "cantonese").

`note.setLanguageOverride(string)`


Additionally, the following new properties are present on the attributes object:

`rIntonation`: `number` rap intonation (-0.5 to 0.5)

`rTone`: `number` rap tone (semitones, from -5 to 1)

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: Scripting])