Summary:	Plugins for UCView video capture and display program
Summary(pl.UTF-8):	Wtyczki do programu do przechwytywania i wyświetlania obrazu UCView
Name:		ucview_plugins
Version:	1.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
#Source0Download: http://unicap-imaging.org/download.htm
Source0:	http://unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	7d4cbb44aa81b654d6bb2f391cb61f05
URL:		http://unicap-imaging.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.8.0
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	libunicap-devel
BuildRequires:	libucil-devel
BuildRequires:	ucview-devel
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for UCView video capture and display program:
- debayer
- histogram
- videoplay

%description -l pl.UTF-8
Wtyczki do programu do przechwytywania i wyświetlania obrazu UCView:
- debayer
- histogram
- videoplay

%prep
%setup -q

%build
# upstream autotools suite is inconsistent
%{__aclocal}
%{__autoconf}
%{__automake}
for d in ucview_*_plugin ; do
	cd $d
	%{__libtoolize}
	%{__aclocal}
	%{__autoconf}
	%{__autoheader}
	%{__automake}
	cd ..
done
# broken pkgconfig check for ucview
CPPFLAGS="%{rpmcppflags} -I/usr/include/ucview"
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/ucview/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/ucvidplay
%attr(755,root,root) %{_libdir}/ucview/plugins/libdebayer_plugin.so
%attr(755,root,root) %{_libdir}/ucview/plugins/libhistogram.so
%attr(755,root,root) %{_libdir}/ucview/plugins/libvideoplay.so
