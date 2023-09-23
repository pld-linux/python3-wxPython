# TODO: move Editra locale (.mo) files to system LC_MESSAGES dirs
%define		module	wxPython
Summary:	Cross platform GUI toolkit for Python
Summary(pl.UTF-8):	Wieloplatformowe narzędzie GUI dla Pythona
Name:		python3-%{module}
Version:	4.2.1
Release:	0.1
License:	wxWindows Library Licence 3.1 (LGPL v2+ with exception)
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/w/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	e62c5bd836d2a9dcb6e955509715b157
Source1:	%{name}-wxversion-null.py
Patch0:		%{name}-CFLAGS.patch
URL:		http://wxpython.org/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	gtk+3-devel
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:2.5
BuildRequires:	python3-devel >= 1:2.5
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	wxGTK3-unicode-gl-devel >= 3.2
# optional: gstreamer 1.7.2
Requires:	python3-modules
Requires:	wxGTK3-unicode-gl >= 3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxPython is a GUI toolkit for Python that is a wrapper around the
wxWidgets C++ GUI library. wxPython provides a large variety of window
types and controls, all implemented with a native look and feel (and
native runtime speed) on the platforms it is supported on.

%description -l pl.UTF-8
wxPython jest narzędziem GUI dla Pythona będącym nakładką na
bibliotekę GUI napisaną w C++ o nazwie wxWidgets. wxPython dostarcza
dużą liczbę typów okien, kontrolek.

%package devel
Summary:	Header and SWIG files for wxPython
Summary(pl.UTF-8):	Pliki nagłówkowe i SWIG dla wxPythona
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wxWidgets-devel >= 2.8.7

%description devel
Header and SWIG files for wxPython.

%description devel -l pl.UTF-8
Pliki nagłówkowe i SWIG dla wxPythona.

%package editra
Summary:	Editra editor
Summary(pl.UTF-8):	Edytor Editra
Group:		Development/Tools
URL:		http://editra.org/
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	%{name} = %{version}-%{release}

%description editra
Editra is a multi-platform text editor with an implementation that
focuses on creating an easy to use interface and features that aid in
code development. Currently it supports syntax highlighting and
variety of other useful features for over 50 programming languages.

%description editra -l pl.UTF-8
Editra to wieloplatformowy edytor tekstu, którego implementacja skupia
się na stworzeniu łatwego w użyciu interfejsu i możliwościach
pomagających w tworzeniu kodu. Aktualnie obsługuje podświetlanie
składni i różne przydatne ułatwienia dla ponad 50 języków
programowania.

%package xrced
Summary:	XRCed - XRC files editor
Summary(pl.UTF-8):	XRCed - edytor plików XRC
License:	BSD
Group:		Development/Tools
URL:		http://xrced.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	%{name} = %{version}-%{release}

%description xrced
XRCed is a simple resource editor for wxWidgets/wxPython GUI
development which supports creating and editing files in XRC format.
It is written in Python and uses wxPython GUI toolkit.

%description xrced -l pl.UTF-8
XRCed to prosty edytor zasobów do programowania w środowisku
graficznym wxWidgets/wxPython, pozwalający na tworzenie i
modyfikowanie plików w formacie XRC. Został napisany w Pythonie i
wykorzystuje toolkit graficzny wxPython.

%package examples
Summary:	wxPython example programs
Summary(pl.UTF-8):	Przykładowe programy wxPython
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description examples
wxPython example programs.

%description examples -l pl.UTF-8
Przykładowe programy w wxPythonie.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python3}\1,' \
	demo/*.py \
	samples/*/*.py

%build
WX_CONFIG=%{_bindir}/wx-gtk3-unicode-config \
%{__python3} build.py build_py \
	--verbose \
	--python=%{__python3} \
	--use_syswx

%install
rm -rf $RPM_BUILD_ROOT

WX_CONFIG=%{_bindir}/wx-gtk3-unicode-config \
%{__python3} build.py install_py \
	--verbose \
	--python=%{__python3} \
	--destdir=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{py3_sitedir}/wxversion.py

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
rm -f $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/samples/embedded/embedded
rm -f $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/samples/embedded/embedded.o

%{__mv} $RPM_BUILD_ROOT%{py3_sitedir}/wx/lib/editor/README.txt README.editor.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc wxPython/docs/{CHANGES.txt,MigrationGuide.txt,README.txt} wxPython/README.editor.txt
#don't remove these files, because this is licensing information
%doc docs/{licence.txt,licendoc.txt,preamble.txt}
%attr(755,root,root) %{_bindir}/helpviewer
%attr(755,root,root) %{_bindir}/img2png
%attr(755,root,root) %{_bindir}/img2py
%attr(755,root,root) %{_bindir}/img2xpm
%attr(755,root,root) %{_bindir}/pyalacarte
%attr(755,root,root) %{_bindir}/pyalamode
%attr(755,root,root) %{_bindir}/pycrust
%attr(755,root,root) %{_bindir}/pyshell
%attr(755,root,root) %{_bindir}/pywrap
%attr(755,root,root) %{_bindir}/pywxrc

