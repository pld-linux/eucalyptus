Summary:	The Eucalyptus Email Application
Name:		eucalyptus
Version:	0.1.6
Release:	1
License:	GPL
Group:		X11/GNOME/Applications
Group(pl):	X11/GNOME/Aplikacje
Vendor:		Paul Schifferer <gandalf@isengard-dev.org>
Source0:	http://www.isengard-dev.org/download/linux/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.isengard-dev.org/
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	gnome-libs-devel >= 1.0.50
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var

%description
An advanced multi-threaded MIME-aware email application.

%description -l pl
Zaawansowany program pocztowy obs³uguj±cy w±tki i typy MIME.

%prep
%setup -q
%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/eucalyptus
%{_datadir}/pixmaps/eucalyptus-logo.png
%{_applnkdir}/Internet/eucalyptus.desktop
