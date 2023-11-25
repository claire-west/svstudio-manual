# The Context (Right-Click) Menus in Detail

Contextual menus will appear when right clicking various elements of the user interface. The options will be different based on the type of UI element being clicked.

Mac users with a single-button mouse can "right click" by holding ++ctrl++ when clicking. Some users may need to enable this feature in System Settings.

The headings on this page are organized first by the section of the UI, followed by the UI element that is being right-clicked.

## The Arrangement Panel

See [The Arrangement Panel](../workspace/arrangement.md) for an overview of UI elements.

### Existing Track

Delete, duplicate, or change the color for the track (see [Managing Tracks](../quickstart/managing-tracks.md)).

### Blank Space Below Tracks

Create a new vocal or instrumental track (see [Managing Tracks](../quickstart/managing-tracks.md)).

### Time Axis (measure number or unoccupied space)

Creating tempo, time signature, or loop markers (see [Setting Up the Score](../quickstart/setting-up-the-score.md) and [Playback → Loop Marker](../quickstart/playback.md#1-loop-marker)).

### Time Axis (existing marker)

Delete a tempo or time signature marker (see [Setting Up the Score](../quickstart/setting-up-the-score.md).

Loop markers can be hidden by clicking the Loop Mode button (see [Playback → Loop Mode](../quickstart/playback.md#3-loop-mode)).

### Note Preview Area (note group)

There are multiple options which will affect the selected instance of a group (see [Groups](groups.md)):

* Copy, cut, or delete it
* Disband the instance
* Dissociate it from the parent group
* Change the selected singer

The same options will appear when right-clicking an instrumental preview, but only the "delete selection" option will have any effect.

### Note Preview Area (instrumental preview or ARA-synced note group)

[Voice-to-MIDI Conversion](../ai-functions/voice-to-midi.md) can be accessed by right-clicking on an instrumental preview or a group that is synchronized with an audio clip in the DAW via [ARA integration](../daw-integration/ara-plugin.md).

### Note Preview Area (anywhere else)

Paste a copied group to this point in the arrangement (see [Groups](groups.md)).

## The Piano Roll

See [The Piano Roll](../workspace/piano-roll.md) for an overview of UI elements.

### Time Axis

The same options as when right-clicking the time axis in the Arrangement Panel (see above).

### Notes

Multiple options are displayed for interacting with the selected note(s) in various ways:

* Split the note at the current mouse position
* Merge the selected notes
* Open the [Insert Lyrics](batch-lyrics.md) dialog for the selection
* Shift the lyrics forward or backward for the selection
* Reset various aspects of the notes
* Generate or crop [AI Retakes](../ai-functions/ai-retakes.md)
* Recompute pitch for the selection (force re-rendering when using [Sing](../ai-functions/pitch-mode-sing.md) or [Rap](../ai-functions/pitch-mode-rap.md) pitch mode)
* Copy, cut, or delete the notes
* Select all parameters for the notes (see [Editing Parameters → Additional Functions](../parameters/editing-parameters.md#select-parameters-for-notes))
* Merge into group (no effect if the notes are already in a [Groups](groups.md))
* Disband or dissociate group (if selecting notes for an entire [Groups](groups.md))

### Unoccupied Space

* Paste the currently copied notes or group
* Change which note group is currently being edited

## The Parameters Panel

See [The Parameters Panel](../parameters/parameters-panel.md) for an overview of UI elements.

Right-clicking anywhere within the main area of the parameters panel (not the toolbar) will present the following options:

* Copy, cut, or delete the selected parameter points (see [Editing Parameters → Editing Parameter Curves](../parameters/editing-parameters.md#editing-parameter-curves)).
* Paste the copied parameter points

No options will be displayed if "Rap Intonation" is the current editing parameter.

## Side Panels and Other Menus

### Text Inputs

Right-clicking a text box will provide options to copy, cut, delete, or select the text, as well as undo/redo changes before they are confirmed.

### Library Panel (group)

Delete a group and all instances of it (see [Groups](groups.md)).

### Library Panel (group instance)

Disband, dissociate, or delete the instance of the group (see [Groups](groups.md)).

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: Context Menus in Detail])