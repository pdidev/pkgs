# Fedora package repository for PDI and related software

This is the repository that holds the Fedora packages of PDI and related projects.

The list of repositories for all distributions is available at: https://github.com/pdidev/repo/

## Install the packages

To actually install the packages, use the following instructions.

### On Fedora Rawhide

```
sudo wget -O /etc/yum.repos.d/pdidev.repo https://raw.githubusercontent.com/pdidev/repo/fedora/33/pdidev.repo
sudo dnf install pdi-devel
```
### On Fedora 32

```
sudo wget -O /etc/yum.repos.d/pdidev.repo https://raw.githubusercontent.com/pdidev/repo/fedora/32/pdidev.repo
sudo dnf install pdi-devel
```
### On Fedora 31

```
sudo wget -O /etc/yum.repos.d/pdidev.repo https://raw.githubusercontent.com/pdidev/repo/fedora/31/pdidev.repo
sudo dnf install pdi-devel
```
### On Fedora 30

```
sudo wget -O /etc/yum.repos.d/pdidev.repo https://raw.githubusercontent.com/pdidev/repo/fedora/30/pdidev.repo
sudo dnf install pdi-devel
```

