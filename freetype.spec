#
# Conditional build:
%bcond_without	bytecode	# without TT bytecode interpreter
#		 (patents pending in USA, Japan etc., but now it includes
#		  also patent-free hinting workaround)
#
Summary:	TrueType font rasterizer
Summary(es):	Biblioteca de render 3D de fuentes TrueType
Summary(ko):	юзю╞╥с╟т ╬Н╣П╣Г ╬╣ ╪Ж юж╢б ф╝╥Ге╦ют ╠ш╡цю╩ ╢ы╥Г╢б ©ёаЬ
Summary(pl):	Rasteryzer fontСw TrueType
Summary(pt_BR):	Biblioteca de renderizaГЦo de fontes TrueType
Summary(ru):	Растеризатор шрифтов TrueType
Summary(uk):	Растеризатор шрифт╕в TrueType
Name:		freetype
Version:	2.1.7
Release:	1
License:	GPL or FTL
Group:		Libraries
Source0:	ftp://ftp.freetype.org/freetype/freetype2/%{name}-%{version}.tar.bz2
# Source0-md5:	d5c39853f6741c8401bfe272478958a8
Source1:	ftp://ftp.freetype.org/freetype/freetype2/ftdocs-%{version}.tar.bz2
# Source1-md5:	56579e3610482522061cfafbb788a81b
Source2:	ftp://ftp.freetype.org/freetype/freetype2/ft2demos-%{version}.tar.bz2
# Source2-md5:	89a5b3fd3177fbc71f9ba7cbc64edfa2
URL:		http://www.freetype.org/
BuildRequires:	SysVinit
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	zlib-devel
Obsoletes:	freetype2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	"-fomit-frame-pointer"

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

%description -l es
FreeType es una mАquina libre y portАtil para en render de fuentes
TrueType. Fue desarrollada para ofrecer soporte TrueType a una gran
variedad de plataformas y ambientes. Observa que FreeType es una
biblioteca y no una aplicaciСn, a pesar de que algunos utilitarios se
incluyan en este paquete.

%description -l pl
FreeType jest bibliotek╠ sЁu©╠c╠ do rasteryzacji fontСw TrueType. Jest
to jedynie biblioteka, a nie serwer fontСw, chocia© zostaЁa ona
zaprojektowana do u©ywania tak©e w takich serwerach. Nie jest to te©
kompletna biblioteka do rasteryzacji tekstu. Jej celem jest tylko
odczytywanie i zarz╠dzanie plikami z fontami oraz wczytywanie i
wykonywanie hintingu i rasteryzacji poszczegСlnych glifСw. Mo©e byФ
tak©e uwa©ana za "sterownik TrueType" dla bibliotek wy©szego poziomu,
jednak u©ycie samej biblioteki FreeType do rasteryzacji jest bardzo
proste, co mo©na zobaczyФ w programach demonstracyjnych.

%description -l pt_BR
FreeType И uma mАquina livre e portАvel para renderizaГЦo de fontes
TrueType. Ela foi desenvolvida para fornecer suporte TrueType a uma
grande variedade de plataformas e ambientes. Note que FreeType И uma
biblioteca e nЦo uma aplicaГЦo, apesar que alguns utilitАrios sЦo
incluМdos neste pacote.

%description -l ru
Библиотека FreeType - это свободная переносимая библиотека для
рендеринга (растеризации) шрифтов TrueType, доступная в исходных
текстах на ANSI C и Pascal. Она была разработана для поддержки TT на
разнообразных платформах.

%description -l uk
Б╕бл╕отека FreeType - це в╕льна переносима б╕бл╕отека для рендерингу
(растеризац╕╖) шрифт╕в TrueType, що розповсюджу╓ться у вих╕дних
текстах на C та Pascal. Вона була розроблена для п╕дтримки TT на
р╕зних платформах.

