# Editing Parameters

Parameters offer detailed manual control over various aspects of a vocal sequence.

## Parameter Types

**Pitch Deviation**
: A layer of pitch shifts added to the base pitch curve. 100 cents is equivalent to 1 semitone.

**Vibrato Envelope**
: Amplitude modulation of vibrato.

**Loudness**
: Vocal effort/dynamics.

**Tension**
: Sharpening/relaxation of the voice.

**Breathiness**
: The amount of air flow.

**Voicing**
: Interpolation between normal phonation and whispering.

**Gender**
: Formant shifting.

**Tone Shift** (AI voice databases only)
: Modifies the tone of the voice without changing the pitch.

!!! note "Pro Feature - Tone Shift is only available in Synthesizer V Studio Pro."

**Vocal Modes** (AI voice databases only)
: Modifies the [vocal mode](../ai-functions/vocal-modes.md) settings for the voice.
: Each AI voice database has different vocal modes, and each vocal mode can be selected as a parameter and will have its own associated parameter curve.

!!! note "Pro Feature - Vocal Modes are only available in Synthesizer V Studio Pro."

### A Simple Example

In this example, SOLARIA's "Light" Vocal Mode and the Breathiness parameter are modified over the duration of a phrase.

The vertical position of a curve at a given point in time dictates the value of its respective parameter or vocal mode at that moment. For example, the "Light" Vocal Mode curve shown in the foreground is at approximately 105% at the start of the phrase, then slowly falls to around 30%, building to approximately 135% near the end of the phrase.

