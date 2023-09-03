Name:       ell
Summary:    Embedded Linux library
Version:    0.58
Release:    1
License:    GPLv2
URL:        https://git.kernel.org/pub/scm/libs/ell/ell.git
Source:     %{name}-%{version}.tar.bz2

BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf

%description
%{summary}

%package devel
Summary:    Headers for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
Development headers and libraries for %{name}

%prep
%setup -q -n %{name}-%{version}/upstream
./bootstrap

%build

%configure --prefix=/usr

make %{_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libell.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/ell/
%{_libdir}/pkgconfig/ell.pc
%{_libdir}/libell.so
