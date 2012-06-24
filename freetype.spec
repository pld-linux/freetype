Summary:	Truetype font rasterizer
Summary(pl):	Rasteryzer font�w Truetype
Name:		freetype
Version:	1.3.1
Release:	8
License:	BSD like
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.physiol.med.tu-muenchen.de/pub/freetype/%{name}-%{version}.tar.gz
Source1:	ttmkfdir.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-autoconf.patch
Patch2:		%{name}-foundrynames.patch
Patch3:		%{name}-nospaces.patch
URL:		http://www.physiol.med.tu-muenchen.de/~robert/freetype.html
BuildRequires:	gettext-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
FreeType jest bibliotek� s�u��c� do rasteryzacji font�w TrueType. Kody
�r�d�owe napisane s� w ANSI C oraz PASCAL'u.

%package devel
Summary:	Header files and development documentation
Summary(pl):	Pliki nag��wkowe biblioteki freetype i dokumentacja
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package includes the header files documentations and libraries
necessary to develop applications that use freetype.

%description -l pl devel 
Pakiet ten zawiera pliki nag��wkowe oraz biblioteki niezb�dne przy
kompilowaniu program�w wykorzystuj�cych bibliotek� freetype.

%package static
Summary:	Freetype static libraries
Summary(pl):	Biblioteki statyczne freetype
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static freetype libraries.

%description -l pl static 
Biblioteki statyczne freetype.

%package progs
Summary:	Freetype library utilities
Summary(pl):	Programy u�ytkowe freetype
Group:		Utilities
Group(pl):	Narz�dzia
Requires:	%{name} = %{version}
Obsoletes:	freetype-utils

%description progs
Freetype library utilites:
- ftimer - a simple performance timer for the engine,
- fzoom - very simple glyph viewer,
- ftlint - program will hint each glyph of a font file, at a given
  point size,
- ftwiew - display all glyphs in a given font, applying hinting to
  each one,
- fdump - a simple TrueType font or collection dumper,
- ftstring - a simple program to show off string text generation.
- ftstrpn - convert a rendered text string into the PGM or PBM format,
- fterror - small test program. Tests the gettext() functionality for
  internationalized messages.

%description -l pl progs
Przyk�adowe aplikacje wykorzystuj�ce freetype.

%prep
%setup -q
mkdir ttmkfdir
tar xz -C ttmkfdir -f %{SOURCE1}
%patch0 -p1
%patch1 -p1

%build
gettextize --copy --force
aclocal
autoconf
%configure \
        --enable-static \
        --with-gnu-ld
%{__make}
%{__make} -C ttmkfdir CC="gcc $RPM_OPT_FLAGS -I../lib"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -s ttmkfdir/ttmkfdir $RPM_BUILD_ROOT%{_bindir}

strip $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9nf howto/unix.txt README announce docs/{*.txt,FAQ,TODO,credits}

%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ttmkfdir
%attr(755,root,root) %{_libdir}/lib*so.*.*

%files devel
%defattr(644,root,root,755)
%doc howto/unix* docs/*txt* *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/f*
