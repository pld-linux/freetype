Summary:	Truetype font rasterizer
Summary(pl):	Rasteryzer fontów Truetype
Name:		freetype
Version:	2.0.2
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://freetype.sourceforge.net/pub/freetype/%{name}/%{name}2-%{version}-test.tar.bz2
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.freetype.org/
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

%description static
Static freetype libraries.

%description -l pl static 
Biblioteki statyczne freetype.

%prep
%setup -q -n freetype-%{version}-test
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" %{__make} 
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	prefix"=%{_prefix}"

chmod u+rw $RPM_BUILD_ROOT%{_bindir}/freetype-config
cat $RPM_BUILD_ROOT%{_bindir}/freetype-config \
	| sed 's/prefix=\/usr\/local/prefix=\/usr/g' \
	> $RPM_BUILD_ROOT%{_bindir}/freetype-config.new
mv $RPM_BUILD_ROOT%{_bindir}/freetype-config.new $RPM_BUILD_ROOT%{_bindir}/freetype-config

gzip -9nf LICENSE.TXT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*.html
%attr(755,root,root) %{_libdir}/lib*so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/freetype2

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
