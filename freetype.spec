Summary:	Truetype font rasterizer
Summary(pl):	Rasteryzer font�w Truetype
Name:		freetype
Version:	1.2
Release:	2
Group:		Libraries
Group(pl):	Biblioteki
Copyright:	LGPL
Source:		ftp://ftp.physiol.med.tu-muenchen.de/pub/freetype/freetype-%{version}.tar.gz
URL:		http://www.physiol.med.tu-muenchen.de/~robert/freetype.html
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The FreeType engine is a free and portable TrueType font rendering engine,
available in ANSI C and Pascal source code.  It has been developed to
provide TT support to a great variety of platforms and environments.

%description -l pl
FreeType jest bibliotek� s�u��c� do rasteryzacji font�w TrueType.
Kody �r�d�owe napisane
s� w ANSI C orza PASCAL'u. 

%package devel
Summary:	Header files and development documentation
Summary(pl):	Pliki nag��wkowe biblioteki freetype i dokumentacja
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	freetype = %{version}

%description devel
This package includes the header files documentations and libraries
necessary to develop applications that use freetype.

%description -l pl devel 
Pakiet ten zawiera pliki nag��wkowe oraz biblioteki niezb�dne przy
kompilowaniu program wykorzystuj�cych bibliotek� freetype.

%package static
Summary:	Freetype static libraries
Summary(pl):	Biblioteki statyczne freetype
Group:		Development/Libraries
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
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description progs
Freetype library utilites:
- ftimer   - a simple performance timer for the engine,
- fzoom    - very simple glyph viewer,
- ftlint   - program will hint each glyph of a font file, at a given point
             size,
- ftwiew   - display all glyphs in a given font, applying hinting to each one,
- fdump    - a simple TrueType font or collection dumper,
- ftstring - a simple program to show off string text generation.
- ftstrpn  - convert a rendered text string into the PGM or PBM format,
- fterror  - small test program. Tests the gettext()
             functionality for internationalized messages.

%description -l pl progs
Przyk�adowe aplikacje wykorzystuj�ce freetype

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure --prefix=/usr \
            --enable-static \
            --with-locale-dir=/usr/share/locale \
            --with-gnu-ld
make

%install
rm -rf $RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT/usr \
	localedir=$RPM_BUILD_ROOT/usr/share/locale \
	gnulocaledir=$RPM_BUILD_ROOT/usr/share/locale

strip $RPM_BUILD_ROOT/usr/lib/lib*so.*.*

bzip2 -9 HOWTO.txt README announce license.txt docs/{*.txt,*lsm,*doc,FAQ,TODO}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/lib*so.*.*

%lang(cs) /usr/share/locale/cs/LC_MESSAGES/freetype.mo
%lang(de) /usr/share/locale/de/LC_MESSAGES/freetype.mo
%lang(es) /usr/share/locale/es/LC_MESSAGES/freetype.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/freetype.mo
%lang(nl) /usr/share/locale/nl/LC_MESSAGES/freetype.mo

%files devel
%defattr(644,root,root)
%doc docs/* *.bz2
%attr(755,root,root) /usr/lib/lib*.so
/usr/include/*

%files static
%attr(644,root,root) /usr/lib/lib*.a

%files progs
%attr(755,root,root) /usr/bin/*

%changelog
* Sun Jan 24 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-2]
- fixed pl transtion,
- added Group(pl),
- all %doc moved to devel,
- added bzipping2 %doc,
- fixed permission on /usr/lib/lib*.so in devel (must be 755).

* Mon Jul 20 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.1-2]
- added static subapackage
- added pl translation.

* Fri Jun 05 1998 Arne Coucheron <arneco@online.no>
- updated to 1.1pre1-2
- rpm 2.5 is doing weird things with the %doc, moved it last in filelist
  to make it behave better

* Mon May 25 1998 Arne Coucheron <arneco@online.no>
- updated to 1.1pre1-1
- removed libttf.so.1 symlink
- added --with-locale-dir and --with-gnu-ld to configure
- changed HOWTO in %doc to HOWTO.txt
- lib*.so* files wasn't chmod 755, fixed
- removed initial making of the $RPM_BUILD_ROOT/usr directory
  layout in %install, it isn't needed

* Thu May 14 1998 Arne Coucheron <arneco@online.no>
- updated to current devel release so that ImageMagick 4.0.6 can be compiled
- removed installing of tterror.h/ttcommon.h, don't exist in devel source
- added --enable-static to configure, required now to build static libs
- added additional NLS languages
- made symlink from libttf.so.1 to libttf.so.2.0.0 for apps needing it

* Wed May  6 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- added instaling tterror.h header file,
- %%{version} macro instead %%{PACKAGE_VERSION},
- added using %%{name} macro in Buildroot and in Requires in devel,
- added -q %setup parameter.

* Mon Apr 27 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- replaced usind %{version} macro by predefined %%{PACKAGE_VERSION},
- added "Requires: freetype = %{PACKAGE_VERSION}" for devel subpackage,
- added using %defattr in %files (requires rpm >= 2.4.99),
- added %lang macros for files /usr/share/locale/*/LC_MESSAGES/freetype.mo
  files,
- added stripping /usr/lib/lib*so.*.*,
- programs from /usr/bin/ moved to separated progs subpackage.

* Wed Feb 18 1998 Arne Coucheron <arneco@online.no>
- First release, 1.0-1
