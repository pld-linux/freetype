#
# Conditional build:
%bcond_without	bytecode	# without TT bytecode interpreter
#		 (patents pending in USA, Japan etc., but now it includes
#		  also patent-free hinting workaround)
%bcond_without	x11
#
Summary:	TrueType font rasterizer
Summary(es):	Biblioteca de render 3D de fuentes TrueType
Summary(ko):	자유롭게 어디든 쓸 수 있는 트루타입 글꼴을 다루는 엔진
Summary(pl):	Rasteryzer font�w TrueType
Summary(pt_BR):	Biblioteca de renderiza豫o de fontes TrueType
Summary(ru):	直戇텀�憫冬� 褙�팸窘 TrueType
Summary(uk):	直戇텀�憫冬� 褙�팸┹ TrueType
Name:		freetype
Version:	2.1.8
Release:	2
License:	GPL or FTL
Group:		Libraries
Source0:	ftp://ftp.freetype.org/freetype/freetype2/%{name}-%{version}.tar.bz2
# Source0-md5:	f717615787a1aadbdb164d1bc23c2308
# ftdocs-2.1.8 are empty???
#Source1:	ftp://ftp.freetype.org/freetype/freetype2/ftdocs-%{version}.tar.bz2
Source1:	ftp://ftp.freetype.org/freetype/freetype2/ftdocs-2.1.7.tar.bz2
# Source1-md5:	56579e3610482522061cfafbb788a81b
Source2:	ftp://ftp.freetype.org/freetype/freetype2/ft2demos-%{version}.tar.bz2
# Source2-md5:	8f74f908637420d54d7cc87168c0a92e
URL:		http://www.freetype.org/
BuildRequires:	SysVinit
%{?with_x11:BuildRequires:	XFree86-devel}
BuildRequires:	automake
BuildRequires:	zlib-devel
Obsoletes:	freetype2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	"-fomit-frame-pointer"
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

%description -l es
FreeType es una m�quina libre y port�til para en render de fuentes
TrueType. Fue desarrollada para ofrecer soporte TrueType a una gran
variedad de plataformas y ambientes. Observa que FreeType es una
biblioteca y no una aplicaci�n, a pesar de que algunos utilitarios se
incluyan en este paquete.

%description -l pl
FreeType jest bibliotek� s퀅엽c� do rasteryzacji font�w TrueType. Jest
to jedynie biblioteka, a nie serwer font�w, chocia� zosta쿪 ona
zaprojektowana do u퓓wania tak풽 w takich serwerach. Nie jest to te�
kompletna biblioteka do rasteryzacji tekstu. Jej celem jest tylko
odczytywanie i zarz켨zanie plikami z fontami oraz wczytywanie i
wykonywanie hintingu i rasteryzacji poszczeg�lnych glif�w. Mo풽 by�
tak풽 uwa풹na za "sterownik TrueType" dla bibliotek wy퓋zego poziomu,
jednak u퓓cie samej biblioteki FreeType do rasteryzacji jest bardzo
proste, co mo퓆a zobaczy� w programach demonstracyjnych.

%description -l pt_BR
FreeType � uma m�quina livre e port�vel para renderiza豫o de fontes
TrueType. Ela foi desenvolvida para fornecer suporte TrueType a uma
grande variedade de plataformas e ambientes. Note que FreeType � uma
biblioteca e n�o uma aplica豫o, apesar que alguns utilit�rios s�o
inclu�dos neste pacote.

%description -l ru
隋쫄�鞫탸� FreeType - 卜� 當苟謳适� 斤瑙卦譚皐� 쪼쫄�鞫탸� 켈�
瑙匡텀�曠� (怒戇텀�憫촁�) 褙�팸窘 TrueType, 켓戇徠适� � �談謳槐�
旽喀讀� 适 ANSI C � Pascal. 停� 쬔訣 怒撲좌鞫죔� 켈� 饉컴텀隷� TT 适
怒剝龜쫘줅槐� 覲죤팥魯좨.

