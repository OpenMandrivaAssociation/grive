# Looks like upstream switched to static build for 0.2.0
# Keep subpackages in spec in case upstream starts to provide them again
%define build_shared 0

%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}

Summary:	An Open Source Linux Client for Google Drive
Name:		grive
Version:	0.3.0
Release:	6
License:	GPLv2+
Group:		Networking/File transfer
Url:		https://github.com/Grive/
# Repack from git
Source0:	%{name}-%{version}.tar.xz
Source100:	grive.rpmlintrc
Patch0:		grive-0.2.0-bfd.patch
Patch1:		grive-0.3.0-doc.patch
Patch2:		grive-0.3.0-compile.patch
BuildRequires:	cmake
BuildRequires:	binutils-devel
BuildRequires:	boost-devel
BuildRequires:  qt4-devel
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
sed -i 's|json/json.h|json-c/json.h|g' cmake/Modules/FindJSONC.cmake
sed -i 's|json|json-c json|g' cmake/Modules/FindJSONC.cmake
sed -i 's|json/json_tokener.h|json-c/json_tokener.h|g' libgrive/src/protocol/Json.cc
sed -i 's|json/linkhash.h|json-c/linkhash.h|g' libgrive/src/protocol/Json.cc

%build
export LDFLAGS="$LDFLAGS -ljson-c"
%cmake
%make

%install
%makeinstall_std -C build

%files
%doc COPYING README
%{_bindir}/bgrive
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%if %{build_shared}
%files -n %{libname}
%{_libdir}/libgrive.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/libgrive.so
%endif

