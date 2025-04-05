# Downloads cli
wget $( curl https://api.github.com/repos/revanced/revanced-cli/releases | jq -r '.[0].assets[] | select(.name | test("revanced-cli.*\\.jar$")) | .browser_download_url' ) -O cli.jar

# Downloads patches
wget $(cat release.json | jq -r '.assets[] | select(.name | test("patches.*\\.rvp$")) | .browser_download_url') -O patches.rvp
