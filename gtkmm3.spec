#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries

%define		atkmm_ver	2.24.2
%define		glibmm_ver	2.50.0
%define		gtk3_ver	3.22.0
%define		pangomm_ver	2.38.2
Summary:	A C++ interface for the GTK+ (a GUI library for X)
Summary(pl.UTF-8):	Wrapper C++ dla GTK+
Name:		gtkmm3
Version:	3.22.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkmm/3.22/gtkmm-%{version}.tar.xz
# Source0-md5:	9bdd3bfefaa4d3b68ea57456a75c4a12
URL:		http://www.gtkmm.org/
BuildRequires:	atkmm-devel >= %{atkmm_ver}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairomm-devel >= 1.12.0
BuildRequires:	gdk-pixbuf2-devel >= 2.36.0
BuildRequires:	glibmm-devel >= %{glibmm_ver}
BuildRequires:	gtk+3-devel >= %{gtk3_ver}
BuildRequires:	libepoxy-devel >= 1.2
BuildRequires:	libsigc++-devel
BuildRequires:	libstdc++-devel >= 6:4.6
BuildRequires:	libtool >= 2:2.0
BuildRequires:	mm-common >= 0.9.10
BuildRequires:	pangomm-devel >= %{pangomm_ver}
BuildRequires:	perl-base >= 1:5.6.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	atkmm >= %{atkmm_ver}
Requires:	cairomm >= 1.12.0
Requires:	gdk-pixbuf2 >= 2.36.0
Requires:	glibmm >= %{glibmm_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	pangomm >= %{pangomm_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a C++ interface for GTK+ (the Gimp ToolKit) GUI
library. The interface provides a convenient interface for C++
programmers to create GUIs with GTK+'s flexible object-oriented
framework. Features include type safe callbacks, widgets that are
extensible using inheritance and over 110 classes that can be freely
combined to quickly create complex user interfaces.

%description -l pl.UTF-8
gtkmm jest wrapperem C++ dla Gimp ToolKit (GTK). GTK+ jest biblioteką
służącą do tworzenia graficznych interfejsów. W pakiecie znajduje się
także biblioteka gdkmm - wrapper C++ dla GDK (General Drawing Kit).

%package devel
Summary:	gtkmm and gdkmm header files
Summary(pl.UTF-8):	Pliki nagłówkowe gtkmm i gdkmm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	atkmm-devel >= %{atkmm_ver}
Requires:	cairomm-devel >= 1.12.0
Requires:	gdk-pixbuf2-devel >= 2.36.0
Requires:	glibmm-devel >= %{glibmm_ver}
Requires:	gtk+3-devel >= %{gtk3_ver}
Requires:	libstdc++-devel >= 6:4.6
Requires:	pangomm-devel >= %{pangomm_ver}

%description devel
Header files for gtkmm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtkmm.

%package static
Summary:	gtkmm and gdkmm static libraries
Summary(pl.UTF-8):	Biblioteki statyczne gtkmm i gdkmm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gtkmm and gdkmm static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne gtkmm i gdkmm.

%package apidocs
Summary:	Reference documentation for gtkmm and gdkmm
Summary(pl.UTF-8):	Szczegółowa dokumentacja gtkmm i gdkmm
Group:		Documentation
Requires:	devhelp
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Reference documentation for gtkmm and gdkmm.

%description apidocs -l pl.UTF-8
Szczegółowa dokumentacja gtkmm i gdkmm.

%prep
%setup -q -n gtkmm-%{version}

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS PORTING README
%attr(755,root,root) %{_libdir}/libgdkmm-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdkmm-3.0.so.1
%attr(755,root,root) %{_libdir}/libgtkmm-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkmm-3.0.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdkmm-3.0.so
%attr(755,root,root) %{_libdir}/libgtkmm-3.0.so
%{_libdir}/gdkmm-3.0
%{_libdir}/gtkmm-3.0
%{_includedir}/gdkmm-3.0
%{_includedir}/gtkmm-3.0
%{_pkgconfigdir}/gdkmm-3.0.pc
%{_pkgconfigdir}/gtkmm-3.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgdkmm-3.0.a
%{_libdir}/libgtkmm-3.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/gtkmm-3.0
%{_datadir}/devhelp/books/gtkmm-3.0
