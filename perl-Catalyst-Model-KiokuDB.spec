%define upstream_name    Catalyst-Model-KiokuDB
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Use KiokuDB in your Catalyst apps
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Catalyst::Plugin::Authentication)
BuildRequires:	perl(Hash::Util::FieldHash::Compat)
BuildRequires:	perl(KiokuX::Model)
BuildRequires:	perl(KiokuX::User)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Scope::Guard)
BuildRequires:	perl(Throwable)
BuildArch:	noarch

%description
Perl extension to use KiokuDB in your Catalyst apps.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.120.0-3mdv2011.0
+ Revision: 654253
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.120.0-2mdv2011.0
+ Revision: 624895
- Add description and summary
- import perl-Catalyst-Model-KiokuDB

