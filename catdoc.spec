Summary:	reads MS-Word file and puts its content as plain text on standard output
Name:		catdoc
Version:	0.91.4
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	http://www.ice.ru/~vitus/catdoc/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CATDOC is program which reads MS-Word file and prints readable ASCII
text to stdout, just like Unix cat command. It also able to produce
correct escape sequences if some UNICODE charachers have to be
represented specially in your typesetting system such as (La)TeX.

%prep
%setup -q -n %{name}

%build
%configure --with-wish=/usr/bin/wish

%{__make} FLAGS="%{?debug:-g -O}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	installroot=$RPM_BUILD_ROOT \
	mandir=%{_mandir}/man1

gzip -9nf CREDITS README NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755, root, root) %{_bindir}/*
%{_libdir}/catdoc
%{_mandir}/man1/*
