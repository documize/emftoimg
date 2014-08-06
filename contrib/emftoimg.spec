%define __prefix /usr/local
%global debug_package %{nil}

Summary:    emfotimg
Name:       emftoimg
Version:    %{version}
Release:    1%{?dist}
License:    MIT
Group:      Applications/System
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: golang = 1.2.2

%description
EMF images converter

%prep
%setup -T -D -n %{name}-%{version}

%build
go build -o %{name}

%install
install -p -D -m 755 %{_builddir}/%{name}-%{version}/%{name} \
    %{buildroot}%{__prefix}/bin/%{name}

%clean
rm -rf %{buildroot}

%files
%attr(755,root,root) %{__prefix}/bin/%{name}