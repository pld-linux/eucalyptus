Summary:	The Eucalyptus Email Application
Name:		eucalyptus
Version:	0.1.6
Release:	1
License:	GPL
Group:		X11/GNOME/Applications
URL:		http://www.isengard-dev.org/
Vendor:		Paul Schifferer <gandalf@isengard-dev.org>
Source:		http://www.isengard-dev.org/download/linux/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRoot:	/tmp/%{name}-%{version}-root
Requires:	gtk+ >= 1.2.6
Requires:	glib >= 1.2.6
Requires:	gnome-libs >= 1.0.50

%define		prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var
%define		_applnkdir	%{_datadir}/applnk

%description
An advanced multi-threaded MIME-aware email application.

%prep
%setup -q
%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS COPYING ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,COPYING,ChangeLog,NEWS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/eucalyptus
%{_datadir}/pixmaps/eucalyptus-logo.png
%{_applnkdir}/Internet/eucalyptus.desktop
