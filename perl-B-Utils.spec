
%define realname   B-Utils
%define version    0.07
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Easily build XS extensions that depend on XS extensions
Source:     http://www.cpan.org/modules/by-module/B/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