%package devel
Summary:	Header files and development documentation
Summary(es):	Archivos de inclusiСn e bibliotecas estАticas para desarrollo con FreeType
Summary(ko):	FreeTypeю╩ ╬╣ ╤╖ гй©Дгя а╓юШ ╤Сюл╨Й╥╞╦╝©м ╦с╦╝╦╩ фдюо
Summary(pl):	Pliki nagЁСwkowe biblioteki freetype i dokumentacja
Summary(pt_BR):	Arquivos de inclusЦo e bibliotecas estАticas para desenvolvimento com FreeType
Summary(ru):	Библиотеки разработчика для freetype
Summary(uk):	Б╕бл╕отеки програм╕ста для freetype
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	zlib-devel
Obsoletes:	freetype2-devel

%description devel
This package includes the header files and documentation necessary to
develop applications that use FreeType.

%description devel -l es
Este paquete es necesario, si pretendes desarrollar/compilar
aplicaciones con la biblioteca FreeType. Si, simplemente, deseas
ejecutar aplicaciones existentes, no lo necesitas.

%description devel -l pl
Pakiet ten zawiera pliki nagЁСwkowe oraz dokumentacjЙ potrzebne przy
tworzeniu programСw wykorzystuj╠cych bibliotekЙ FreeType.

%description devel -l pt_BR
Este pacote И necessАrio se vocЙ pretende desenvolver/compilar
aplicaГУes com a biblioteca FreeType. Se vocЙ simplesmente deseja
rodar aplicaГУes existentes, vocЙ nЦo precisa deste pacote.

%description devel -l ru
Этот пакет содержит хедеры и библиотеки, необходимые для разработки
программ, использующих freetype.

%description devel -l uk
Цей пакет м╕стить хедери та б╕бл╕отеки, необх╕дн╕ для розробки
програм, що використовують freetype.

%package static
Summary:	FreeType static libraries
Summary(es):	Static libraries for freetype development
Summary(pl):	Biblioteki statyczne FreeType
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com freetype
Summary(ru):	Статические библиотеки freetype
Summary(uk):	Статичн╕ б╕бл╕отеки freetype
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	freetype2-static

%description static
Static FreeType libraries.

%description static -l es
Static libraries for freetype development.

%description static -l pl
Biblioteki statyczne FreeType.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com freetype.

%description static -l ru
Этот пакет содержит статические библиотеки, необходимые для написания
программ, использующих freetype.

%description static -l uk
Цей пакет м╕стить статичн╕ б╕бл╕отеки, необх╕дн╕ для написання
програм, що використовують freetype.

%package demos
Summary:	FreeType demo programs
Summary(ko):	FreeTypeю╩ ╫цгХгь╨╪ ╪Ж юж╢б га╥н╠в╥╔ ╦Пю╫
Summary(pl):	Programy demonstracyjne FreeType
Group:		X11/Applications
Requires:	%{name} = %{version}

%description demos
Demonstration programs for FreeType library.

%description demos -l pl
Programy demonstracyjne do biblioteki FreeType.

%prep
%setup -q -a1 -a2

mv -f freetype-%{version}/docs/reference/* docs/reference

%build
CFLAGS="%{rpmcflags} %{?with_bytecode:-DTT_CONFIG_OPTION_BYTECODE_INTERPRETER}" \
%{__make} setup unix \
	CFG="--prefix=%{_prefix}"

%{__make}
%{__make} -C ft2demos-* \
	TOP_DIR="`pwd`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	datadir=%{_datadir}

install ft2demos-*/bin/.libs/ft{multi,timer,view} $RPM_BUILD_ROOT%{_bindir}
install ft2demos-*/bin/.libs/ft{dump,lint,memchk} $RPM_BUILD_ROOT%{_bindir}
install ft2demos-*/bin/.libs/testname $RPM_BUILD_ROOT%{_bindir}/fttestname

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/{CHANGES,FTL.txt,PATENTS,license.txt,TODO,modules.txt}
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/{DEBUG,TRUETYPE} docs/reference
%attr(755,root,root) %{_bindir}/freetype-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/freetype2
%{_includedir}/*.h
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files demos
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ft*
