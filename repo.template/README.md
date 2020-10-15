# deb and RPM packages for PDI and related software 

This is the repository that holds the `.deb` and `.rpm` packages of PDI and
related projects.

The packages are built from the [master](../../tree/master) branch of this
repository using the `pkgbuild` script https://github.com/jbigot/pkg_builder

# Install the packages

## Ubuntu

### On Ubuntu 20.04 LTS (Focal Fossa)

```
echo "deb [ arch=amd64 ] https://raw.githubusercontent.com/pdidev/pkgs/repo/ubuntu/ focal main" | sudo tee /etc/apt/sources.list.d/pdi.list
sudo wget -O /etc/apt/trusted.gpg.d/pdidev-archive-keyring.gpg https://raw.githubusercontent.com/pdidev/pkgs/repo/pdidev-archive-keyring.gpg
sudo apt update
sudo apt install pdidev-archive-keyring libpdi-dev
```

### On Ubuntu 19.10 (Eoan Ermine)

```
echo "deb [ arch=amd64 ] https://raw.githubusercontent.com/pdidev/pkgs/repo/ubuntu/ eoan main" | sudo tee /etc/apt/sources.list.d/pdi.list
sudo wget -O /etc/apt/trusted.gpg.d/pdidev-archive-keyring.gpg https://raw.githubusercontent.com/pdidev/pkgs/repo/pdidev-archive-keyring.gpg
sudo apt update
sudo apt install pdidev-archive-keyring libpdi-dev
```

### On Ubuntu 16.04 LTS (Xenial Xerus)

```
echo "deb [ arch=amd64 ] https://raw.githubusercontent.com/pdidev/pkgs/repo/ubuntu/ xenial main" | sudo tee /etc/apt/sources.list.d/pdi.list
sudo wget -O /etc/apt/trusted.gpg.d/pdidev-archive-keyring.gpg https://raw.githubusercontent.com/pdidev/pkgs/repo/pdidev-archive-keyring.gpg
sudo apt update
sudo apt install pdidev-archive-keyring libpdi-dev
```

## Debian GNU/Linux

### On Debian GNU/Linux 10 (Buster) aka. stable

```
echo "deb [ arch=amd64 ] https://raw.githubusercontent.com/pdidev/pkgs/repo/debian/ buster main" | sudo tee /etc/apt/sources.list.d/pdi.list
sudo wget -O /etc/apt/trusted.gpg.d/pdidev-archive-keyring.gpg https://raw.githubusercontent.com/pdidev/pkgs/repo/pdidev-archive-keyring.gpg
sudo apt update
sudo apt install pdidev-archive-keyring libpdi-dev
```

### On Debian GNU/Linux Sid aka. unstable

```
echo "deb [ arch=amd64 ] https://raw.githubusercontent.com/pdidev/pkgs/repo/debian/ unstable main" | sudo tee /etc/apt/sources.list.d/pdi.list
sudo wget -O /etc/apt/trusted.gpg.d/pdidev-archive-keyring.gpg https://raw.githubusercontent.com/pdidev/pkgs/repo/pdidev-archive-keyring.gpg
sudo apt update
sudo apt install pdidev-archive-keyring libpdi-dev
```

### On Debian GNU/Linux 11 (Bullseye) aka. testing

```
echo "deb [ arch=amd64 ] https://raw.githubusercontent.com/pdidev/pkgs/repo/debian/ testing main" | sudo tee /etc/apt/sources.list.d/pdi.list
sudo wget -O /etc/apt/trusted.gpg.d/pdidev-archive-keyring.gpg https://raw.githubusercontent.com/pdidev/pkgs/repo/pdidev-archive-keyring.gpg
sudo apt update
sudo apt install pdidev-archive-keyring libpdi-dev
```

### On Debian GNU/Linux 9 (Stretch) aka. oldstable

```
echo "deb [ arch=amd64 ] https://raw.githubusercontent.com/pdidev/pkgs/repo/debian/ stretch main" | sudo tee /etc/apt/sources.list.d/pdi.list
sudo wget -O /etc/apt/trusted.gpg.d/pdidev-archive-keyring.gpg https://raw.githubusercontent.com/pdidev/pkgs/repo/pdidev-archive-keyring.gpg
sudo apt update
sudo apt install pdidev-archive-keyring libpdi-dev
```

## Fedora

### On Fedora 31

```
sudo wget -O /etc/yum.repos.d/pdidev.repo https://raw.githubusercontent.com/pdidev/pkgs/repo/fedora/31/pdidev.repo
sudo dnf install pdi-devel
```

### On Fedora 33 aka. Rawhide

```
sudo wget -O /etc/yum.repos.d/pdidev.repo https://raw.githubusercontent.com/pdidev/pkgs/repo/fedora/33/pdidev.repo
sudo dnf install pdi-devel
```

### On Fedora 32 aka. branched

```
sudo wget -O /etc/yum.repos.d/pdidev.repo https://raw.githubusercontent.com/pdidev/pkgs/repo/fedora/32/pdidev.repo
sudo dnf install pdi-devel
```

### On Fedora 30

```
sudo wget -O /etc/yum.repos.d/pdidev.repo https://raw.githubusercontent.com/pdidev/pkgs/repo/fedora/30/pdidev.repo
sudo dnf install pdi-devel
```
