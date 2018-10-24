%define upstream_name    B-Utils
%define upstream_version 0.27
Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Easily build XS extensions that depend on XS extensions

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/B/%{upstream_name}-%{upstream_version}.tar.gz
Source100:  %{name}.rpmlintrc

BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::MakeMaker) >= 7.40.0
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Test::More) >= 1.1.9
BuildRequires: perl(Exporter)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl-devel

%description
  sub foo {
    dothis(1);
    find_things();
    return;
  }

has the following optree:

 d  <1> leavesub[1 ref] K/REFC,1 ->(end)
 -     <@> lineseq KP ->d
 1        <;> nextstate(main -371 bah.pl:8) v/2 ->2
 5        <1> entersub[t2] vKS/TARG,3 ->6
 -           <1> ex-list K ->5
 2              <0> pushmark s ->3
 3              <$> const[IV 1] sM ->4
 -              <1> ex-rv2cv sK/3 ->-
 4                 <#> gv[*dothis] s ->5
 6        <;> nextstate(main -371 bah.pl:9) v/2 ->7

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%clean

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*



