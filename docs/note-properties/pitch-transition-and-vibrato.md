# Pitch Transition and Vibrato

The pitch transition and vibrato settings in the Note Properties panel are meant for quickly setting up a rough pitch outline. The details are expected to be fine-tuned via the [Parameters Panel](../parameters/parameters-panel.md).

Pitch transition controls the part of pitch curve near note boundaries. Vibrato applies to the middle of a note.

The default values of the transition and vibrato sliders are determined by their respective settings in the Voice panel.

!!! note

    The vibrato created using these sliders produces a simple expression-based pattern. Other methods of creating vibrato such as [Auto Pitch Tuning](../ai-functions/auto-pitch-tuning.md) and [Instant Mode](../ai-functions/instant-mode.md) will create more complex vibrato patterns without using these settings, and those patterns will not be affected by the vibrato sliders or the [Vibrato Envelope](../parameters/editing-parameters.md#vibrato-envelope) parameter.

!!! warning

    Executing [Auto Pitch Tuning](../ai-functions/auto-pitch-tuning.md) or enabling [Instant Mode](../ai-functions/instant-mode.md) will set the vibrato depth of all notes to zero, except for notes which have already had their vibrato depth set manually in the Note Properties panel. Once this has happened the vibrato depth will no longer be inherited from the default set in the Voice panel.

    To continue using the vibrato sliders, increase the vibrato depth in the Note Properties panel for the relevant notes.

![Transition and Vibrato Sliders](/img/note-properties/pitch-transition-and-vibrato-sliders.png)

## Transition and Vibrato Visualized

<figure markdown>
  ![Visual Diagram of Each Slider](/img/note-properties/pitch-transition-and-vibrato-breakdown.png)
  <figcaption>Diagram from the legacy manual for Synthesizer V (2018)</figcaption>
</figure>

### Other Vibrato Properties
**Phase**
: The phase of the sine-wave-like vibrato at its beginning, relative to a full cycle.

**Frequency**
: How fast the vibrato oscillates (cycles per second).

**Jitter**
: How much natural pitch fluctuation is added to the pitch curve (non-AI singers only).

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: Transition and Vibrato])