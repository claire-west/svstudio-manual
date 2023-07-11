# Frequently Asked Questions

Below are common questions not answered elsewhere in the documentation.

---

## About Synthesizer V Studio

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
- Less natural generated pitch patterns

Lite voice databases are subject to the following terms:

- You may not use the Lite version for commercial purposes
- You may not publish your work using the Lite version on behalf of an organization
- If you wish to publish a work created using the Lite version, you must clearly state the name of the voice database used and the fact that a Lite version is used
- You should acknowledge that the Lite version does not represent the quality of the full version of the same voice database. Dreamtonics makes no quality or quantity guarantee on the Lite version of a voice database.

### What are "FLT" voice databases?
"Feature-Limited Trial" voice databases are free versions of paid products with a limited set of features, however they are different from "lite" voice databases in that they do not have reduced output quality. FLT voice databases are primarily used as preview versions of in-development products (as opposed to "lite" voice databases which are restricted version of released products).

- A maximum of one track for each FLT voice.
- Export: output limited to the first 45 seconds.
- AI Retakes: Pitch retakes only.
- Vocal Mode and Cross-Lingual Synthesis: limited options.
- Use in the standalone editor only.
- Non-commercial usage only.

### Where are my settings saved?

Settings are saved in a file called `settings.xml`. You can find this in the following locations based on your operating system:

|Operating System|File Location|
|---|---|
|Windows|`Documents\Dreamtonics\Synthesizer V Studio\settings`|
|MacOS|`/Library/Application Support/Dreamtonics/settings`|
|Linux|`<your installation directory>/settings`<br/>For example:<br/>`/opt/Synthesizer V Studio Pro/settings/settings.xml`|

If the software settings are not being saved successfully, or are reset each time the software launches, this is usually because the application does not have suitable permissions to access this folder. This can be resolved by either reinstalling the software, or granting the appropriate file permissions.

### Where is the "Track Manager"?

The original version of Synthesizer V had a separate window for managing tracks. In Synthesizer V Studio, all [track management](quickstart/managing-tracks.md) is done via the Arrangement panel.

### The original manual has a page for "Glottal Effects", why can't I find anything about that here?

Glottal effects have not yet been implemented for Synthesizer V Studio.

## About This Website

### The keyboard combinations aren't working on Mac, why?

Mac has a slightly different keyboard layout than other devices. Generally where you see ++ctrl++ Mac users will want to press ++cmd++ instead, and where you see ++alt++ it's usually ++opt++ on Mac.

### Why do some examples show notes in Manual Pitch Mode, but they don't have an indicator in the corner?

Pitch modes were handled differently prior to version 1.9.0, and there was no note-level indicator because the AI-generated pitch deviations ("Instant Mode") were a project-wide setting.

### How can I access the manual offline?

You can download an offline version of the manual by following the download link below. You must unzip the folder and then open the "index.html" file in your web browser.

Keep in mind that unlike the online version, the offline manual will need to be redownloaded to see any updates or corrections. This can be done by extracting the latest zip download to the same location (overwriting the older files).

A PDF version is also available, however due to the format it does not include video examples or have the benefit of an improved navigation/serach system.

[Download](https://github.com/claire-west/svstudio-manual/releases/tag/latest){ .md-button }

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: FAQ])