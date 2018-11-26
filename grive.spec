%global optflags %{optflags} -Wno-c++11-narrowing
%define major	0
%define libname	%mklibname %{name} %{major}

Summary:	An Open Source Linux Client for Google Drive
Name:		grive2
Version:	0.5.0
Release:	1
License:	GPLv2+
Group:		Networking/File transfer
Url:		https://github.com/vitalif/grive2/
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

%description
The purpose of this project is to provide an independent implementation of
Google Drive client. It uses the Google Document List API to talk to the
servers in Google. The code is written in standard C++.

%prep
%setup -q
%apply_patches


%build

%cmake
%make

%install
%makeinstall_std -C build

%files
%doc COPYING README.md
%{_bindir}/grive
%{_mandir}/man1/*





