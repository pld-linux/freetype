Summary:	Truetype font rasterizer
Summary(pl):	Rasteryzer fontów Truetype
Name:		freetype
Version:	1.2
Release:	6
Copyright:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.physiol.med.tu-muenchen.de/pub/freetype/%{name}-%{version}.tar.gz
URL:		http://www.physiol.med.tu-muenchen.de/~robert/freetype.html
BuildPrereq:	gettext
BuildPrereq:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The FreeType engine is a free and portable TrueType font rendering engine,
available in ANSI C and Pascal source code.  It has been developed to
provide TT support to a great variety of platforms and environments.

%description -l pl
FreeType jest bibliotek± s³u¿±c± do rasteryzacji fontów TrueType.
Kody ¼ród³owe napisane
s± w ANSI C orza PASCAL'u. 

%package devel
Summary:	Header files and development documentation
Summary(pl):	Pliki nag³ówkowe biblioteki freetype i dokumentacja
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package includes the header files documentations and libraries
necessary to develop applications that use freetype.

%description -l pl devel 
Pakiet ten zawiera pliki nag³ówkowe oraz biblioteki niezbêdne przy
kompilowaniu program wykorzystuj±cych bibliotekê freetype.

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
Summary(pl):	Programy u¿ytkowe freetype
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
Przyk³adowe aplikacje wykorzystuj±ce freetype

%prep
%setup -q

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=%{_prefix} \
        --enable-static \
        --with-locale-dir=%{_datadir}/locale \
        --with-gnu-ld
make

%install
rm -rf $RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT/usr \
	localedir=$RPM_BUILD_ROOT%{_datadir}/locale \
	gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale

strip $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9nf howto/unix.txt README announce docs/{*.txt,*.doc,FAQ,TODO,credits}

%find_lang freetype

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f freetype.lang
%attr(755,root,root) %{_libdir}/lib*so.*.*

%files devel
%defattr(644,root,root,755)
%doc howto/unix* docs/*txt* *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%attr(755,root,root) %{_bindir}/*

%changelog
* Sat May 29 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.-6]
- based on cpec from RH contrib (Arne Coucheron <arneco@online.no>),
- spec rewrited by PLD team,
- pl translation by Wojtek ¦lusarczyk <wojtek@shadow.eu.org>.
