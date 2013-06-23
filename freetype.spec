#
# Conditional build:
%bcond_without	lcd		# without LCD subpixel color filtering (Microsoft patents in USA)
%bcond_without	x11		# don't build examples (X11-based)
%bcond_without	apidocs         # disable api docs

Summary:	TrueType font rasterizer
Summary(es.UTF-8):	Biblioteca de render 3D de fuentes TrueType
Summary(ko.UTF-8):	자유롭게 어디든 쓸 수 있는 트루타입 글꼴을 다루는 엔진
Summary(pl.UTF-8):	Rasteryzer fontów TrueType
Summary(pt_BR.UTF-8):	Biblioteca de renderização de fontes TrueType
Summary(ru.UTF-8):	Растеризатор шрифтов TrueType
Summary(uk.UTF-8):	Растеризатор шрифтів TrueType
Name:		freetype
Version:	2.5.0.1
Release:	1
Epoch:		1
License:	GPL v2 or FTL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/freetype/%{name}-%{version}.tar.bz2
# Source0-md5:	c72e9010b1d986d556fc0b2b5fcbf31a
Source1:	http://downloads.sourceforge.net/freetype/%{name}-doc-2.5.0.tar.bz2
# Source1-md5:	40f3d5cc0b16396b3fb6b98eeaa053b2
Source2:	http://downloads.sourceforge.net/freetype/ft2demos-2.5.0.tar.bz2
# Source2-md5:	9bbea1989116715d3544d8439c8d2972
Patch0:		freetype-2.2.1-enable-valid.patch
URL:		http://www.freetype.org/
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libpng-devel
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	sed >= 4.0
%if "%{pld_release}" == "ac"
%{?with_x11:BuildRequires:	XFree86-devel}
%else
%{?with_x11:BuildRequires:	xorg-lib-libX11-devel}
%endif
BuildRequires:	zlib-devel
Obsoletes:	freetype2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	-fomit-frame-pointer
# see <freetype/internal/ftserv.h>, the real horror
%define		specflags	-fno-strict-aliasing

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
Summary:	Header files for FreeType development
Summary(es.UTF-8):	Archivos de inclusión para desarrollo con FreeType
Summary(ko.UTF-8):	FreeType을 쓸 때 필요한 정적 라이브러리와 머리말 파일
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki FreeType
Summary(pt_BR.UTF-8):	Arquivos de inclusão para desenvolvimento com FreeType
Summary(ru.UTF-8):	Библиотеки разработчика для freetype
Summary(uk.UTF-8):	Бібліотеки програміста для freetype
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bzip2-devel
Requires:	libpng-devel
Requires:	zlib-devel
Obsoletes:	freetype2-devel

%description devel
This package includes the header files necessary to develop
applications that use FreeType.

%description devel -l es.UTF-8
Este paquete es necesario, si pretendes desarrollar/compilar
aplicaciones con la biblioteca FreeType. Si, simplemente, deseas
ejecutar aplicaciones existentes, no lo necesitas.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe potrzebne przy tworzeniu programów
wykorzystujących bibliotekę FreeType.

%description devel -l pt_BR.UTF-8
Este pacote é necessário se você pretende desenvolver/compilar
aplicações com a biblioteca FreeType. Se você simplesmente deseja
rodar aplicações existentes, você não precisa deste pacote.

%description devel -l ru.UTF-8
Этот пакет содержит хедеры необходимые для разработки программ,
использующих FreeType.

%description devel -l uk.UTF-8
Цей пакет містить хедери необхідні для розробки програм, що
використовують FreeType.

%package apidocs
Summary:	FreeType API documetation
Summary(pl.UTF-8):	Dokumentacja API FreeType
Group:		Documentation

%description apidocs
FreeType API documetation.

%description apidocs -l pl.UTF-8
Dokumentacja API FreeType.

%package static
Summary:	FreeType static libraries
Summary(es.UTF-8):	Static libraries for freetype development
Summary(pl.UTF-8):	Biblioteki statyczne FreeType
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com freetype
Summary(ru.UTF-8):	Статические библиотеки freetype
Summary(uk.UTF-8):	Статичні бібліотеки freetype
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
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
Summary(ko.UTF-8):	FreeType을 시험해볼 수 있는 프로그램 모음
Summary(pl.UTF-8):	Programy demonstracyjne FreeType
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description demos
Demonstration programs for FreeType library.

%description demos -l pl.UTF-8
Programy demonstracyjne do biblioteki FreeType.

%prep
%setup -q -a1 -a2
%patch0 -p1

# avoid propagating -L%{_libdir} through *.la
%{__sed} -i -e 's,libpng-config --ldflags,libpng-config --libs,' builds/unix/configure

%build
CFLAGS="%{rpmcflags} %{rpmcppflags} \
%{?with_lcd:-DFT_CONFIG_OPTION_SUBPIXEL_RENDERING} \
-DTT_CONFIG_OPTION_SUBPIXEL_HINTING \
" \
%{__make} setup unix \
	CFG="--prefix=%{_prefix} --libdir=%{_libdir}"

%{__make} \
	X11_LIB=%{?_x_libraries}

%if %{with x11}
%{__make} -C ft2demos-* \
	TOP_DIR=$(pwd) \
	X11_LIB=%{?_x_libraries}
%endif

%{__make} refdoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with x11}
install -p ft2demos-*/bin/.libs/ft* $RPM_BUILD_ROOT%{_bindir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/{CHANGES,FTL.TXT,LICENSE.TXT,TODO,formats.txt,raster.txt}
%attr(755,root,root) %{_libdir}/libfreetype.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfreetype.so.6

%files devel
%defattr(644,root,root,755)
%doc docs/DEBUG
%attr(755,root,root) %{_bindir}/freetype-config
%attr(755,root,root) %{_libdir}/libfreetype.so
%{_libdir}/libfreetype.la
%{_includedir}/freetype2
%{_includedir}/ft2build.h
%{_aclocaldir}/freetype2.m4
%{_pkgconfigdir}/freetype2.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc docs/reference
%endif

%files static
%defattr(644,root,root,755)
%{_libdir}/libfreetype.a

%if %{with x11}
%files demos
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ft*
%endif
