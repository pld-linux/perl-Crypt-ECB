%define		pdir	Crypt
%define		pnam	ECB
%include	/usr/lib/rpm/macros.perl
Summary:	Crypt::ECB Perl module - implementation of the ECB mode
Summary(pl.UTF-8):	Moduł Perla Crypt::ECB - implementacja trybu ECB
Name:		perl-Crypt-ECB
Version:	1.1
Release:	4
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}-2.tar.gz
# Source0-md5:	8c15a093e500abdd3ac24ca199fae7b9
URL:		http://search.cpan.org/dist/Crypt-ECB/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a Perl-only implementation of the ECB mode. In
combination with a block cipher such as DES, IDEA or Blowfish, you can
encrypt and decrypt messages of arbitrarily long length. Though for
security reasons other modes than ECB such as CBC should be preferred.
See textbooks on cryptography if you want to know why.

%description -l pl.UTF-8
Ten moduł jest czysto perlową implementacją trybu ECB. W połączeniu z
szyfrem blokowym, takim jak DES, IDEA lub Blowfish, można kodować i
rozkodowywać wiadomości o dowolnej długości. Jednak ze względów
bezpieczeństwa lepiej używać innych trybów niż ECB, na przykład CBC.
Odpowiedź dlaczego znajduje się w książkach z dziedziny kryptografii.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Crypt/ECB.pm
%{_mandir}/man3/*
