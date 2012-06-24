Summary:	Reads MS-Word file and puts its content as plain text on standard output
Summary(pl):	Program konwertuj�cy pliki MS Worda na czysty tekst
Name:		catdoc
Version:	0.93.4
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.45.free.net/pub/catdoc/%{name}-%{version}.tar.gz
# Source0-md5:	efe7e24b387444d5967fc2fc25664fb2
# Source0-size:	121933
URL:		http://www.45.free.net/~vitus/ice/catdoc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CATDOC is program which reads MS-Word file and prints readable ASCII
text to stdout, just like Unix cat command. It is also able to produce
correct escape sequences if some UNICODE characters have to be
represented specially in your typesetting system such as (La)TeX.

%description -l pl
catdoc jest programem czytaj�cym dokumenty MS-Worda i wypisuj�cym
tekst ASCII na standardowe wyj�cie, podobnie jak komenda cat. Mo�e
tak�e tworzy� poprawne sekwencje dla niekt�rych znak�w unikodowych
reprezentowanych specjalnie w systemie sk�adu, jak np. (La)TeX.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure \
	--with-wish=/usr/bin/wish

%{__make} \
	FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	installroot=$RPM_BUILD_ROOT \
	mandir=%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/catdoc
%{_mandir}/man1/*
