# Motile Tracker Installer

This repository is used for packaging [Motile Tracker](https://funkelab.github.io/motile_tracker/) into an executable for Windows, OSX, and
Linux

The current workflow assumes that when a `v<VERSION>` tag is pushed to the `funkelab/motile_tracker` repository, it creates a draft release. After the user edits and publishes the release the `release` event triggers the `bundle_app` workflow which packages the application and uploads the artifacts to `funkelab/motile_tracker`