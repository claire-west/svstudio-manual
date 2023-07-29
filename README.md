# svstudio-manual
An unofficial user manual for Synthesizer V Studio.

## Dev Environment

1. Run `setup.sh` to install prerequisites (may need to run with `sudo`)
2. Run `mkdocs serve` in the root directory (future runs can use `mkdocs serve --dirtyreload` for faster rebuilds during development)
3. Navigate to http://localhost:8000

This assumes you already have `pip`. Some of the packages added in `setup.sh` will be named/aliased differently based on your package manager or linux distribution, so you might have to install them one-by-one or with a different command (for example, `zlib1g-dev` might need to be installed as `libz-dev`).

This works with WSL, so there is no plan for a Windows setup.

## Translation

If you would like to contribute translations for a language, refer to the respective repository. If the language you are translating to does not have a repository yet, [create an Issue](https://github.com/claire-west/svstudio-manual/issues/new) in this repository to have it created.

|Language|Repository|URL|Primary Contributor or Translator|
|---|---|---|---|
|English|[svstudio-manual](https://github.com/claire-west/svstudio-manual)|https://manual.synthv.info|[Claire](https://github.com/claire-west)|
|Chinese (中文)|[svstudio-manual-zh](https://github.com/claire-west/svstudio-manual-zh)|https://zh.synthv.info|[Blathroat](https://github.com/Blathroat)|