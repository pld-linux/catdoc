Summary:	Reads MS-Word file and puts its content as plain text on standard output
Summary(pl.UTF-8):	Program konwertujący pliki MS Worda na czysty tekst
Name:		catdoc
Version:	0.95
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://ftp.wagner.pp.ru/pub/catdoc/%{name}-%{version}.tar.gz
# Source0-md5:	4ece2f43b140fab6a2c3a9d6436d7779
Patch0:		%{name}-opt.patch
Patch1:		%{name}-make.patch
URL:		http://www.wagner.pp.ru/~vitus/software/catdoc/
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
%patch -P0 -p1
%patch -P1 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure \
	--with-wish=/usr/bin/wish

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	installroot=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_bindir}/catdoc
%attr(755,root,root) %{_bindir}/catppt
%attr(755,root,root) %{_bindir}/wordview
%attr(755,root,root) %{_bindir}/xls2csv
%{_datadir}/catdoc
%{_mandir}/man1/catdoc.1*
%{_mandir}/man1/catppt.1*
%{_mandir}/man1/wordview.1*
%{_mandir}/man1/xls2csv.1*
