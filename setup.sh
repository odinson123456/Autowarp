# Downloads cli
wget -q $( curl https://api.github.com/repos/revanced/revanced-cli/releases | jq -r '.[0].assets[] | select(.name | test("revanced-cli.*\\.jar$")) | .browser_download_url' ) -O cli.jar

# Downloads patches
wget -q $(cat release.json | jq -r '.assets[] | select(.name | test("patches.*\\.rvp$")) | .browser_download_url') -O patches.rvp

# writes commit body to data.txt
jq -r '.body' release.json > data.txt