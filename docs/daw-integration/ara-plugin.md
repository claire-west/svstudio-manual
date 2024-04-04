# Deep ARA Integration and ARA Bridge

!!! note "Pro Feature"

    The features described below require Synthesizer V Studio Pro.

## DAW Compatibility

Not all DAWs offer the same level of ARA support. Some hosts will offer significantly enhanced integration with the plugin, while others will only support the plugin in ARA Bridge mode, primarily providing improved playback and tempo synchronization without the deeper project structure synchronization.

||Deep ARA Integration|ARA Bridge|
|---|---|---|
|Studio One 5/6 (Artist/Pro)|Yes|Yes|
|Cubase 12/13 (Artist/Pro)|Yes|Yes|
|Reaper 6|Yes|Yes|
|Cakewalk|Yes|Yes|
|Ability 5 Pro|Yes|Yes|
|Logic Pro (Rosetta/x86)|No|Yes|
|Logic Pro (Apple Silicon)|No|No|
|[Other ARA2-compatible DAWs](https://en.wikipedia.org/wiki/Audio_Random_Access#Digital_audio_workstations)|No|Yes* (not verified by Dreamtonics)|

!!! info

    The ARA plugin does not fully replace the regular VSTi/AU instrument plugin. Each plugin will be suited to different scenarios.

    Even though they can produce audio output, ARA plugins are not added to the DAW as instruments; they are applied to individual tracks as effects or track extensions, depending on the DAW. They primarily modify or replace the original audio clips in the DAW track they are assigned to, and it is assumed that an ARA plugin will have access to an audio clip as its input.

    The VSTi/AU instrument still benefits from the improved playback and tempo synchronization of the ARA bridge, and will be better suited to situations where you are creating the vocals entirely within Synthsizer V Studio, without using an audio clip in the DAW as a starting point.

    If your project contains some Synthesizer V Studio tracks based on audio clips, and others that are not, you may want to utilize both plugins within the same DAW project.

## Setup and Core Functionality

For setup and usage information about the Synthesizer V Studio ARA plugin, refer to the official guidance from Dreamtonics: [Synthesizer V Studio ARA Plugin Guide](https://docs.google.com/document/d/e/2PACX-1vTx9WXhLQT9UIhMaN9OCLhAF36-vEi7c9syl54DKKJ-BBkaHBSbQTXzyC2F5Rnm-E1EkRWF8pA7I9UI/pub).

It is recommended to add the ARA plugin to your project before adding any instances of the VSTi/AU instrument.

## Saving the Project

Unlike the VSTi/AU instrument, the ARA plugin's project data is always saved within the DAW project. To export project data, select "Save As" from the "File" top menu to save an SVP file.

This SVP file can then be opened in the standalone or VSTi/AU instrument versions of Synthesizer V Studio, or merged into an existing project with the "Import as Tracks" option, also under the "File" menu.

## Importing MIDI with ARA Functions

While the ARA plugin only maintains synchronization with audio clips rather than MIDI sequences, deep ARA integration can be used to quickly move MIDI from the DAW to the plugin without exporting and importing a MIDI file.

Assign a simple instrument (such as a sine tone) to the MIDI sequence and bounce the audio clip. Most DAWs will offer a quick method of doing this, usually labelled "render in place", "quick bounce", "consolidate/freeze track", or similar.

Once you have the audio clip of your MIDI sequence, execute [Voice-to-MIDI Conversion](../ai-functions/voice-to-midi.md) to transcribe it into Synthesizer V Studio and optionally execute "Smart Quantization" from the "Modify" top menu.

## Video Demonstration

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/0ijQ9nLPGe0" title="YouTube video player" frameborder="0" allowfullscreen></iframe>

## Troubleshooting

If you encounter technical issues with the plugin, try removing the software and reinstalling to the default installation directory.

If the problems persist, search for similar issues on the [official forums](https://forum.synthesizerv.com/search) or contact [Dreamtonics support](../support.md).

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: ARA Integration])