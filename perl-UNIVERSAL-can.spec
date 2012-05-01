Name:           perl-UNIVERSAL-can
Version:        1.15
Release:        1%{?dist}
Summary:        Hack around people calling UNIVERSAL::can() as a function

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/UNIVERSAL-can/
Source0:        http://www.cpan.org/authors/id/C/CH/CHROMATIC/UNIVERSAL-can-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Simple) >= 0.60
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The UNIVERSAL class provides a few default methods so that all objects
can use them. Object orientation allows programmers to override these
methods in subclasses to provide more specific and appropriate behavior.

Some authors call methods in the UNIVERSAL class on potential invocants
as functions, bypassing any possible overriding. This is wrong and you
should not do it. Unfortunately, not everyone heeds this warning and
their bad code can break your good code.


%prep
%setup -q -n UNIVERSAL-can-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
chmod -R u+w $RPM_BUILD_ROOT/*


%check
PERL_RUN_ALL_TESTS=1 ./Build test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/UNIVERSAL/
%{_mandir}/man3/*.3*


%changelog
* Wed Oct  7 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.15-1
- update to new upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.12-2
- rebuild for new perl

* Wed Apr  5 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.12-1
- Update to 1.12.

* Fri Feb 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.11-1
- Update to 1.11.
- No longer build requires perl(Test::Exception).

* Thu Feb  9 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.03-2
- Missing build requirement: perl(Test::Exception).

* Wed Feb  8 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.03-1
- Update to 1.03.

* Tue Dec 27 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.01-1
- First build.
