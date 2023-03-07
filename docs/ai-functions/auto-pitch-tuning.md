# Auto Pitch Tuning

Auto pitch tuning is a function found under the "Auto-Process" top menu. The "(Customized Style)" option offers additional vibrato and overshoot sliders when using the Pro edition.

![Auto-Process Menu](../img/ai-functions/auto-pitch-tuning-option.png)

![Auto Pitch Tuning Dialog](../img/ai-functions/auto-pitch-tuning-dialog.png)

## Executing Auto Pitch Tuning

Executing auto pitch tuning will add pitch deviations to the parameters panel for the currently-selected notes. These pitch deviations will be different based on the currently selected voice database, and are based on machine learning analysis of the original voice provider's singing style.

![Auto Pitch Tuning](../img/ai-functions/auto-pitch-tuning.png)

The pitch deviations introduced by Auto Pitch Tuning are context-specific.

A note's "context" is based on its pitch, duration, and phonemes, as well as those same properties of the notes before and after it. If any of these things change, the results of auto pitch tuning will be different.

### Expressiveness
The expressiveness slider determines how drastic the pitch deviations are and how far they deviate from the notes.

<figure markdown>
  ![Expressiveness Side-by-side](../img/ai-functions/auto-pitch-tuning-expressiveness-crop.png)
  <figcaption>Expressiveness setting of 100 (left) and 25 (right)</figcaption>
</figure>

### Rerun with New Random Seed

The "Rerun with New Random Seed" option will generate a different pitch curve, even if the note's context has not changed. This can be used to cycle through different "takes".

### Customized Style Sliders

!!! note "Pro Feature - Auto Pitch Tuning (Customized Style) is only available in Synthesizer V Studio Pro."

!!! warning "Speculative Information"

    There is no clear guidance from Dreamtonics about this topic. The information below is based on user observation and may not be entirely accurate.

When executing the "Customized Style" version of Auto Pitch Tuning, additional sliders will be added to the dialog in addition to the usual expressiveness slider.

![Customized Style Dialog](../img/ai-functions/auto-pitch-tuning-customized-style.png)

#### Vibrato 1

"Strong" settings will result in the AI engine being more "choosy" when applying AI-generated pitch deviations (both vibrato and overshoot). "Weak" settings will allow pitch deviations to be applied to more notes, more intensely.

#### Vibrato 2

Affects the intensity of AI-generated vibrato.

#### Overshoot

Affects the intensity of pitch deviations extending past the note before and after pitch transitions.

![Overshoot](../img/ai-functions/overshoot.png)


---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: Auto Pitch Tuning])