%description -l uk
數쫄┩旽個 FreeType - 쳔 屢景适 斤瑙卦譚皐 짝쫄┩旽個 켈� 瑙匡텀�曠�
(怒戇텀�憫챈�) 褙�팸┹ TrueType, 粉 碌拍窘湛켯邏潼堂 � 慄홀켑��
旽喀讀� 适 C 讀 Pascal. 土适 쫬訣 碌撲苟謙适 켈� 揆켬虜藁� TT 适
娘剝�� 覲죤팥魯좨.

%package devel
Summary:	Header files and development documentation
Summary(es):	Archivos de inclusi�n e bibliotecas est�ticas para desarrollo con FreeType
Summary(ko):	FreeType을 쓸 때 필요한 정적 라이브러리와 머리말 파일
Summary(pl):	Pliki nag농wkowe biblioteki freetype i dokumentacja
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas est�ticas para desenvolvimento com FreeType
Summary(ru):	隋쫄�鞫탸� 怒撲좌鞫司個 켈� freetype
Summary(uk):	數쫄┩旽漑 妗逑怒稽戇� 켈� freetype
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
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
Pakiet ten zawiera pliki nag농wkowe oraz dokumentacj� potrzebne przy
tworzeniu program�w wykorzystuj켧ych bibliotek� FreeType.

%description devel -l pt_BR
Este pacote � necess�rio se voc� pretende desenvolver/compilar
aplica寤es com a biblioteca FreeType. Se voc� simplesmente deseja
rodar aplica寤es existentes, voc� n�o precisa deste pacote.

%description devel -l ru
璜鞫 僅愾� 遝컵壟�� 훅컵籠 � 쪼쫄�鞫탸�, 壙苟훰케梏� 켈� 怒撲좌鞫漑
妗逑怒袴, �唐驅媒藍憤� freetype.

%description devel -l uk
矢� 僅愾� 稽戇�潼 훅컵虜 讀 짝쫄┩旽漑, 壙苟홀켑� 켈� 碌撲苟漑
妗逑怒�, 粉 慄蓋虜戇窘藍潼 freetype.

%package static
Summary:	FreeType static libraries
Summary(es):	Static libraries for freetype development
Summary(pl):	Biblioteki statyczne FreeType
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com freetype
Summary(ru):	慙죤�使沓�� 쪼쫄�鞫탸� freetype
Summary(uk):	慙죤�奢� 짝쫄┩旽漑 freetype
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
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
璜鞫 僅愾� 遝컵壟�� 戇죤�使沓�� 쪼쫄�鞫탸�, 壙苟훰케梏� 켈� 适筋潭炚�
妗逑怒袴, �唐驅媒藍憤� freetype.

%description static -l uk
矢� 僅愾� 稽戇�潼 戇죤�奢� 짝쫄┩旽漑, 壙苟홀켑� 켈� 适筋潭鑛�
妗逑怒�, 粉 慄蓋虜戇窘藍潼 freetype.

%package demos
Summary:	FreeType demo programs
Summary(ko):	FreeType을 시험해볼 수 있는 프로그램 모음
Summary(pl):	Programy demonstracyjne FreeType
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description demos
Demonstration programs for FreeType library.

%description demos -l pl
Programy demonstracyjne do biblioteki FreeType.

%prep
%setup -q -a1 -a2

mv -f freetype-2.1.7/docs/reference/* docs/reference

%build
CFLAGS="%{rpmcflags} %{?with_bytecode:-DTT_CONFIG_OPTION_BYTECODE_INTERPRETER}" \
%{__make} setup unix \
       CFG="--prefix=%{_prefix} --libdir=%{_libdir}"

%{__make} \
	X11_LIB="/usr/X11R6/%{_lib}"

%if %{with x11}
%{__make} -C ft2demos-* \
	TOP_DIR="`pwd`" \
	X11_LIB="/usr/X11R6/%{_lib}"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with x11}
install ft2demos-*/bin/.libs/ft{multi,timer,view} $RPM_BUILD_ROOT%{_bindir}
install ft2demos-*/bin/.libs/ft{dump,lint,memchk} $RPM_BUILD_ROOT%{_bindir}
install ft2demos-*/bin/.libs/testname $RPM_BUILD_ROOT%{_bindir}/fttestname
%endif

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

%if %{with x11}
%files demos
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ft*
%endif
