Summary:	Truetype font rasterizer
Summary(pl):	Rasteryzer fontów Truetype
Name:		freetype
Version:	2.0.4
Release:	1
License:	GPL or FTL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://freetype.sourceforge.net/pub/freetype/%{name}2/%{name}-%{version}.tar.bz2
Source1:	ftp://freetype.sourceforge.net/pub/freetype/%{name}2/ftdocs-%{version}.tar.bz2
Patch0:		%{name}2-DESTDIR.patch
Patch1:		%{name}2-gsf-segv.patch
URL:		http://www.freetype.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	freetype2

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
FreeType jest bibliotek± s³u¿±c± do rasteryzacji fontów TrueType. Kody
¼ród³owe napisane s± w ANSI C oraz PASCAL'u.

%package devel
Summary:	Header files and development documentation
Summary(pl):	Pliki nag³ówkowe biblioteki freetype i dokumentacja
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Obsoletes:	freetype2-devel
Obsoletes:	freetype2-static

%description devel
This package includes the header files documentations and libraries
necessary to develop applications that use freetype.

%description -l pl devel 
Pakiet ten zawiera pliki nag³ówkowe oraz biblioteki niezbêdne przy
kompilowaniu programów wykorzystuj±cych bibliotekê freetype.

%package static
Summary:	Freetype static libraries
Summary(pl):	Biblioteki statyczne freetype
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}
Obsoletes:	freetype2-static

%description static
Static freetype libraries.

%description -l pl static 
Biblioteki statyczne freetype.

%prep
%setup -q -b1
%patch0 -p1
%patch1 -p1

%build
CFLAGS="%{rpmcflags}" %{__make} setup CFG="--prefix=%{_prefix}"

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf docs/{CHANGES,FTL.txt,PATENTS,license.txt,todo,cache.txt}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.gz
%attr(755,root,root) %{_libdir}/lib*so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/*.html docs/{design,freetype2,glyphs,reference,tutorial}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/freetype2
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
