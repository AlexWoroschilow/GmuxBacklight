Summary: Apple gmux backlight fix
Name: gmux
Version: 0.1
Release: %(date +"%Y%m%d")
Group: System Environment/Kernel
License: MIT
BuildArch: noarch
Requires(pre): python3


%description
Alle Online Präventionskurse sind von der Prüfstelle für Prävention zertifiziert und erfüllen die Qualitätskriterien. Egal ob Bewegung, gesunde Ernährung, Stressbewältigung oder die Online Rückenschule – bei fitbase finden Sie den passenden Präventionskurs. Alle Online Gesundheitskurse haben eine Dauer von 8 bzw. 12 Wochen, zusätzlich haben Sie eine „Pufferzeit“ von vier Wochen für Krankheit, Urlaub o.ä. Die Präventionskurse sind für jeden zugänglich und so konzipiert, dass Sie direkt starten können. Durch unsere Erinnerungsfunktion verpassen Sie keine Einheit.

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
