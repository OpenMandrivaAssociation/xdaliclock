%define	name	xdaliclock
%define	version	2.24

Summary:	A melting digital clock
Name:		%{name}
Version:	%{version}
Release:	%mkrel 3
Group:		Toys
URL:		http://www.jwz.org/xdaliclock/

BuildRequires:	libx11-devel libxext-devel libxt-devel
License:	MIT

Source0:	http://www.jwz.org/xdaliclock/%{name}-%{version}.tar.bz2
Patch0:		%{name}-shape-cycle.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch0 -p1

%build
cd X11
CFLAGS="$RPM_OPT_FLAGS" ./configure	--prefix=%{_prefix} \
				--build=%{_target_platform}
%make

%install
rm -rf $RPM_BUILD_ROOT

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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/mandriva-%{name}.desktop
