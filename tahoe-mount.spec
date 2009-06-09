Name:      tahoe-mount
Version:   0.1.0
Release:   1
Summary:   tahoe-mount scripts
Group:     System/Server
URL:       http://stockrtweb.homelinux.com
Vendor:    Allmydata.org
Packager:  Rogerio Carvalho Schneider <stockrt@gmail.com>
License:   GPL
BuildArch: noarch
Source:    %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:  fuse
Requires:  dkms-fuse
Requires:  tahoe-svc

%description
tahoe-mount scripts

%prep
%setup -q -n %{name}

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -m 0755 -d %{buildroot}%{_bindir}
%{__install} -m 0755 -d %{buildroot}%{_sysconfdir}/logrotate.d

%{__install} -m 0755 bin/* %{buildroot}%{_bindir}/
%{__install} -m 0755 logrotate.d/* %{buildroot}%{_sysconfdir}/logrotate.d/

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_sysconfdir}/logrotate.d/*

%clean
%{__rm} -rf %{buildroot}

%changelog
* Mon Jun  8 2009 - Rogerio Carvalho Schneider <stockrt@gmail.com> - 0.1.0-1
- Initial packing
