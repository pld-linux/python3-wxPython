%define		module	wxPython
Summary:	Cross platform GUI toolkit for Python
Summary(pl.UTF-8):	Wieloplatformowe narzędzie GUI dla Pythona
Name:		python3-%{module}
Version:	4.2.1
Release:	1
License:	wxWindows Library Licence 3.1 (LGPL v2+ with exception)
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/w/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	e62c5bd836d2a9dcb6e955509715b157
Source1:	%{name}-wxversion-null.py
Patch0:		%{name}-CFLAGS.patch
URL:		http://wxpython.org/
BuildRequires:	gtk+3-devel
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:2.5
BuildRequires:	python3-devel >= 1:2.5
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
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
	--jobs=%{__jobs} \
	--verbose \
	--python=%{__python3} \
	--use_syswx

%install
rm -rf $RPM_BUILD_ROOT

WX_CONFIG=%{_bindir}/wx-gtk3-unicode-config \
%{__python3} build.py install_py \
	--jobs=%{__jobs} \
	--verbose \
	--python=%{__python3} \
	--destdir=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{py3_sitedir}/wxversion.py

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
rm -f $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/samples/embedded/embedded
rm -f $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/samples/embedded/embedded.o

%{__mv} $RPM_BUILD_ROOT%{py3_sitedir}/wx/lib/editor/README.txt README.editor.txt

install -d $RPM_BUILD_ROOT%{_datadir}
%{__mv} $RPM_BUILD_ROOT%{py3_sitedir}/wx/locale $RPM_BUILD_ROOT%{_datadir}
ln -sfr $RPM_BUILD_ROOT%{_localedir} $RPM_BUILD_ROOT%{py3_sitedir}/wx/locale

%find_lang wxstd

%clean
rm -rf $RPM_BUILD_ROOT

%files -f wxstd.lang
%defattr(644,root,root,755)
%doc CHANGES.rst docs/MigrationGuide.rst README.rst README.editor.txt
#don't remove these files, because this is licensing information
%doc license/{licence,preamble,sip-license}.txt
%attr(755,root,root) %{_bindir}/helpviewer
%attr(755,root,root) %{_bindir}/img2png
%attr(755,root,root) %{_bindir}/img2py
%attr(755,root,root) %{_bindir}/img2xpm
%attr(755,root,root) %{_bindir}/pycrust
%attr(755,root,root) %{_bindir}/pyshell
%attr(755,root,root) %{_bindir}/pyslices
%attr(755,root,root) %{_bindir}/pyslicesshell
%attr(755,root,root) %{_bindir}/pywxrc
%attr(755,root,root) %{_bindir}/wxdemo
%attr(755,root,root) %{_bindir}/wxdocs
%attr(755,root,root) %{_bindir}/wxget

%{py3_sitedir}/wxversion.py

