# svstudio-manual
An unofficial user manual for Synthesizer V Studio.

### Dev Environment

1. Run `setup.sh` to install prerequisites (may need to run with `sudo`)
2. Run `mkdocs serve` in the root directory (future runs can use `mkdocs serve --dirtyreload` for faster rebuilds during development)
3. Navigate to http://localhost:8000

This assumes you already have `pip`. Some of the packages added in `setup.sh` will be named/aliased differently based on your package manager or linux distribution, so you might have to install them one-by-one or with a different command (for example, `zlib1g-dev` might need to be installed as `libz-dev`).

This works with WSL, so there is no plan for a Windows setup.
