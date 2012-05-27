%define gitver	07553e5
%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}

Summary:	An Open Source Linux Client for Google Drive
Name:		grive
Version:	0.0.4
Release:	%{gitver}.1
License:	GPLv2+
Group:		Networking/File transfer
URL:		http://match065.github.com/grive/
Source0:	match065-%{name}-%{gitver}.tar.gz

BuildRequires:	cmake
BuildRequires:	binutils-devel
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(json)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(openssl)

%description
The purpose of this project is to provide an independent implementation of 
Google Drive client. It uses the Google Document List API to talk to the 
servers in Google. The code is written in standard C++.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Libraries and include files for developing with %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package provides the necessary development library and include
files to allow you to develop with %{name}.


%prep
%setup -qn match065-%{name}-%{gitver}

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%doc COPYING README
%{_bindir}/%{name}

%files -n %{libname}
%{_libdir}/libgrive.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/libgrive.so

