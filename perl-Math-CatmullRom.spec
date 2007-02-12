#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	CatmullRom
Summary:	Math::CatmullRom - calculate Catmull-Rom splines
Summary(pl.UTF-8):   Math::CatmullRom - obliczanie splajnów Catmulla-Roma
Name:		perl-Math-CatmullRom
Version:	0.00
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c924e04872eed511e9b6f7c43af2af45
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an algorithm to generate plots for Catmull-Rom
splines.

A Catmull-Rom spline can be considered a special type of Bezier curve
that guarantees that the curve will cross every control point starting
at the second point and terminating at the penultimate one. For this
reason the minimum number of control points is 4.

%description -l pl.UTF-8
Ten moduł udostępnia algorytm do generowania wykresów splajnów
Catmulla-Roma.

Splajn Catmulla-Roma można uznać za specjalny typ krzywej Beziera,
gwarantujący, że krzywa przetnie wszystkie punkty kontrolne poczynając
od drugiego a kończąc na przedostatnim. Dlatego minimalna liczba
punktów kontrolnych to 4.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/CatmullRom.pm
%{_mandir}/man3/*
