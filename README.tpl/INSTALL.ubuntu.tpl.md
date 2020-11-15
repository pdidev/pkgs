### On ${dist_release}

```
echo "deb [ arch=amd64 ] ${baseurl}/ ${codename} main" | sudo tee /etc/apt/sources.list.d/pdi.list
sudo wget -O /etc/apt/trusted.gpg.d/pdidev-archive-keyring.gpg ${baseurl}/pdidev-archive-keyring.gpg
sudo apt update
sudo apt install pdidev-archive-keyring libpdi-dev
```
