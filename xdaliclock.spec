%define	name	xdaliclock
%define	version	2.23
%define	release	1mdk
%define	Summary	A clock for the X Window System

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Toys
URL:		http://www.jwz.org/xdaliclock/

BuildRequires:	X11-devel
License:	MIT

Source0:	http://www.jwz.org/xdaliclock/xdaliclock-%{version}.tar.bz2
Patch0:		%{name}-shape-cycle.patch.bz2

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
CFLAGS="$RPM_OPT_FLAGS" ./configure	--prefix=%{_prefix}/X11R6 \
				--build=%{_target_platform}
%make

%install
rm -rf $RPM_BUILD_ROOT

cd X11
install -d -m 0755 %buildroot/%_prefix/X11R6/{bin,man/man1}
make prefix=%buildroot/%_prefix/X11R6 install

install -d $RPM_BUILD_ROOT%{_menudir}
cat <<EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
        needs="X11" \
        section="Amusement/Toys" \
        title="Xdaliclock" \
        longtitle="%{Summary}" \
        command="%{name}" \
        icon="toys_section.png"
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/X11R6/bin/%{name}
%{_prefix}/X11R6/man/man1/%{name}.1*
%{_menudir}/%{name}
