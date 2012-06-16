Summary:	HTML to XHTML convertor
Summary(pl.UTF-8):	Konwerter z HTML do XHTML
Name:		htx
Version:	0.7.8
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://stuff.myrealm.co.uk/htx/%{name}-%{version}.tar.gz
# Source0-md5:	bd332030ed20e20ca0757b3e18bb1240
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
