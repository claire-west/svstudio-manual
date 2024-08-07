--8<--
notice.md
--8<--

# Entering Lyrics

![Note Lyrics and Special Symbols](../img/quickstart/note-lyrics.png)

### 1. Lyric Entry
Double click on a note to enter a lyric. Press ++enter++ or click outside the note to confirm, or press ++esc++ to cancel the change.

Pressing ++tab++ will confirm the change and advance to the next note, while ++ctrl+tab++ will move to the previous note.

!!! note

    When entering Japanese or Chinese lyrics, it is recommended to only include one mora or character per note.

### 2. Syllable Break
Use the plus sign (`+`) to distribute a multi-syllable word across multiple notes.

!!! note

    It is generally best practice to not include more than one syllable per note. When working in English or Spanish, use of syllable breaks is often critical to accomplishing the desired lyrical timing.

    When working in Japanese or Chinese there will typically only be one mora/syllable per note, rendering the need for explicit syllable breaks unnecessary.

### 3. Legato
Use the minus sign (`-`) to continue the last sung vowel into the following note.

## Combining Syllable Breaks and Legato
Multi-syllable words and melismas may require a combination of syllable breaks (`+`) and legato (`-`).

In this example the word "amazing" has its three syllables extended across six notes.

|Note|Lyric/Symbol|Syllable|
|---|---|---|
|1|amazing|First|
|2|`-` (minus)|First (continued)|
|3|`+` (plus)|Second|
|4|`+` (plus)|Third|
|5|`-` (minus)|Third (continued)|
|6|`-` (minus)|Third (continued)|

![Multi-syllable Lyrics](../img/quickstart/multi-syllable-lyrics.png)

## Adding Breaths

Breath notes can be added by entering `br` as the note's lyric (AI singers only).

![A Breath Note](../img/quickstart/breath-note.png)

## Adding Glottal Stops

Glottal stops can be added between notes by prefixing the following lyric with a single quote (`'`). A note containing just a single quote can be used to add a glottal stop at the end of a phrase.

![Glottal Stops](../img/quickstart/glottal-stop.png)

### Hard Onsets

While a "glottal stop" is, strictly speaking, the sudden termination of airflow (and the resulting sound), the same symbol can be used in Synthesizer V Studio to create hard onsets, by using the single quote (`'`) notation at the start of a phrase.

## Adjusting Pronunciation

It is rare for human vocalists to sing every lyric with perfect enunciation, so the default pronunciation of the entered lyrics will not always produce the desired result.

After completing the Quickstart section it is recommended to familiarize yourself with [Phoneme Editing](../note-properties/editing-phonemes.md) in order to achieve your desired pronunciation where necessary.

## Video Demonstration

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Gj7UipbHBdw" title="YouTube video player" frameborder="0" allowfullscreen></iframe>

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: Entering Lyrics])
