Summary:	Reads MS-Word file and puts its content as plain text on standard output
Summary(pl):	Program konwertuj±cy pliki MS Worda na czysty tekst
Name:		catdoc
Version:	0.91.5
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.ice.ru/pub/vitus/%{name}-%{version}.tar.gz
URL:		http://www.ice.ru/~vitus/catdoc/
BuildRequires:	tk
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CATDOC is program which reads MS-Word file and prints readable ASCII
text to stdout, just like Unix cat command. It is also able to produce
correct escape sequences if some UNICODE characters have to be
represented specially in your typesetting system such as (La)TeX.

%description -l pl
catdoc jest programem czytaj±cym dokumenty MS-Worda i wypisuj±cym
tekst ASCII na standardowe wyj¶cie, podobnie jak komenda cat. Mo¿e
tak¿e tworzyæ poprawne sekwencje dla niektórych znaków unikodowych
reprezentowanych specjalnie w systemie sk³adu, jak np. (La)TeX.

%prep
%setup -q

%build
aclocal
%{__autoconf}
%configure \
	--with-wish=/usr/bin/wish

%{__make} FLAGS="%{rpmcflags}"

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
