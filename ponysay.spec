#
# spec file for package ponysay
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           ponysay
Version:        3.0.3
Release:        1%{?dist}
Summary:        Cowsay reimplementation for ponies
License:        GPL-3.0-or-later
Url:            https://github.com/erkin/ponysay
Source:         https://github.com/erkin/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  texinfo
Requires:       python3
Requires(post): info
Requires(preun): info
#BuildArch:      noarch

%description
ponysay as an awesome terminal application to display ponies speaking
messages in your terminal.
It has many features; you can use its info manual to explore them.

%prep
%setup -q

%build
# Nothing to build.

%install
python3 setup.py \
  --dest-dir=%{buildroot} \
  --prefix=%{_prefix} \
  --freedom=partial \
  --with-everything \
  --with-pdf=%{_docdir}/%{name}/ \
  install
rm -rf %{buildroot}%{_infodir} %{buildroot}%{_datadir}/licenses/
rm -rf %{buildroot}%{_docdir}/%{name}/*.gz 
%fdupes %{buildroot}/%{_datadir}/%{name}

%post
#%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}
#%install_info --info-dir=%{_infodir} %{_infodir}/%{name}-tool.info%{ext_info}
#%install_info --info-dir=%{_infodir} %{_infodir}/ponythink.info%{ext_info}

%postun
#%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}
#%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}-tool.info%{ext_info}
#%install_info_delete --info-dir=%{_infodir} %{_infodir}/ponythink.info%{ext_info}

%files
%license LICENSE COPYING
%doc CHANGELOG CONTRIBUTING CREDITS README.md
%{_bindir}/pony*
%{_datadir}/%{name}/
#%{_infodir}/*.gz
%{_mandir}/*/
%{_datadir}/bash-completion/
%{_datadir}/zsh/
%{_datadir}/fish/

%changelog
* Fri Apr 24 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 3.0.3-1
- Update to 3.0.3
- Modernize spec for EL10 (remove Group, defattr, use python3)

* Sat Sep  6 2014 sor.alexei@meowr.ru
- Update to 3.0.2
  * New ponies: auntorange, grace
  * Pony symlink added:
  - cookiecrumbles → raritysmom (official name)
  - hondoflanks → raritysdad (official name)
  * Special pony cases:
  - orange was renamed to uncleorange to not conflict with
    auntorange.
- Remove info-direntry.patch: fixed upstream.
* Sat Apr 26 2014 andreas.stieger@gmx.de
- spec cleanup.
- Add source URLs.
* Sun Apr  6 2014 sor.alexei@meowr.ru
- Initial package.
