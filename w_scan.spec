%define name w_scan
%define date 20091230
%define distname %{name}-%{date}
%define version 0
%define rel 1
%define release %mkrel 0.%{date}.%{rel}

Summary: Channel scan tool for DVB-T and DVB-C
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.bz2
License: GPLv2+
Group: Video
Url: http://edafe.org/vdr/w_scan/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
w_scan is an application that greatly simplifies the task of scanning
for DVB-T, DVB-C and ATSC channel information. Winfried Kvhler\u2019s
w_scan is special because it does not require any region-specific
initial transponder data for operation. It will create configuration
files for VDR, Kaffeine and Xine.

%prep
%setup -q -n %{distname}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}
%{_bindir}/w_scan_start.sh
%{_mandir}/man1/w_scan.1*

