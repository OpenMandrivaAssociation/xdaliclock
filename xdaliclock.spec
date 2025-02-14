
Summary:	A melting digital clock
Name:		xdaliclock
Version:	2.48
Release:	1
License:	MIT
Group:		Toys
URL:		https://www.jwz.org/xdaliclock/
Source0:	http://www.jwz.org/xdaliclock/%{name}-%{version}.tar.gz
#Patch0:		%{name}-shape-cycle.patch

BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(gtk+-3.0)

%description
The xdaliclock program displays a digital clock, with digits that merge
into the new digits as the time changes.  Xdaliclock can display the time
in 12 or 24 hour modes and can will display the date if you hold your
mouse button down over it.  Xdaliclock has two large fonts built in, but
is capable of animating other fonts.

Install the xdaliclock package if you want a fairly large clock, with
a melting special effect, for your system.

%prep
%setup -q
#patch0 -p1

%build
cd X11
CFLAGS="$RPM_OPT_FLAGS" ./configure --libdir=%{_libdir}	--prefix=%{_prefix} \
				--build=%{_target_platform}
%make

%install
cd X11
install -d -m 0755 %buildroot{%_bindir,%_mandir/man1}
make prefix=%buildroot/%_prefix install

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Xdaliclock
Comment=A melting digital clock
Exec=%{_bindir}/%{name} 
Icon=toys_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Utility;Clock;Amusement;X-MandrivaLinux-MoreApplications-Games-Toys;
EOF

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/applications/xdaliclock.desktop
%{_datadir}/glib-2.0/schemas/gschemas.compiled
%{_datadir}/glib-2.0/schemas/org.jwz.xdaliclock.gschema.xml
%{_datadir}/pixmaps/xdaliclock.png
