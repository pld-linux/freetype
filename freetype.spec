#
# Conditional build:
# _without_bytecode	- without TT bytecode interpreter
#			(patents pending in USA, Japan...)
#
Summary:	TrueType font rasterizer
Summary(pl):	Rasteryzer fontów TrueType
Name:		freetype
Version:	2.0.9
Release:	1
License:	GPL or FTL
Group:		Libraries
Source0:	ftp://ftp.freetype.org/freetype/freetype2/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.freetype.org/freetype/freetype2/ftdocs-%{version}.tar.bz2
Source2:	ftp://ftp.freetype.org/freetype/freetype2/ft2demos-%{version}.tar.bz2
Patch0:		%{name}2-DESTDIR.patch
Patch1:		%{name}2-bytecode.patch
URL:		http://www.freetype.org/
BuildRequires:	SysVinit
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	freetype2

%define		_xbindir	/usr/X11R6/bin

%description
The FreeType engine is a free and portable TrueType font rendering
engine. It has been developed to provide TrueType support to a great
variety of platforms and environments.

Note that FreeType is a *library*. It is not a font server for your
favorite platform, even though it was designed to be used in many of
them. Note also that it is *not* a complete text-rendering library.
Its purpose is simply to open and manage font files, as well as load,
hint and render individual glyphs efficiently. You can also see it as
a "TrueType driver" for a higher-level library, though rendering text
with it is extremely easy, as demo-ed by the test programs.

%description -l pl
FreeType jest bibliotek± s³u¿±c± do rasteryzacji fontów TrueType. Jest
to jedynie biblioteka, a nie serwer fontów, chocia¿ zosta³a ona
zaprojektowana do u¿ywania tak¿e w takich serwerach. Nie jest to te¿
kompletna biblioteka do rasteryzacji tekstu. Jej celem jest tylko
odczytywanie i zarz±dzanie plikami z fontami oraz wczytywanie i
wykonywanie hintingu i rasteryzacji poszczególnych glifów. Mo¿e byæ
tak¿e uwa¿ana za "sterownik TrueType" dla bibliotek wy¿szego poziomu,
jednak u¿ycie samej biblioteki FreeType do rasteryzacji jest bardzo
proste, co mo¿na zobaczyæ w programach demonstracyjnych.

%package devel
Summary:	Header files and development documentation
Summary(pl):	Pliki nag³ówkowe biblioteki freetype i dokumentacja
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	freetype2-devel

%description devel
This package includes the header files and documentation necessary
to develop applications that use FreeType.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe oraz dokumentacjê potrzebne przy
tworzeniu programów wykorzystuj±cych bibliotekê FreeType.

%package static
Summary:	FreeType static libraries
Summary(pl):	Biblioteki statyczne FreeType
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	freetype2-static

%description static
Static FreeType libraries.

%description static -l pl
Biblioteki statyczne FreeType.

%package demos
Summary:	FreeType demo programs
Summary(pl):	Programy demonstracyjne FreeType
Group:		X11/Applications
Requires:	%{name} = %{version}

%description demos
Demonstration programs for FreeType library.

%description demos -l pl
Programy demonstracyjne do biblioteki FreeType.

%prep
%setup -q -b1 -a2
%patch0 -p1
%{!?_without_bytecode:%patch1 -p1}

%build
CFLAGS="%{rpmcflags}" %{__make} setup CFG="--prefix=%{_prefix}"

%{__make}

%{__make} TOP="`pwd`" -C ft2demos-*

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

# demos
install -d $RPM_BUILD_ROOT{%{_bindir},%{_xbindir}}
install ft2demos-*/bin/.libs/ft{multi,timer,view} $RPM_BUILD_ROOT%{_xbindir}
install ft2demos-*/bin/.libs/ft{dump,lint,memchk} $RPM_BUILD_ROOT%{_bindir}
install ft2demos-*/bin/.libs/testnames $RPM_BUILD_ROOT%{_bindir}/fttestnames

gzip -9nf docs/{BUGS,CHANGES,FTL.txt,PATENTS,license.txt,TODO,modules.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/*.gz
%attr(755,root,root) %{_libdir}/lib*so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/*.html docs/{design,freetype2,glyphs,reference,tutorial}
%attr(755,root,root) %{_bindir}/freetype-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/freetype2
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files demos
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ft*
%attr(755,root,root) %{_xbindir}/ft*
