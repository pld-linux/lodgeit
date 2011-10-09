Summary:	Command line Lodge It
Summary(pl.UTF-8):	Klient Lodge It (jak pastebin) działający z linii poleceń
Name:		lodgeit
# latest date at http://dev.pocoo.org/hg/lodgeit-main
Version:	20100919
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://dev.pocoo.org/hg/lodgeit-main/raw-file/tip/scripts/%{name}.py
# Source0-md5:	f88ed5c59bbf0d779d86526ac21a8f1c
URL:		http://paste.pocoo.org/help/integration/
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line interface to "Lodge It" (pastebin-like) service.

%description -l pl
Interfejs linii poleceń do serwisu "Lodge It" (podobnego do pastebin).

%prep
%setup -q -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lodgeit
