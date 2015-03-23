Name: hello
Version: 1.0
Release: 1%{?dist}
Summary: A sample package, saying hello, world
License: GPL
Prefix: /usr
Source0: hello-1.0.tar.gz
BuildRoot: %{_tmppath}/hello-root

%description
This package basically does nothing, but it potentially could do something useful.

%prep
%setup -q -n %{name}-%{version}

%build
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/ {bin,lib}
make install


%make_install


%files
%defattr(-,root,root)
/usr/local/lib


%clean
rm -rf $RPM_BUILD_ROOT

