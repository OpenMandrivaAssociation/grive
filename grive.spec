%global optflags %{optflags} -Wno-c++11-narrowing
%define major	0
%define libname	%mklibname %{name} %{major}

Summary:	An Open Source Linux Client for Google Drive
Name:		grive2
Version:	0.5.3
Release:	1
License:	GPLv2+
Group:		Networking/File transfer
Url:		https://github.com/vitalif/grive2/
Source0:	https://github.com/vitalif/grive2/archive/v%{version}/grive2-%{version}.tar.gz
Source100:	grive.rpmlintrc

BuildRequires:	cmake
BuildRequires:	binutils-devel
BuildRequires:	boost-devel
BuildRequires:  pkgconfig(icu-uc)
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
%autopatch -p1

%build

%cmake
%make_build

%install
%make_install -C build

%files
%doc COPYING README.md
%{_bindir}/grive
%{_mandir}/man1/*
%{_prefix}/lib/grive/grive-sync.sh
%{_prefix}/lib/systemd/user/grive-changes@.service
%{_prefix}/lib/systemd/user/grive-timer@.service
%{_prefix}/lib/systemd/user/grive-timer@.timer
