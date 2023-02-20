# Instant Mode

While Instant Mode is active, [Auto Pitch Tuning](auto-pitch-tuning.md) will be executed on the notes as you work. This uses AI-generated pitch deviations to create realistic transitions, sustains, and vibrato.

## Using Instant Mode

Instant Mode affects the entire project and behaves very similarly to auto pitch tuning, with some main exceptions:

- Pitch deviations introduced by Instant Mode do not appear in the parameters panel. This keeps the automatic pitch deviations separate from your manual ones.
- Expressiveness is determined by the slider in the [AI Retakes](ai-retakes.md) panel (Pro edition only). This can be adjusted for all notes, or only selected notes.

Instant Mode can be enabled with the button in the upper right corner of the Piano Roll.

!!! info

    The pitch deviations introduced by Instant Mode are context-specific.

    A note's "context" is based on its pitch, duration, and phonemes, as well as those same properties of the notes before and after it. If any of these things change the pitch deviations for the note will be recalculated.

![Instant Mode options](/img/ai-functions/instant-mode.png)

Enabling Instant Mode also allows the use of pitch [AI Retakes](ai-retakes.md).

## Pre-existing Pitch Deviations and Vibrato

Pre-existing pitch deviations entered via the parameters panel will not be overwritten by Instant Mode.

Any notes with an unmodified vibrato depth setting in the Note Properties panel will have their vibrato depth set to zero, such that the expression-based vibrato will not interfere with the AI-generated pitch deviations.

If a note's vibrato depth slider has been manually set, it will not be overwritten.

![Vibrato Depth Set to Zero](/img/ai-functions/instant-mode-vibrato-depth.png)

## Disabling Instant Mode

Clicking the Instant Mode button while it is enabled will disable Instant Mode for the entire project.

When this occurs, all generated pitch deviations (including the currently-selected AI Retakes) will be persisted to the parameters panel. These pitch deviations will be combined with any manually-created curves already present in the parameters panel to produce a resultant pitch line that is the same as before disabling Instant Mode.

After disabling Instant Mode you will no longer be able to choose different AI Retakes and the pitch deviations will no longer be recalculated if a note's context changes.

![Instant Mode Disabled](/img/ai-functions/instant-mode-disabled.png)

## Default Instant Mode Setting

Instant Mode will be enabled for new projects by default. To create new projects with Instant Mode disabled, uncheck "Enable instant mode by default" in the Settings panel.

![Default Instant Mode Setting](/img/ai-functions/instant-mode-default.png)

## Video Demonstration

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Yb8m_HmBEt4" title="YouTube video player" frameborder="0" allowfullscreen></iframe>

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: Instant Mode])