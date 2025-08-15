# Motile Tracker Installer

This repository is used for packaging [Motile Tracker](https://funkelab.github.io/motile_tracker/) into an executable for Windows, OSX, and
Linux

The current workflow assumes that when a `<VERSION>` tag is pushed to the `funkelab/motile_tracker` repository, it creates a draft release. After the user edits and publishes the release the `release` event triggers the `bundle_app` workflow which packages the application and uploads the artifacts to `funkelab/motile_tracker`.

To create a standalone motile_tracker directly from this repo run:
    `pixi run create-app`
and to create the installer for the current platform run:
    `pixi run create-installer`

To create an installer for Windows:
 * Check that [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/) is available
 * If not [download](https://aka.ms/vs/17/release/vs_BuildTools.exe) and install [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/).
 * Check that InnoSetup is available. If not you can install it either with [scoop](https://scoop.sh/) (`scoop install inno-setup`) or with winget (`winget install "Inno Setup"`)
 * Setup the environment for running the `Visual Studio Build Tools`. The script to set all required environment variables is located typically at `"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat"` so before you setup the app you need to run this bat file. For powershell run `scripts\scripts/set-vs-buildTools-env.ps1 <fullpathto vcvars64>`.

To create an installer on Mac:
 * Check that create-dmg is available
 * If create-dmg is not available, install it using [Homebrew](https://brew.sh/) (`brew install create-dmg`)

To create an installer on Linux (Ubuntu) you will need:
* makeself on Linux (`apt install makeself`)
