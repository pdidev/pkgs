This is the repository that holds the files used to generate `.deb` and `.rpm`
packages of PDI and related projects on the Open Build Service
(https://build.opensuse.org/project/show/home:pdi).

## Layout

Each directory maps to an open build service "package".
Each package contains:
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

To add a new package, one must:
* add a package manually on the open build service side,
* add a `_service` file in this package whose content match that of the one
  provided at the root of the repository, but where `%(package)` is replaced by
  the package name,
* generate a token for the repository
  - either with the `osc` command line tool:
```
osc token --create home:pdi ${pkgname}
```
  - or with `curl`:
```
curl -X POST --anyauth -u ${username} "https://api.opensuse.org/person/jbigot/token?project=home:pdi&package=${pkgname}"
```
* add this token as a "secret" on github
  https://github.com/pdidev/obs-packages/settings/secrets/new
* add a trigger line to `.github/workflows/main.yml`
  - an env line:
```
OBS_<ALLCAPSPACKAGENAME>_RUNSERVICE_TOKEN: ${{ secrets.<YourSecretName> }}
```
  - the actual trigger:
```
curl -s 'https://build.opensuse.org/trigger/runservice' -X POST -H "Authorization: Token ${OBS_<ALLCAPSPACKAGENAME>_RUNSERVICE_TOKEN}"
```
