%define upstream_name    Catalyst-Model-KiokuDB
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Use KiokuDB in your Catalyst apps
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Catalyst)
BuildRequires: perl(Catalyst::Plugin::Authentication)
BuildRequires: perl(Hash::Util::FieldHash::Compat)
BuildRequires: perl(KiokuX::Model)
BuildRequires: perl(KiokuX::User)
BuildRequires: perl(Moose)
BuildRequires: perl(Scope::Guard)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Perl extension to use KiokuDB in your Catalyst apps.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