!!! note

    Parameter curves are associated with their horizontal location along the time axis, not the notes that occur at that same point in time.

    This means that moving, copying, or grouping a sequence of notes will not include the parameter values during the duration of that sequence unless you use the [Select Parameters for Notes](#select-parameters-for-notes) function to select them.

    Some parameters such as Pitch Deviation will be specific to the notes they line up with, and so should be moved/copied/grouped along with their respective notes. Other parameters like Vocal Modes are generally applied to entire phrases, so moving those curves along with a specific note might not make sense in all situations.

![Base Parameter Sliders](../img/parameters/parameter-curve-example.png)

## Base Values

The base value of most parameters can be set in the Voice panel. The curves in the parameters panel will modify the value from this base setting.

![Base Parameter Sliders](../img/parameters/voice-parameters.png)

### Base Value Indicator

When the base value is set for the parameter currently being edited, a green horizontal line will indicate the the base value relative to the default (indicated by the light grey horizontal line).

![Parameters Base Value](../img/parameters/parameter-base-value.png)

### Vibrato Envelope

The Vibrato Envelope parameter affects the amplitude (depth) vibrato in its duration.

Rather than a base value set in the Voice panel, the curve modifies the vibrato depth setting of the note as defined in the Note Properties panel when using Manual Pitch Mode (Basic and Pro editions), or the note's Vibrato Modulation setting when using "Sing" Pitch Mode (Pro edition only).

![Vibrato Envelope](../img/parameters/vibrato-envelope.png)

### Rap Intonation

The Rap Intonation parameter offers a graphical tool for editing the mode-specific settings for notes using [Rap Pitch Mode](../ai-functions/pitch-mode-rap.md#the-rap-intonation-parameter).

This parameter is always set on a per-note basis, so there are no associated default values in the Voice panel.

## Editing Parameter Curves

### Selecting a Parameter

Clicking on the current editing parameter label will open the parameter selection dropdown.

The currently selected parameter will be indicated with a checkmark, and any parameters with associated curves will be indicated in green.

Select a parameter or [vocal mode](../ai-functions/vocal-modes.md) to set it as the current editing parameter.

![Parameter Selection](../img/parameters/parameter-selection.png)

!!! warning

    It is recommended to enable [Manual Pitch Mode](../advanced/pitch-mode-manual.md) for notes before adding manual changes via the Pitch Deviation parameter.

    Notes that are in [Sing](../ai-functions/pitch-mode-sing.md) or [Rap](../ai-functions/pitch-mode-rap.md) pitch modes will have their base pitch re-generated if the note's context changes, which can cause your manual pitch deviations to become meaningless; the parameter curve will remain, however the base curve it was being combined with will have changed.

### Pointer Tool (point-based)

All parameter curves are composed of points (sometimes referred to as "nodes") and the interpolated lines joining them.

The pointer tool (++alt+1++) can add and move points, and is suited to creating smooth curves and making adjustments to existing curves.

Double click to add a point.

![Add a Point](../img/parameters/place-point.png)

![Add a Point](../img/parameters/place-point-2.png)

The pointer tool can also select points and move them, just like with notes in the piano roll.

![type:video](../img/parameters/move-points.mp4)

#### Point Movement Modifiers

Modifier keys can be held to change the behavior of dragging point(s) with the mouse.

|Held Modifier|Behavior|
|---|---|
|++shift++|Vertical movement only|
|++ctrl++|Horizontal movement only|
|++shift+ctrl++|Fine control with no snapping to zero|

### Pencil Tool (freehand)

The pencil tool (++alt+2++) allows you to draw the curve directly by clicking and holding down the left mouse button as you draw with the cursor.

This can be used to customize a note transition, draw unique vibrato, or introduce a variety of pitch deviations to achieve your desired singing style.

![type:video](../img/parameters/freehand-draw.mp4)

Holding right click will instead clear any curves along the area the mouse passes over.

![type:video](../img/parameters/freehand-clear.mp4)

### Line Tool

The line tool (++alt+3++) will introduce two points, one at each end of the line drawn with the mouse.

If either end of the drawn line is in proximity to an existing point, the existing point will be moved to the spot where the line began or ended.

![type:video](../img/parameters/line-draw.mp4)

### Curve Types

The curve type setting changes how the curves between points are interpolated.

The first setting (Linear) will draw straight lines between the points.

The second (Cosine) will ensure a horizontal line on either side of a point before curving toward the neighboring points.

The third and final type (Adaptive Spline) will produce the smoothest curve connecting each point.

<figure markdown>
  ![Add a Point](../img/parameters/curve-types-crop.png)
  <figcaption>A comparison of interpolation types</figcaption>
</figure>

### Automation Indicator

Any parameters that have curves associated with them will have an automation indicator in the Voice panel as a reminder that the parameter is being modified from its base value.

![Automation Indicator](../img/parameters/automation-indicator.png)

The actual value of a parameter (the base value plus the parameter curve) will be displayed on the slider in the Voice panel based on the current playhead position, and will reflect the real-time value of the parameter during playback.

![type:video](../img/parameters/parameter-live-visualizer.mp4)

## Additional Functions

Additional options for parameter editing can be found in the "Editor" section of the Settings panel.

![Parameter Options](../img/parameters/parameter-options.png)

Hide points in freehand mode
: When the pencil tool is selected, the dots for each individual point will be hidden.

Auto-insert anchor points
: If a point is placed within the duration of a note and no nearby points are present, anchor points will be placed before and after the note.

Simplify freehand drawn curves
: Automatically simplify curves drawn with the pencil tool. This will reduce the number of points and may improve performance, but also may cause the final curves to not follow the freehand line precisely.

Snap points to zero
: May need to be disabled if moving points to precise values near zero.

### Select Parameters for Notes

The Select Parameters for Notes option can be found under the "Edit" top menu, as well as by right clicking on selected notes.

This function will select all parameter points for the currently selected notes. The parameter points for all parameter types will be selected, even if they are not visible in the Parameters panel.

This is especially helpful when copying or grouping a sequence while retaining the associated parameter curves.

See [Editing Notes](../quickstart/editing-notes.md#selecting-notes) for methods of selecting many notes at once using hotkeys and modifier keys.

![type:video](../img/parameters/move-params-with-notes.mp4)

### Simplify Parameters

The Simplify Parameters option can be found under the "Modify" top menu (default ++alt+s++).

This function reduces the number of points in a selection to smooth a curve, at the cost of precision. The resulting curve may not match the original exactly.

![type:video](../img/parameters/simplify-parameter-curve.mp4)

## Video Demonstration

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/agSYwd_LQZU" title="YouTube video player" frameborder="0" allowfullscreen></iframe>

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: Editing Parameters])