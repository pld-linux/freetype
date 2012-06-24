#
# Conditional build:
# _without_bytecode	- without TT bytecode interpreter
#			(patents pending in USA, Japan...)
#
Summary:	TrueType font rasterizer
Summary(es):	Biblioteca de render 3D de fuentes TrueType
Summary(pl):	Rasteryzer font�w TrueType
Summary(pt_BR):	Biblioteca de renderiza��o de fontes TrueType
Summary(ru):	������������ ������� TrueType
Summary(uk):	������������ ����Ԧ� TrueType
Name:		freetype
Version:	2.1.2
Release:	2
License:	GPL or FTL
Group:		Libraries
Source0:	ftp://ftp.freetype.org/freetype/freetype2/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.freetype.org/freetype/freetype2/ftdocs-%{version}.tar.bz2
Source2:	ftp://ftp.freetype.org/freetype/freetype2/ft2demos-%{version}.tar.bz2
Patch0:		%{name}2-DESTDIR.patch
Patch1:		%{name}2-bytecode.patch
Patch2:		%{name}2-bluefuzz.patch
Patch3:		%{name}2-cvs-autohint.patch
Patch4:		%{name}2-fix-metrics.patch
Patch5:		%{name}2-missing-glyph.patch
Patch6:		%{name}2-ps-hinter.patch
Patch7:		%{name}2-slighthint.patch
Patch8:		%{name}2-transform.patch
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

%description -l es
FreeType es una m�quina libre y port�til para en render de fuentes
TrueType. Fue desarrollada para ofrecer soporte TrueType a una gran
variedad de plataformas y ambientes. Observa que FreeType es una
biblioteca y no una aplicaci�n, a pesar de que algunos utilitarios se
incluyan en este paquete.

%description -l pl
FreeType jest bibliotek� s�u��c� do rasteryzacji font�w TrueType. Jest
to jedynie biblioteka, a nie serwer font�w, chocia� zosta�a ona
zaprojektowana do u�ywania tak�e w takich serwerach. Nie jest to te�
kompletna biblioteka do rasteryzacji tekstu. Jej celem jest tylko
odczytywanie i zarz�dzanie plikami z fontami oraz wczytywanie i
wykonywanie hintingu i rasteryzacji poszczeg�lnych glif�w. Mo�e by�
tak�e uwa�ana za "sterownik TrueType" dla bibliotek wy�szego poziomu,
jednak u�ycie samej biblioteki FreeType do rasteryzacji jest bardzo
proste, co mo�na zobaczy� w programach demonstracyjnych.

%description -l pt_BR
FreeType � uma m�quina livre e port�vel para renderiza��o de fontes
TrueType. Ela foi desenvolvida para fornecer suporte TrueType a uma
grande variedade de plataformas e ambientes. Note que FreeType � uma
biblioteca e n�o uma aplica��o, apesar que alguns utilit�rios s�o
inclu�dos neste pacote.

%description -l ru
���������� FreeType - ��� ��������� ����������� ���������� ���
���������� (������������) ������� TrueType, ��������� � ��������
������� �� ANSI C � Pascal. ��� ���� ����������� ��� ��������� TT ��
������������� ����������.

%description -l uk
��̦����� FreeType - �� צ���� ���������� ¦�̦����� ��� ����������
(���������æ�) ����Ԧ� TrueType, �� ����������դ���� � ��Ȧ����
������� �� C �� Pascal. ���� ���� ���������� ��� Ц������� TT ��
Ҧ���� ����������.

%package devel
Summary:	Header files and development documentation
Summary(es):	Archivos de inclusi�n e bibliotecas est�ticas para desarrollo con FreeType.
Summary(pl):	Pliki nag��wkowe biblioteki freetype i dokumentacja
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas est�ticas para desenvolvimento com FreeType.
Summary(ru):	���������� ������������ ��� freetype
Summary(uk):	��̦����� ������ͦ��� ��� freetype
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	freetype2-devel

%description devel
This package includes the header files and documentation necessary to
develop applications that use FreeType.

%description devel -l es
Este paquete es necesario, si pretendes desarrollar/compilar
aplicaciones con la biblioteca FreeType. Si, simplemente, deseas
ejecutar aplicaciones existentes, no lo necesitas.

%description devel -l pl
Pakiet ten zawiera pliki nag��wkowe oraz dokumentacj� potrzebne przy
tworzeniu program�w wykorzystuj�cych bibliotek� FreeType.

%description devel -l pt_BR
Este pacote � necess�rio se voc� pretende desenvolver/compilar
aplica��es com a biblioteca FreeType. Se voc� simplesmente deseja
rodar aplica��es existentes, voc� n�o precisa deste pacote.

%description devel -l ru
���� ����� �������� ������ � ����������, ����������� ��� ����������
��������, ������������ freetype.

%description devel -l uk
��� ����� ͦ����� ������ �� ¦�̦�����, ����Ȧ�Φ ��� ��������
�������, �� �������������� freetype.

%package static
Summary:	FreeType static libraries
Summary(es):	Static libraries for freetype development
Summary(pl):	Biblioteki statyczne FreeType
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com freetype
Summary(ru):	����������� ���������� freetype
Summary(uk):	������Φ ¦�̦����� freetype
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
Bibliotecas est�ticas para desenvolvimento com freetype.

%description static -l ru
���� ����� �������� ����������� ����������, ����������� ��� ���������
��������, ������������ freetype.

%description static -l uk
��� ����� ͦ����� ������Φ ¦�̦�����, ����Ȧ�Φ ��� ���������
�������, �� �������������� freetype.

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
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2
%patch6 -p1
%patch7 -p1
%patch8 -p1

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
%doc docs/*.html docs/{design,freetype2,glyphs,reference,tutorial}
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
