# MIDI Controller Support

!!! note "Pro Feature"

    The features described below require Synthesizer V Studio Pro.

You can record melodies to the piano roll in real-time using a MIDI controller.

## Setup
Select your MIDI controller in the "Audio" section of the Settings panel.

![MIDI Controller Selection](/img/advanced/midi-controller.png)

## MIDI Recording
To begin recording, click the record button in the transport controls located at the top of the piano roll or arrangement panel (whichever is focused by user input).

You may also want to enable the metronome option to the left of the Play button.

Stop recording by pressing the record button again, the stop button, or by pressing ++space++.

![Record Button and Metronome](/img/advanced/record-button.png)

After recording your melody, a dialog window will prompt for additional action.

![MIDI Recording Dialog](/img/advanced/midi-record-dialog.png)

"Snap to Grid" will quantize the note lengths based on the current grid snap setting.

"Smart Quantization" will estimate a grid snap setting appropriate to your recorded input, instead of using the current snap setting.

![MIDI Recording Dialog](/img/advanced/midi-record-dialog-2.png)

After pressing "OK", the note timings will be set to the appropriate lengths.

To leave the notes at their recorded timings, click "Cancel" to abort the dialog.

Snap to Grid and Smart Quantization can be executed at any time via the "Modify" top menu.

![Quantized Notes](/img/advanced/midi-record-quantized.png)

## Recording Options
The Settings panel has some additional settings for MIDI recording, such as whether to play the metronome sound during normal playback, and whether to overwrite existing notes while recording.

![Recording Options](/img/advanced/midi-recording-options.png)

## MMC Support
If your MIDI controller has playback controls, these can be used to navigate the piano roll and trigger playback within Synthesizer V Studio.

## Video Demonstration

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/KxwLaLn4zbY" title="YouTube video player" frameborder="0" allowfullscreen></iframe>

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: MIDI Controller])