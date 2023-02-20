# DAW Integration

!!! note "Pro Feature"

    The features described below require Synthesizer V Studio Pro.

You can use Synthesizer V Studio Pro in a DAW (digital audio workstation) software as a VSTi or AudioUnit plugin.

## Project Saving

When Synthesizer V Studio is used as an instrument in a DAW, an additional setting is added under the "File" top menu.

If "Save Inside Host" is selected, the Synthesizer V Studio project (SVP) file will be embedded within the DAW project.

To save an external SVP file separate from your DAW project, select "Save to External File" instead.

![Save Inside Host option](/img/daw-integration/save-inside-host.png)

## Synchronize Tempo with Host

An additional setting is added under the "Project" top menu.

![Sync Tempo option](/img/daw-integration/sync-tempo.png)

By selecting "Synchronize Tempo with Host", tempo markers will be added to the Synthesizer V Studio project matching those of the DAW's project.

## Output Channels

The output of Synthesizer V Studio can be routed to one or many channels based on the option chosen in the Settings Panel. This allows you to apply different effects to each track while using Synthesizer V Studio as a plugin.

![Output Channels option](/img/daw-integration/output-channels.png)

Master Combined
: A single channel is used for all audio output.

Master Aspiration Isolated
: Two channels are used, one for the main output of all tracks and a second for the isolated aspiration of all tracks.

Track Combined
: One channel is used for each track.

Track Aspiration Isolated
: Two output channels are used for each track, one for the main output and the other for the isolated aspiration.

## Video Demonstration

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/jMm7piaJ0ss" title="YouTube video player" frameborder="0" allowfullscreen></iframe>

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: DAW Integration])