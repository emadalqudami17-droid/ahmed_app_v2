[app]

# (String) Title of your application
title = Ahmed App

# (String) Package name
package.name = ahmedapp

# (String) Package domain (needed for android/ios packaging)
package.domain = org.ahmed

# (directory) Source code where the main.py lives
source.dir = .

# (list) Source files to include (including png images and wav audio)
source.include_exts = py,png,jpg,kv,atlas,wav

# (list) List of inclusions matching patterns
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (optional)
#source.exclude_exts = spec

# (list) List of directory to exclude (optional)
#source.exclude_dirs = tests, bin, venv

# (String) Application versioning
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
# Sets custom source for any requirement with recipes
# requirements.source.kivy = ../kivy

# (list) Garden requirements
#garden_requirements =

# (String) Presumed orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API required.
android.minapi = 21

# (str) NDK version to use
android.ndk = 25b

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

# (list) List of architectures to build for
android.archs = arm64-v8a

# (bool) If True, then skip building the NDK
#android.skip_update = False

# (bool) If True, the post-build sequence will be executed
#android.post_build = False

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = ignore, 1 = warn)
warn_on_root = 1
