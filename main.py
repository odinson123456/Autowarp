from glob import glob
import json
from utils import downloadapk, patchapk

pkgs = {
    "youtube": "com.google.android.youtube",
    "youtube music": "com.google.android.apps.youtube.music",
}

patches = {}
with open(glob("selected*json")[0], "r") as f:
    patches = json.load(f)
otp = {}
for name, pkgname in pkgs.items():
    print(f"Downloading {name} APK")
    f, title = downloadapk(pkgname)
    print(f"Downloaded {f} for {title}")
    print(f"Applying patches for {name}")
    otp[pkgname] = {
        "name": name,
        "logs": patchapk(f, pkgname, patches),
        "outfile": f"out/{f}",
    }
    print(f"Patched {f} for {title}")

with open("otp.json", "w") as f:
    json.dump(otp, f, indent=4)
