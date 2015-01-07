%define date 20130331

Summary:	Channel scan tool for DVB-T and DVB-C
Name:		w_scan
Version:	0
Release:	0.%{date}.2
Source0:	%{name}-%{date}.tar.bz2
License:	GPLv2+
Group:	Video
Url:	http://edafe.org/vdr/w_scan/
BuildRequires:	kernel-headers
BuildRequires:	glibc-devel

%description
w_scan is an application that greatly simplifies the task of scanning
for DVB-T, DVB-C and ATSC channel information. Winfried Kvhler\u2019s
w_scan is special because it does not require any region-specific
initial transponder data for operation. It will create configuration
files for VDR, Kaffeine and Xine.

%prep
%setup -q -n  %{name}-%{date}
# -n %{distname}

%build
export CC=gcc
export CXX=g++

%configure
%make

%install
%makeinstall_std

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/w_scan.1*
