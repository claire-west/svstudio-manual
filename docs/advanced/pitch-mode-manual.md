# Manual Pitch Mode

Experienced users will often want the most manual control over the vocals, without influence from AI-generated behaviors.

Notes with a Manual pitch mode are blue in the Piano Roll and will have a flattened pitch line by default.

![Manual Pitch Mode setting](../img/advanced/pitch-mode-manual.png)

## Manual Pitch Settings

When Manual Pitch Mode is selected, additional transition and vibrato options are made available in the Note Properties panel.

The pitch transition and vibrato settings are meant for quickly setting up a rough pitch outline. The details are expected to be fine-tuned via the [Parameters Panel](../parameters/parameters-panel.md).

Pitch transition controls the part of pitch curve near note boundaries. Vibrato applies to the middle of a note.

The default values of the transition and vibrato sliders are determined by their respective settings in the Voice panel. Some settings can only be set for individual notes and do not have a matching default value set in the Voice panel.

## Pitch Transition

The first set of sliders are related to the transitions between notes.

<figure markdown>
  ![Transition Sliders](../img/note-properties/transition-sliders.png)
  <figcaption>Transition sliders in the Voice (left) and Note Properties (right) panels</figcaption>
</figure>

**Offset**
: Shifts the start of the pitch curve for a note left or right. This will also affect the right transition of the previous note. Offset will not affect the note's vibrato or transition to the following note.

**Duration Left**
: The amount of time between the start of the note and the point where the pitch curve reaches the note's exact pitch. This part of the pitch curve is often referred to as "undershoot", "overshoot", or "correction".

**Duration Right**
: The amount of time before the end of the note where the pitch deviates based on the "Depth Right" setting. This part of the pitch curve is often referred to as "preparation".

**Depth Left**
: Adjusts the pitch near the start of the note and the end of the transition based on the "Duration Left" setting. Negative values result in undershoot and positive values result in overshoot.

**Depth Right**
: Adjusts the pitch neat the end of the note based on the "Duration Right" setting. Negative values will pre-emptively adjust toward the next note and positive values will move away from the next note.

### Transition Settings Visualized

This diagram illustrates how each of the transition sliders affects the pitch curve at the boundary between Note A (lower left) and Note B (upper right).

![Transition Visualized](../img/note-properties/pitch-transition-visualized.png)

## Vibrato

The vibrato sliders produce a simple expression-based pattern similar to a sine wave, which can be used to quickly add vibrato to notes.

!!! note

    Other methods of creating vibrato such as [Auto Pitch Tuning](../ai-functions/auto-pitch-tuning.md) will create more complex vibrato patterns without using these settings, and those patterns will not be affected by the vibrato sliders or the [Vibrato Envelope](../parameters/editing-parameters.md#vibrato-envelope) parameter.

<figure markdown>
  ![Vibrato Sliders](../img/note-properties/vibrato-sliders.png)
  <figcaption>Vibrato sliders in the Voice (left) and Note Properties (right) panels</figcaption>
</figure>

**Start**
: The delay before vibrato begins, measured from the start of the note.

**Left**
: The duration of the ease-in behavior before the vibrato reaches its full amplitude.

**Right**
: The duration of the ease-out behavior where the vibrato curve ends at the tail of the note.

**Depth**
: The amplitude (in semitones) of the sine-like curve.

!!! warning

    Executing [Auto Pitch Tuning](../ai-functions/auto-pitch-tuning.md) or enabling [Instant Mode](../ai-functions/instant-mode.md) will set the vibrato depth of all notes to zero, except for notes which have already had their vibrato depth set manually in the Note Properties panel. Once this has happened the vibrato depth will no longer be inherited from the default set in the Voice panel.

    To continue using the vibrato sliders, increase the vibrato depth in the Note Properties panel for the relevant notes.

**Frequency**
: How fast the vibrato oscillates (cycles per second).

**Phase**
: The phase of the sine-wave-like vibrato at its beginning, relative to a full cycle.

**Jitter**
: How much natural pitch fluctuation is added to the pitch curve (non-AI singers only).

### Vibrato Settings Visualized

This diagram illustrates how each of the vibrato sliders affects the pitch curve for a note. The pitch curve before and after the vibrato is based on the Pitch Transition settings described above.

![Vibrato Visualized](../img/note-properties/vibrato-visualized.png)


---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: Manual Pitch Mode])