### On ${dist_release}

```
echo "deb [ arch=amd64 ] ${baseurl} ${codename} main" | sudo tee /etc/apt/sources.list.d/pdi.list > /dev/null
sudo wget -O /etc/apt/trusted.gpg.d/pdidev-archive-keyring.gpg ${baseurl}/pdidev-archive-keyring.gpg
sudo chmod a+r /etc/apt/trusted.gpg.d/pdidev-archive-keyring.gpg /etc/apt/sources.list.d/pdi.list
sudo apt update
sudo apt install pdidev-archive-keyring libpdi-dev pdiplugin-all
```
