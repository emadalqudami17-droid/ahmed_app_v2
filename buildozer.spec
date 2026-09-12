[app]

# (str) Title of your application
title = Ahmed's World

# (str) Package name
package.name = ahmedworld

# (str) Package domain (needed for android/ios packaging)
package.domain = org.ahmedapp

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,wav,mp3

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, venv, .buildozer, .git

# (str) Application versioning
version = 2.0

# (list) Application requirements
requirements = python3,kivy==2.3.0,plyer

# (str) Icon of the application
icon.filename = %(source.dir)s/app_icon.png

# (str) Supported orientation
orientation = portrait

#
# Android specific
#

# (bool) Fullscreen
fullscreen = 1

# (list) Permissions
android.permissions = VIBRATE, INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API supported
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) If True, then accept all SDK licenses
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a

# (str) Presplash image
presplash.filename = %(source.dir)s/app_icon.png

# (bool) Enable AndroidX support
android.enable_androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
