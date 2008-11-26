Summary:	HTML to XHTML convertor
Summary(pl.UTF-8):	Konwerter z HTML do XHTML
Name:		htx
Version:	0.7.6
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://stuff.myrealm.co.uk/htx/%{name}-%{version}.tar.gz
# Source0-md5:	0237ad727593646f68dbafd8e9e3e370
Requires:	perl-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML to XHTML convertor.

%description -l pl.UTF-8
Konwerter z HTML do XHTML.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install htx $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/htx
