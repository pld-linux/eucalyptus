Summary:	The Eucalyptus Email Application
Summary(pl.UTF-8):	Program pocztowy Eucalyptus
Name:		eucalyptus
Version:	0.1.6
Release:	1
License:	GPL
Group:		X11/Applications
Vendor:		Paul Schifferer <gandalf@isengard-dev.org>
Source0:	http://www.isengard-dev.org/download/linux/%{name}-%{version}.tar.gz
# Source0-md5:	81a5087fa0c8f8f4ea00cac3e17b7914
Source1:	%{name}.desktop
Patch0:		%{name}-GNU_GETTEXT.patch
URL:		http://www.isengard-dev.org/
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	gnome-libs-devel >= 1.0.50
BuildRequires:	gettext-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var

%description
An advanced multi-threaded MIME-aware email application.

%description -l pl.UTF-8
Zaawansowany program pocztowy obsługujący wątki i typy MIME.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/eucalyptus
%{_pixmapsdir}/eucalyptus-logo.png
%{_applnkdir}/Internet/eucalyptus.desktop
