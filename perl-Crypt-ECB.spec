%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	ECB
Summary:	Crypt::ECB Perl module - implementation of the ECB mode
Summary(pl):	Modu� Perla Crypt::ECB - implementacja trybu ECB
Name:		perl-Crypt-ECB
Version:	1.1
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}-2.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a Perl-only implementation of the ECB mode. In
combination with a block cipher such as DES, IDEA or Blowfish, you can
encrypt and decrypt messages of arbitrarily long length. Though for
security reasons other modes than ECB such as CBC should be preferred.
See textbooks on cryptography if you want to know why.

%description -l pl
Ten modu� jest czysto perlow� implementacj� trybu ECB. W po��czeniu z
szyfrem blokowym, takim jak DES, IDEA lub Blowfish, mo�na kodowa� i
rozkodowywa� wiadomo�ci o dowolnej d�ugo�ci. Jednak ze wzgl�d�w
bezpiecze�stwa lepiej u�ywa� innych tryb�w ni� ECB, na przyk�ad CBC.
Odpowied� dlaczego znajduje si� w ksi��kach z dziedziny kryptografii.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
%{perl_sitelib}/Crypt/ECB.pm
%{_mandir}/man3/*
