#
# Conditional build:
# _without_bytecode	- without TT bytecode interpreter
#			(patents pending in USA, Japan...)
#
Summary:	TrueType font rasterizer
Summary(es.UTF-8):   Biblioteca de render 3D de fuentes TrueType
Summary(pl.UTF-8):   Rasteryzer fontów TrueType
Summary(pt_BR.UTF-8):   Biblioteca de renderização de fontes TrueType
Summary(ru.UTF-8):   Растеризатор шрифтов TrueType
Summary(uk.UTF-8):   Растеризатор шрифтів TrueType
Name:		freetype
Version:	2.1.3rc2
Release:	2
License:	GPL or FTL
Group:		Libraries
Source0:	ftp://ftp.freetype.org/freetype/freetype2/%{name}-%{version}.tar.bz2

Source2:	ftp://ftp.freetype.org/freetype/freetype2/ft2demos-%{version}.tar.bz2
Patch0:		%{name}2-owen.patch
Patch1:		%{name}2-bytecode.patch
Patch2:		%{name}2-slight.patch
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

%description -l es.UTF-8
FreeType es una máquina libre y portátil para en render de fuentes
TrueType. Fue desarrollada para ofrecer soporte TrueType a una gran
variedad de plataformas y ambientes. Observa que FreeType es una
biblioteca y no una aplicación, a pesar de que algunos utilitarios se
incluyan en este paquete.

%description -l pl.UTF-8
FreeType jest biblioteką służącą do rasteryzacji fontów TrueType. Jest
to jedynie biblioteka, a nie serwer fontów, chociaż została ona
zaprojektowana do używania także w takich serwerach. Nie jest to też
kompletna biblioteka do rasteryzacji tekstu. Jej celem jest tylko
odczytywanie i zarządzanie plikami z fontami oraz wczytywanie i
wykonywanie hintingu i rasteryzacji poszczególnych glifów. Może być
także uważana za "sterownik TrueType" dla bibliotek wyższego poziomu,
jednak użycie samej biblioteki FreeType do rasteryzacji jest bardzo
proste, co można zobaczyć w programach demonstracyjnych.

%description -l pt_BR.UTF-8
FreeType é uma máquina livre e portável para renderização de fontes
TrueType. Ela foi desenvolvida para fornecer suporte TrueType a uma
grande variedade de plataformas e ambientes. Note que FreeType é uma
biblioteca e não uma aplicação, apesar que alguns utilitários são
incluídos neste pacote.

%description -l ru.UTF-8
Библиотека FreeType - это свободная переносимая библиотека для
рендеринга (растеризации) шрифтов TrueType, доступная в исходных
текстах на ANSI C и Pascal. Она была разработана для поддержки TT на
разнообразных платформах.

%description -l uk.UTF-8
Бібліотека FreeType - це вільна переносима бібліотека для рендерингу
(растеризації) шрифтів TrueType, що розповсюджується у вихідних
текстах на C та Pascal. Вона була розроблена для підтримки TT на
різних платформах.

%package devel
Summary:	Header files and development documentation
Summary(es.UTF-8):   Archivos de inclusión e bibliotecas estáticas para desarrollo con FreeType.
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki freetype i dokumentacja
Summary(pt_BR.UTF-8):   Arquivos de inclusão e bibliotecas estáticas para desenvolvimento com FreeType.
Summary(ru.UTF-8):   Библиотеки разработчика для freetype
Summary(uk.UTF-8):   Бібліотеки програміста для freetype
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	freetype2-devel

%description devel
This package includes the header files and documentation necessary to
develop applications that use FreeType.

%description devel -l es.UTF-8
Este paquete es necesario, si pretendes desarrollar/compilar
aplicaciones con la biblioteca FreeType. Si, simplemente, deseas
ejecutar aplicaciones existentes, no lo necesitas.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe oraz dokumentację potrzebne przy
tworzeniu programów wykorzystujących bibliotekę FreeType.

%description devel -l pt_BR.UTF-8
Este pacote é necessário se você pretende desenvolver/compilar
aplicações com a biblioteca FreeType. Se você simplesmente deseja
rodar aplicações existentes, você não precisa deste pacote.

%description devel -l ru.UTF-8
Этот пакет содержит хедеры и библиотеки, необходимые для разработки
программ, использующих freetype.

%description devel -l uk.UTF-8
Цей пакет містить хедери та бібліотеки, необхідні для розробки
програм, що використовують freetype.

%package static
Summary:	FreeType static libraries
Summary(es.UTF-8):   Static libraries for freetype development
Summary(pl.UTF-8):   Biblioteki statyczne FreeType
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para desenvolvimento com freetype
Summary(ru.UTF-8):   Статические библиотеки freetype
Summary(uk.UTF-8):   Статичні бібліотеки freetype
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	freetype2-static

%description static
Static FreeType libraries.

%description static -l es.UTF-8
Static libraries for freetype development.

%description static -l pl.UTF-8
Biblioteki statyczne FreeType.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com freetype.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки, необходимые для написания
программ, использующих freetype.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки, необхідні для написання
програм, що використовують freetype.

%package demos
Summary:	FreeType demo programs
Summary(pl.UTF-8):   Programy demonstracyjne FreeType
Group:		X11/Applications
Requires:	%{name} = %{version}

%description demos
Demonstration programs for FreeType library.

%description demos -l pl.UTF-8
Programy demonstracyjne do biblioteki FreeType.

%prep
%setup -q -a2

%{!?_without_bytecode:%patch1 -p1}
%patch2 -p0
%patch0 -p1

%build
CFLAGS="%{rpmcflags}" %{__make} setup CFG="--prefix=%{_prefix}"

%{__make}

%{__make} TOP_DIR="`pwd`" -C ft2demos-*

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	datadir=%{_datadir}

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
#The docs have been moved to the www module, which is very big, decided not to include
#in the package, since it also contained much unwanted and unneeded stuff
#%doc docs/*.html docs/{design,freetype2,glyphs,reference,tutorial}
%attr(755,root,root) %{_bindir}/freetype-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/freetype2
%{_includedir}/*.h
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files demos
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ft*
%attr(755,root,root) %{_xbindir}/ft*