%{py3_sitedir}/wxversion.py

%dir %{py3_sitedir}/wx
%attr(755,root,root) %{py3_sitedir}/wx/*.so
%{py3_sitedir}/wx/*.py
%dir %{py3_sitedir}/wx/build
%{py3_sitedir}/wx/build/*.py
%dir %{py3_sitedir}/wx/lib
%{py3_sitedir}/wx/lib/*.py
%dir %{py3_sitedir}/wx/lib/analogclock
%{py3_sitedir}/wx/lib/analogclock/*.py
%dir %{py3_sitedir}/wx/lib/analogclock/lib_setup
%{py3_sitedir}/wx/lib/analogclock/lib_setup/*.py
%dir %{py3_sitedir}/wx/lib/art
%{py3_sitedir}/wx/lib/art/*.py
%dir %{py3_sitedir}/wx/lib/colourchooser
%{py3_sitedir}/wx/lib/colourchooser/*.py
%dir %{py3_sitedir}/wx/lib/editor
%{py3_sitedir}/wx/lib/editor/*.py
%dir %{py3_sitedir}/wx/lib/floatcanvas
%{py3_sitedir}/wx/lib/floatcanvas/*.py
%dir %{py3_sitedir}/wx/lib/floatcanvas/Utilities
%{py3_sitedir}/wx/lib/floatcanvas/Utilities/*.py
%dir %{py3_sitedir}/wx/lib/masked
%{py3_sitedir}/wx/lib/masked/*.py
%dir %{py3_sitedir}/wx/lib/mixins
%{py3_sitedir}/wx/lib/mixins/*.py
%dir %{py3_sitedir}/wx/lib/ogl
%{py3_sitedir}/wx/lib/ogl/*.py
%dir %{py3_sitedir}/wx/lib/agw
%{py3_sitedir}/wx/lib/agw/*.py
%{py3_sitedir}/wx/lib/agw/data
%dir %{py3_sitedir}/wx/lib/agw/aui
%{py3_sitedir}/wx/lib/agw/aui/*.py
%dir %{py3_sitedir}/wx/lib/agw/persist
%{py3_sitedir}/wx/lib/agw/persist/*.py
%dir %{py3_sitedir}/wx/lib/agw/ribbon
%{py3_sitedir}/wx/lib/agw/ribbon/*.py
%dir %{py3_sitedir}/wx/lib/pdfviewer
%{py3_sitedir}/wx/lib/pdfviewer/*.py
%dir %{py3_sitedir}/wx/lib/pubsub
%{py3_sitedir}/wx/lib/pubsub/*.py
%dir %{py3_sitedir}/wx/lib/pubsub/core
%{py3_sitedir}/wx/lib/pubsub/core/*.py
%dir %{py3_sitedir}/wx/lib/pubsub/core/arg1
%{py3_sitedir}/wx/lib/pubsub/core/arg1/*.py
%dir %{py3_sitedir}/wx/lib/pubsub/core/kwargs
%{py3_sitedir}/wx/lib/pubsub/core/kwargs/*.py
%dir %{py3_sitedir}/wx/lib/pubsub/utils
%{py3_sitedir}/wx/lib/pubsub/utils/*.py
%dir %{py3_sitedir}/wx/py
%{py3_sitedir}/wx/py/*.ico
%{py3_sitedir}/wx/py/*.py
%doc %{py3_sitedir}/wx/py/*.txt
%dir %{py3_sitedir}/wx/tools
%{py3_sitedir}/wx/tools/*.py
%dir %{py3_sitedir}/wx/tools/XRCed
%{py3_sitedir}/wx/tools/XRCed/*.py
%doc %{py3_sitedir}/wx/tools/XRCed/*.txt
%{py3_sitedir}/wx/tools/XRCed/*.xrc

%{py3_sitedir}/wxPython-*.egg-info

%files devel
%defattr(644,root,root,755)
%{_includedir}/wx-3.0/wx/wxPython

%files editra
%defattr(644,root,root,755)
%doc wxPython/wx/tools/Editra/{AUTHORS,CHANGELOG,COPYING,FAQ,NEWS,README,THANKS,TODO,docs/*.txt}
%attr(755,root,root) %{_bindir}/editra
%dir %{py3_sitedir}/wx/tools/Editra
%{py3_sitedir}/wx/tools/Editra/__init__.py
%{py3_sitedir}/wx/tools/Editra/launcher.py
%{py3_sitedir}/wx/tools/Editra/Editra.pyw
%dir %{py3_sitedir}/wx/tools/Editra/locale
%lang(ca) %{py3_sitedir}/wx/tools/Editra/locale/ca_ES@valencia
%lang(cs) %{py3_sitedir}/wx/tools/Editra/locale/cs_CZ
%lang(da) %{py3_sitedir}/wx/tools/Editra/locale/da_DK
%lang(de) %{py3_sitedir}/wx/tools/Editra/locale/de_DE
%lang(en) %{py3_sitedir}/wx/tools/Editra/locale/en_US
%lang(es) %{py3_sitedir}/wx/tools/Editra/locale/es_ES
%lang(fr) %{py3_sitedir}/wx/tools/Editra/locale/fr_FR
%lang(gl) %{py3_sitedir}/wx/tools/Editra/locale/gl_ES
%lang(hr) %{py3_sitedir}/wx/tools/Editra/locale/hr_HR
%lang(hu) %{py3_sitedir}/wx/tools/Editra/locale/hu_HU
%lang(it) %{py3_sitedir}/wx/tools/Editra/locale/it_IT
%lang(ja) %{py3_sitedir}/wx/tools/Editra/locale/ja_JP
%lang(lv) %{py3_sitedir}/wx/tools/Editra/locale/lv_LV
%lang(nl) %{py3_sitedir}/wx/tools/Editra/locale/nl_NL
%lang(nn) %{py3_sitedir}/wx/tools/Editra/locale/nn_NO
%lang(pl) %{py3_sitedir}/wx/tools/Editra/locale/pl_PL
%lang(pt_BR) %{py3_sitedir}/wx/tools/Editra/locale/pt_BR
%lang(ro) %{py3_sitedir}/wx/tools/Editra/locale/ro_RO
%lang(ru) %{py3_sitedir}/wx/tools/Editra/locale/ru_RU
%lang(sk) %{py3_sitedir}/wx/tools/Editra/locale/sk_SK
%lang(sl) %{py3_sitedir}/wx/tools/Editra/locale/sl_SI
%lang(sr) %{py3_sitedir}/wx/tools/Editra/locale/sr_RS
%lang(sv) %{py3_sitedir}/wx/tools/Editra/locale/sv_SE
%lang(tr) %{py3_sitedir}/wx/tools/Editra/locale/tr_TR
%lang(uk) %{py3_sitedir}/wx/tools/Editra/locale/uk_UA
%lang(zh_CN) %{py3_sitedir}/wx/tools/Editra/locale/zh_CN
%lang(zh_TW) %{py3_sitedir}/wx/tools/Editra/locale/zh_TW
%{py3_sitedir}/wx/tools/Editra/pixmaps
%dir %{py3_sitedir}/wx/tools/Editra/src
%{py3_sitedir}/wx/tools/Editra/src/*.py
%dir %{py3_sitedir}/wx/tools/Editra/src/autocomp
%{py3_sitedir}/wx/tools/Editra/src/autocomp/*.py
%dir %{py3_sitedir}/wx/tools/Editra/src/eclib
%{py3_sitedir}/wx/tools/Editra/src/eclib/*.py
%dir %{py3_sitedir}/wx/tools/Editra/src/extern
%{py3_sitedir}/wx/tools/Editra/src/extern/*.py
%dir %{py3_sitedir}/wx/tools/Editra/src/syntax
%{py3_sitedir}/wx/tools/Editra/src/syntax/*.py
%dir %{py3_sitedir}/wx/tools/Editra/src/ebmlib
%{py3_sitedir}/wx/tools/Editra/src/ebmlib/*.py
%{py3_sitedir}/wx/tools/Editra/styles

%files xrced
%defattr(644,root,root,755)
%doc wxPython/wx/tools/XRCed/{CHANGES.txt,ChangeLog,README.txt,TODO.txt,license.txt}
%attr(755,root,root) %{_bindir}/xrced
%dir %{py3_sitedir}/wx/tools/XRCed
%{py3_sitedir}/wx/tools/XRCed/misc
%dir %{py3_sitedir}/wx/tools/XRCed/plugins
%{py3_sitedir}/wx/tools/XRCed/plugins/*.py
%{py3_sitedir}/wx/tools/XRCed/plugins/bitmaps
%{py3_sitedir}/wx/tools/XRCed/plugins/gizmos.crx
%{py3_sitedir}/wx/tools/XRCed/xrced.htb

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
