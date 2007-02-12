Summary:	Reads MS-Word file and puts its content as plain text on standard output
Summary(pl.UTF-8):   Program konwertujący pliki MS Worda na czysty tekst
Name:		catdoc
Version:	0.94.2
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	ftp://ftp.45.free.net/pub/catdoc/%{name}-%{version}.tar.gz
# Source0-md5:	243e1680bb3e703616f5adecfee24491
Patch0:		%{name}-opt.patch
URL:		http://www.45.free.net/~vitus/software/catdoc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CATDOC is program which reads MS-Word file and prints readable ASCII
text to stdout, just like Unix cat command. It is also able to produce
correct escape sequences if some UNICODE characters have to be
represented specially in your typesetting system such as (La)TeX.

%description -l pl.UTF-8
catdoc jest programem czytającym dokumenty MS-Worda i wypisującym
tekst ASCII na standardowe wyjście, podobnie jak komenda cat. Może
także tworzyć poprawne sekwencje dla niektórych znaków unikodowych
reprezentowanych specjalnie w systemie składu, jak np. (La)TeX.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure \
	--with-wish=/usr/bin/wish

%{__make}

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
