# Frequently Asked Questions

Below are common questions not answered elsewhere in the documentation.

---

### Can I use Synthesizer V Studio for commercial purposes?
Yes, both the Basic and Pro editions can be used for commercial purposes with no limit on revenue.

Each voice database has separate terms. You can find the license for each voice database in its installation directory.

The terms for Dreamtonics voice databases can be found on the [Dreamtonics website](https://dreamtonics.com/en/terms/).

### What is the difference between "Basic" and "Pro"?

The Basic edition of Synthesizer V Studio has a limited feature set compared to the Pro edition. The list of features that are limited or unavailable in the Basic edition can be found on the store page for [Synthesizer V Studio Pro](https://store.dreamtonics.com/product/editor-svstudio-pro/).

This documentation will indicate where the Pro edition is required to use a feature (such as on the [Vocal Modes](ai-functions/vocal-modes.md) page).

### What are "Lite" voice databases?
Lite voice databases are lower quality versions of paid products, which are available for free but have limited functionality.

- No vocal mode support
- No cross-lingual support
- Reduced vocal range
- Lower quality output (more noise/artifacts)
    - Lite voice databases are restricted to the "Prefer Speed" render mode in the Voice panel

Lite voice databases are subject to the following terms:

- You may not use the Lite version for commercial purposes
- You may not publish your work using the Lite version on behalf of an organization
- If you wish to publish a work creating using the Lite version, you must clearly state the name of the voice database used and the fact that a Lite version is used
- You should acknowledge that the Lite version does not represent the quality of the full version of the same voice database. Dreamtonics makes no quality or quantity guarantee on the Lite version of a voice database.

### The original manual has a page for "Glottal Effects", why can't I find anything about that here?
Glottal effects have not yet been implemented for Synthesizer V Studio.

### Why are the vibrato sliders doing nothing?

Certain automated processes such as [Auto Pitch Tuning](ai-functions/auto-pitch-tuning.md) and [Instant Mode](ai-functions/instant-mode.md) will set the vibrato depth for each note to zero. Notes with manual settings will not be changed, but those which have had their depth set to zero will no longer inherit that value from the defaults in the Voice panel.

Ensure the note you are modifying does not have a vibrato depth of zero in the Note Properties panel, and that the start of the vibrato does not occur after the note's duration.

If the vibrato depth for the notes is set to zero the [Vibrato Envelope](parameters/editing-parameters.md#vibrato-envelope) parameter will also have no effect, since it is applying a multiplier to the depth value (which is zero).

### The keyboard combinations aren't working on Mac, why?

Mac has a slightly different keyboard layout than other devices. Generally where you see ++ctrl++ Mac users will want to press ++cmd++ instead, and where you see ++alt++ it's usually ++opt++ on Mac.

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: FAQ])