%define upstream_name    B-Utils
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:    Easily build XS extensions that depend on XS extensions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/B/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.150.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.150.0-1
+ Revision: 659886
- update to new version 0.15

* Wed Mar 23 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1
+ Revision: 648057
- update to new version 0.14

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.130.0-2
+ Revision: 640763
- rebuild to obsolete old packages

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.130.0-1
+ Revision: 635492
- update to new version 0.13

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.120.0-1
+ Revision: 634206
- update to new version 0.12

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 555223
- rebuild

* Wed Jan 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.1
+ Revision: 490485
- update to 0.11

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.1
+ Revision: 474728
- update to 0.09

* Wed Sep 02 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 424342
- adding missing buildrequires:
- update to 0.08

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 401786
- rebuild using %%perl_convert_version
- fixed license field

* Wed Dec 03 2008 Jérôme Quelin <jquelin@mandriva.org> 0.07-1mdv2009.1
+ Revision: 309776
- import perl-B-Utils


* Wed Dec 03 2008 cpan2dist 0.07-1mdv
- initial mdv release, generated with cpan2dist

