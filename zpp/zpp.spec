Name:           zpp
Version:        1.0.4
Release:        1
Summary:        The Z Pre-Processor
License:        MIT
URL:            https://github.com/jbigot/zpp
Source0:        https://github.com/jbigot/zpp/archive/%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
Zpp transforms bash in a pre-processor for F90 source files. It offers a set of
functions specifically tailored to build clean Fortran90 interfaces by
generating code for all types, kinds, and array ranks supported by a given
compiler.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%files
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{name}-%{version}-*.egg-info
%{python3_sitelib}/%{name}/
%{_bindir}/%{name}
%{_bindir}/bpp
%{_datadir}/%{name}
%{_datadir}/bpp

%changelog
* Thu Mar 26 2020 - Julien Bigot julien.bigot@cea.fr
- Initial Release
