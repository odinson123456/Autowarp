# Downloads cli
wget $( curl https://api.github.com/repos/revanced/revanced-cli/releases | jq -r '.[0].assets[] | select(.name | test("revanced-cli.*\\.jar$")) | .browser_download_url' ) -O cli.jar
