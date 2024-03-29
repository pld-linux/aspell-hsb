Summary:	Upper Sorbian dictionary for aspell
Summary(pl.UTF-8):	Słownik górnołużycki dla aspella
Name:		aspell-hsb
Version:	0.02
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/hsb/aspell6-hsb-%{version}-%{subv}.tar.bz2
# Source0-md5:	f018c68a688600aeb9cb53747021703a
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
BuildRequires:	which
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Upper Sorbian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik górnołużycki (lista słów) dla aspella.

%prep
%setup -q -n aspell6-hsb-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/hsb.*
%{_datadir}/aspell/hsb.dat
%{_datadir}/aspell/hsb_affix.dat
