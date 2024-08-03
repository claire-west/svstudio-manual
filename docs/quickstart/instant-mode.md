--8<--
notice.md
--8<--

# Introduction to Instant Mode

!!! danger "Outdated Information"

    Instant Mode is no longer part of Synthesizer V Studio.

    Refer to [Pitch Mode: Sing](../ai-functions/pitch-mode-sing.md) for the feature that replaced it in version 1.9.0.

While adding and modifying notes you may notice that the pitch line does not follow the exact positions of the notes. This indicates that you have [Instant Mode](../ai-functions/instant-mode.md) enabled for your project.

## What is Instant Mode?

Instant Mode will add AI-generated pitch deviations to your notes which are modeled to mimic human singing techniques.

In some ways, Instant Mode is comparable to the preset libraries included with traditional software synthesizers and effects plugins; it offers a simplified workflow which can help inexperienced users get results quickly, and acts as a starting point for learning what realistic pitch curves might look and sound like.

<figure markdown>
  ![Without and With Instant Mode](../img/quickstart/instant-mode-without-and-with.png)
  <figcaption>The default pitch curve (left) and the same notes with Instant Mode enabled (right)</figcaption>
</figure>

If you do not want to use the simplified workflow offered by Instant Mode, and prefer more manual control, you may wish to disable it with the button in the upper right corner of the piano roll.

Instant Mode can be disabled by default for new projects by changing the "Enable instant mode by default" option in the Settings panel.

![Toggling Instant Mode](../img/quickstart/instant-mode-button.png)

## Removing Instant Mode From an Existing Project

If you have already been working on your project, disabling Instant Mode will not remove all of the pitch changes it added.

Disabling Instant Mode will stop it from generating new patterns, but existing patterns will be moved to the Parameters panel for manual editing. This topic will be discussed later in the user manual, but for now you can remove any remaining patterns with the following steps:

1. Expand the Parameters panel, if it is not already open. If there is no Parameters panel below the piano roll, you can open a new one from the three-bars (:fontawesome-solid-bars:) button beside the Instant Mode button shown above.
2. Ensure the "EDIT:" setting is set to "Pitch Deviation".
3. Click within the Parameters panel and press ++ctrl+a++ to select all points.
4. Press ++del++.

![type:video](../img/quickstart/delete-parameter-points.mp4)
