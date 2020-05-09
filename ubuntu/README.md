# Ubuntu package repository for PDI and related software

This is the repository that holds the Ubuntu packages of PDI and related projects.

The list of repositories for all distributions is available at: https://github.com/pdidev/repo/

## Install the packages

To actually install the packages, use the following instructions.

### On Ubuntu 18.04 LTS (Bionic Beaver)

```
echo "deb [ arch=amd64 ] https://raw.githubusercontent.com/pdidev/repo/ubuntu bionic main" | sudo tee /etc/apt/sources.list.d/pdi.list
sudo wget -O /etc/apt/trusted.gpg.d/pdidev-archive-keyring.gpg https://raw.githubusercontent.com/pdidev/repo/ubuntu/pdidev-archive-keyring.gpg
sudo apt update
sudo apt install pdidev-archive-keyring libpdi-dev
```
### On Ubuntu 20.10 (Groovy Gorilla)

```
echo "deb [ arch=amd64 ] https://raw.githubusercontent.com/pdidev/repo/ubuntu groovy main" | sudo tee /etc/apt/sources.list.d/pdi.list
sudo wget -O /etc/apt/trusted.gpg.d/pdidev-archive-keyring.gpg https://raw.githubusercontent.com/pdidev/repo/ubuntu/pdidev-archive-keyring.gpg
sudo apt update
sudo apt install pdidev-archive-keyring libpdi-dev
```
### On Ubuntu 16.04 LTS (Xenial Xerus)

```
echo "deb [ arch=amd64 ] https://raw.githubusercontent.com/pdidev/repo/ubuntu xenial main" | sudo tee /etc/apt/sources.list.d/pdi.list
sudo wget -O /etc/apt/trusted.gpg.d/pdidev-archive-keyring.gpg https://raw.githubusercontent.com/pdidev/repo/ubuntu/pdidev-archive-keyring.gpg
sudo apt update
sudo apt install pdidev-archive-keyring libpdi-dev
```
### On Ubuntu 20.04 LTS (Focal Fossa)

```
echo "deb [ arch=amd64 ] https://raw.githubusercontent.com/pdidev/repo/ubuntu focal main" | sudo tee /etc/apt/sources.list.d/pdi.list
sudo wget -O /etc/apt/trusted.gpg.d/pdidev-archive-keyring.gpg https://raw.githubusercontent.com/pdidev/repo/ubuntu/pdidev-archive-keyring.gpg
sudo apt update
sudo apt install pdidev-archive-keyring libpdi-dev
```

