# User Dictionaries

Dictionaries can be used to customize word-to-phoneme conversion.

When a note's lyric is being converted to phonemes, it will first check for an entry in the currently selected dictionary. If there is no custom entry or no dictionary is selected, the default conversion will be used. This can be useful if the same word appears many times in a project and you want all instances of that word to use a modifies phoneme sequence.

The Dictionary panel can be accessed from the side menu.

![The Dictionary Panel](/img/advanced/dictionary-panel.png)

## Creating a Dictionary

To create a dictionary, open the Dictionary panel and click "New".

![Creating a Dictionary](/img/advanced/dictionary-new.png)

## Adding Dictionary Entries

Add dictionaries by entering the word and the desired phoneme sequence to be used.

![Adding a Dictionary Entry](/img/advanced/dictionary-new-entry.png)

Once a word is present in the active dictionary, all instances of that word in the track/group will use the new phoneme sequence, unless their phonemes have been set manually. Notice that the phoneme text above the note is white to indicate that it is based on lyric-to-phoneme conversion rather than manual entry.

![Dictionary Phoneme Conversion](/img/advanced/dictionary-conversion.png)

### Removing Dictionary Entries

To remove a dictionary entry, select it from the list and select "Remove".

![Dictionary Phoneme Conversion](/img/advanced/dictionary-remove.png)

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: User Dictionaries])