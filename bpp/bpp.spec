Name:           bpp
Version:        0.4.0
Release:        0
Summary:        A Bash pre-processor originally intended for Fortran
License:        MIT
URL:            https://github.com/pdidev/bpp
Source0:        https://github.com/pdidev/%{name}/archive/v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%name-root
BuildArch:      noarch
BuildRequires:  python3-devel

%description
BPP, the Bash Pre-Processor.

BPP is useful in order to build clean Fortran90 interfaces.
It allows to generate Fortran code for all types, kinds,
and array ranks supported by the compiler.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%files
%license COPYING
%doc README.md
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/
%{_bindir}/%{name}

%changelog
* Wed Mar 25 2020 - Julien Bigot julien.bigot@cea.fr
- Initial Release
