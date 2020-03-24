# obs-package repository

This is the repository that holds the files used to generate `.deb` and `.rpm`
packages of PDI and related projects on the Open Build Service
(https://build.opensuse.org/project/show/home:pdi).

## Layout

Each directory maps to an open build service "package".

Each directory contains:
* a `debian` directory whose content will be used as-is to generate the debian
  source packages,
* a `src_url` file that contains the URL where to fetch the debian orig file.
* `.spec` and `.changes` files that will be transfered as-is on the open build
  service instance.

The `src_url` file might reference three variables:
* `${PKGNAME}` will be replaced by the name of the source package as defined in
  `debian/control`
* `${PKGVERS}` contains the version of the latest (topmost) package in
  `debian/changelog`
* `${SRCVERS}` contains the source part of this version (i.e. everything before
  a dash)

## Behaviour

The repository contains two important branches:
* `master`: the branch that holds the files used to generate the packages
* `generated`: a single commit branch continuously modified to store the
  generated tar from master HEAD.

The content of `generated` is automatically updated on each commit by the github
Action "OBS".
In addition the action triggers a rebuild on open build service to use the
updated files.

## Adding a new package

To add a new package, edit the `add_package` script to set your username.
Then, simply execute:
```
./add_package <dirnames...>
```

Where `<dirnames...>` is the list of package directories to add.
