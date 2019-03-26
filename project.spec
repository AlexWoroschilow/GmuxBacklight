Summary: Apple gmux backlight fix
Name: gmux
Version: 0.1
Release: %(date +"%Y%m%d")
Group: System Environment/Kernel
License: MIT
BuildArch: noarch
Requires(pre): python3


%description
gmux fix

%prep
%setup -q

%install
install -d $RPM_BUILD_ROOT/etc/udev/rules.d
install -d $RPM_BUILD_ROOT/etc/gmux

cp -R 80-gmux.rules $RPM_BUILD_ROOT/etc/udev/rules.d
cp -R gmux_* $RPM_BUILD_ROOT/etc/gmux

%post
udevadm control --reload

%files 
%defattr(644,root,root,755)
%dir /etc/udev/rules.d
%dir /etc/gmux

%attr(755,root,root) /etc/gmux/*
/etc/udev/rules.d/*