%dir %{py3_sitedir}/wx
%attr(755,root,root) %{py3_sitedir}/wx/*.so
%{py3_sitedir}/wx/__pycache__
%{py3_sitedir}/wx/*.py
%{py3_sitedir}/wx/*.pyi
%dir %{py3_sitedir}/wx/lib
%{py3_sitedir}/wx/lib/myole4ax.*
%{py3_sitedir}/wx/lib/__pycache__
%{py3_sitedir}/wx/lib/*.py
%dir %{py3_sitedir}/wx/lib/analogclock
%{py3_sitedir}/wx/lib/analogclock/__pycache__
%{py3_sitedir}/wx/lib/analogclock/*.py
%dir %{py3_sitedir}/wx/lib/analogclock/lib_setup
%{py3_sitedir}/wx/lib/analogclock/lib_setup/__pycache__
%{py3_sitedir}/wx/lib/analogclock/lib_setup/*.py
%dir %{py3_sitedir}/wx/lib/art
%{py3_sitedir}/wx/lib/art/__pycache__
%{py3_sitedir}/wx/lib/art/*.py
%dir %{py3_sitedir}/wx/lib/colourchooser
%{py3_sitedir}/wx/lib/colourchooser/__pycache__
%{py3_sitedir}/wx/lib/colourchooser/*.py
%dir %{py3_sitedir}/wx/lib/editor
%{py3_sitedir}/wx/lib/editor/__pycache__
%{py3_sitedir}/wx/lib/editor/*.py
%dir %{py3_sitedir}/wx/lib/floatcanvas
%{py3_sitedir}/wx/lib/floatcanvas/__pycache__
%{py3_sitedir}/wx/lib/floatcanvas/*.py
%dir %{py3_sitedir}/wx/lib/floatcanvas/Utilities
%{py3_sitedir}/wx/lib/floatcanvas/Utilities/__pycache__
%{py3_sitedir}/wx/lib/floatcanvas/Utilities/*.py
%dir %{py3_sitedir}/wx/lib/gizmos
%{py3_sitedir}/wx/lib/gizmos/__pycache__
%{py3_sitedir}/wx/lib/gizmos/*.py
%dir %{py3_sitedir}/wx/lib/masked
%{py3_sitedir}/wx/lib/masked/__pycache__
%{py3_sitedir}/wx/lib/masked/*.py
%dir %{py3_sitedir}/wx/lib/mixins
%{py3_sitedir}/wx/lib/mixins/__pycache__
%{py3_sitedir}/wx/lib/mixins/*.py
%dir %{py3_sitedir}/wx/lib/ogl
%{py3_sitedir}/wx/lib/ogl/__pycache__
%{py3_sitedir}/wx/lib/ogl/*.py
%dir %{py3_sitedir}/wx/lib/agw
%{py3_sitedir}/wx/lib/agw/__pycache__
%{py3_sitedir}/wx/lib/agw/*.py
%{py3_sitedir}/wx/lib/agw/data
%dir %{py3_sitedir}/wx/lib/agw/aui
%{py3_sitedir}/wx/lib/agw/aui/__pycache__
%{py3_sitedir}/wx/lib/agw/aui/*.py
%dir %{py3_sitedir}/wx/lib/agw/persist
%{py3_sitedir}/wx/lib/agw/persist/__pycache__
%{py3_sitedir}/wx/lib/agw/persist/*.py
%dir %{py3_sitedir}/wx/lib/agw/ribbon
%{py3_sitedir}/wx/lib/agw/ribbon/__pycache__
%{py3_sitedir}/wx/lib/agw/ribbon/*.py
%dir %{py3_sitedir}/wx/lib/pdfviewer
%{py3_sitedir}/wx/lib/pdfviewer/__pycache__
%{py3_sitedir}/wx/lib/pdfviewer/*.py
%dir %{py3_sitedir}/wx/lib/pdfviewer/bitmaps
%{py3_sitedir}/wx/lib/pdfviewer/bitmaps/__pycache__
%{py3_sitedir}/wx/lib/pdfviewer/bitmaps/*.py
%{py3_sitedir}/wx/lib/pdfviewer/bitmaps/*.png
%dir %{py3_sitedir}/wx/lib/plot
%{py3_sitedir}/wx/lib/plot/__pycache__
%{py3_sitedir}/wx/lib/plot/*.py
%dir %{py3_sitedir}/wx/lib/pubsub
%{py3_sitedir}/wx/lib/pubsub/__pycache__
%{py3_sitedir}/wx/lib/pubsub/*.py
%dir %{py3_sitedir}/wx/lib/pubsub/core
%{py3_sitedir}/wx/lib/pubsub/core/__pycache__
%{py3_sitedir}/wx/lib/pubsub/core/*.py
%dir %{py3_sitedir}/wx/lib/pubsub/core/arg1
%{py3_sitedir}/wx/lib/pubsub/core/arg1/__pycache__
%{py3_sitedir}/wx/lib/pubsub/core/arg1/*.py
%dir %{py3_sitedir}/wx/lib/pubsub/core/kwargs
%{py3_sitedir}/wx/lib/pubsub/core/kwargs/__pycache__
%{py3_sitedir}/wx/lib/pubsub/core/kwargs/*.py
%dir %{py3_sitedir}/wx/lib/pubsub/utils
%{py3_sitedir}/wx/lib/pubsub/utils/__pycache__
%{py3_sitedir}/wx/lib/pubsub/utils/*.py
%dir %{py3_sitedir}/wx/lib/wxcairo
%{py3_sitedir}/wx/lib/wxcairo/__pycache__
%{py3_sitedir}/wx/lib/wxcairo/*.py
%dir %{py3_sitedir}/wx/py
%{py3_sitedir}/wx/py/*.ico
%{py3_sitedir}/wx/py/*.png
%{py3_sitedir}/wx/py/__pycache__
%{py3_sitedir}/wx/py/*.py
%doc %{py3_sitedir}/wx/py/*.txt
%dir %{py3_sitedir}/wx/svg
%{py3_sitedir}/wx/svg/__pycache__
%attr(755,root,root) %{py3_sitedir}/wx/svg/*.so
%{py3_sitedir}/wx/svg/*.py
%dir %{py3_sitedir}/wx/tools
%{py3_sitedir}/wx/tools/__pycache__
%{py3_sitedir}/wx/tools/*.py

%{py3_sitedir}/wx/locale
%{py3_sitedir}/wxPython-*.egg-info

%files devel
%defattr(644,root,root,755)
%{py3_sitedir}/wx/include

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
