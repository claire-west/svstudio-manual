# Editing Parameters

Parameters offer detailed manual control over various aspects of a vocal sequence.

## Parameter Types

**Pitch Deviation**
: A layer of pitch shifts added to the base pitch curve.

**Vibrato Envelope**
: Amplitude modulation of expression-based vibrato.

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
: Modifies the tone of the voice. Effects may vary with each voice database.

!!! note "Pro Feature - Tone Shift is only available in Synthesizer V Studio Pro."

## Base Values

The base value of most parameters can be set in the Voice panel. The curves in the parameters panel will modify the value from this base setting.

![Base Parameter Sliders](/img/parameters/voice-parameters.png)

### Vibrato Envelope

The Vibrato Envelope parameter affects the amplitude (depth) of expression-based vibrato in its duration.

Rather than a base value set in the Voice panel, the curve modifies the vibrato depth setting of the note as defined in the Note Properties panel.

![Add a Node](/img/parameters/vibrato-envelope.png)

## Editing Parameter Curves

### Pointer Tool (node-based)

All parameter curves are composed of nodes and the interpolated lines joining them.

The pointer tool can add and move nodes, and is suited to creating smooth curves and making adjustments to existing curves.

Double click to add a node.

![Add a Node](/img/parameters/place-node.png)

![Add a Node](/img/parameters/place-node-2.png)

The pointer tool can also select nodes and move them, just like with notes in the piano roll.

<video width="360" height="480" controls>
    <source src="/img/parameters/move-nodes.mp4" type="video/mp4">
    Moving Nodes
</video>

### Pencil Tool (freehand)

The pencil tool allows you to draw the curve directly by clicking and holding down the left mouse button as you draw with the cursor.

This can be used to customize a note transition, draw unique vibrato, or introduce all sorts of pitch deviations to mimic the desired singing style.

<video width="360" height="480" controls>
    <source src="/img/parameters/freehand-draw.mp4" type="video/mp4">
    Drawing Parameters
</video>

Holding right click will instead clear any curves along the area the moust passes over.

<video width="360" height="480" controls>
    <source src="/img/parameters/freehand-clear.mp4" type="video/mp4">
    Clearing Parameters
</video>

### Line Tool

The line tool will introduce two points, one at each end of the line drawn with the mouse.

<video width="360" height="480" controls>
    <source src="/img/parameters/line-draw.mp4" type="video/mp4">
    Using the Line Tool
</video>

### Curve Types

The curve type setting changes how the curves between nodes are interpolated.

The first setting will draw straight lines between the points.

The second will ensure a horizontal line on either side of a node before curving toward the neighboring nodes.

The third and final type will produce the smoothest curve connecting each node.

<figure markdown>
  ![Add a Node](/img/parameters/curve-types-crop.png)
  <figcaption>A comparison of interpolation types</figcaption>
</figure>

## Additional Functions

Additional options for parameter editing can be found in the "Editor" seciton of the Settings panel.

![Parameter Options](/img/parameters/parameter-options.png)

Hide points in freehand mode
: When the pencil tool is selected, will not display dots for each individual node.

Auto-insert anchor points
: If a node is placed within the duration of a note and no nearby nodes are present, anchor nodes will be placed before and after the note.

Simplify freehand drawn curves
: Automatically simplify curves drawn with the pencil tool. This will reduce the number of nodes and may improve performance, but also may cause the final curves to not follow the freehand line precisely.

Snap points to zero
: May need to be disabled if moving nodes to precise values near zero.


### Simplify Parameters

The Simplify Parameters option can be found under the "Modify" top menu.

This function reduces the number of nodes in a selection to smooth a curve, at the cost of precision. The resulting curve may not match the original exactly.

<video width="360" height="480" controls>
    <source src="/img/parameters/simplify-parameter-curve.mp4" type="video/mp4">
    Simplifying a Parameter Curve
</video>

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: Editing Parameters])