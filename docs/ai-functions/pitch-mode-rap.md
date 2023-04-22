# Pitch Mode: Rap

"Rap" Pitch Mode will add AI-generated pitch deviations to your notes which are modeled to mimic human rap techniques, and allows the use of the Rap Intonation parameter.

!!! warning

    Rap Mode is only available for English and Mandarin Chinese. Japanese support is currently in development.

## Enabling Rap Mode

Rap mode can be enabled for notes from the Note Properties menu. Notes using Rap mode will be red in the Piano Roll.

![Rap Mode](../img/ai-functions/pitch-mode-rap.png)

!!! info

    The pitch deviations introduced by Rap Mode are context-specific.

    A note's "context" is based on its pitch, duration, and phonemes, as well as those same properties of the notes before and after it. If any of these things change, the pitch deviations for the note will be recalculated.

Enabling Rap Mode also allows the use of pitch [AI Retakes](ai-retakes.md).

### Rap Accent

The Rap Accent dropdown can be used to produce variations of a note.

This option is only available for Mandarin Chinese.

![Rap Accent dropdown](../img/ai-functions/rap-accent.png)

### Intonation

Causes the pitch of the note to rise or fall over its duration.

The value of this slider is directly linked to the upward or downward curve of the Rap Intonation parameter for the note.

![type:video](../img/ai-functions/rap-intonation-slider.mp4)

### Tone

Modifies the overall pitch of the note to be higher or lower, without affecting the change in intonation over its duration. The value is represented in semitones.

The value of this slider is directly linked to the vertical position of the Rap Intonation parameter for the note.

![type:video](../img/ai-functions/rap-tone-slider.mp4)

## The Rap Intonation Parameter

The Rap Intonation parameter allows easy editing of pitch movement and intonation throughout a note or phrase. Unlike other parameters, Rap Intonation is represented as a series of arrows rather than a continuous curve.

![The Rap Intonation Parameter](../img/parameters/rap-intonation.png)

Each arrow represents the pitch movement over the duration of the associated note. The position of each arrow is directly linked to the sliders in the Note Properties panel.

To modify the arrow's vertical position (Tone), click and drag the line portion of the arrow. To change the curve (Intonation), click and drag the head of the arrow instead.

![type:video](../img/parameters/rap-intonation.mp4)

## Video Demonstration

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Z6OB3jHiBBk" title="YouTube video player" frameborder="0" allowfullscreen></iframe>

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: Rap Pitch Mode])