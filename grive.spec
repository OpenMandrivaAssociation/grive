# Looks like upstream switched to static build for 0.2.0
# Keep subpackages in spec in case upstream starts to provide them again
%define build_shared 0

%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}

Summary:	An Open Source Linux Client for Google Drive
Name:		grive2
Version:	0.5.0
Release:	1
License:	GPLv2+
Group:		Networking/File transfer
Url:		https://github.com/vitalif/grive2/
# Repack from git
Source0:	https://github.com/vitalif/grive2/archive/v0.5.0/grive2-0.5.0.tar.gz
Source100:	grive.rpmlintrc
#Patch0:		grive-0.2.0-bfd.patch
#Patch1:		grive-0.3.0-doc.patch
#Patch2:		grive-0.3.0-compile.patch
BuildRequires:	cmake
BuildRequires:	binutils-devel
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(yajl)
%if ! %{build_shared}
Obsoletes:	%{libname} < %{version}-%{release}
Obsoletes:	%{devname} < %{version}-%{release}
%endif

%description
The purpose of this project is to provide an independent implementation of
Google Drive client. It uses the Google Document List API to talk to the
servers in Google. The code is written in standard C++.

%if %{build_shared}
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
%endif

%prep
%setup -q
%apply_patches


%build

%cmake
%make

%install
%makeinstall_std -C build

%files
%doc COPYING
#{_bindir}/bgrive
#{_bindir}/%{name}
#{_mandir}/man1/%{name}.1*

%if %{build_shared}
%files -n %{libname}
%{_libdir}/libgrive.so.%{major}*

%files -n %{devname}
#dir %{_includedir}/%{name}
#{_includedir}/%{name}/*
#{_libdir}/libgrive.so
%endif

