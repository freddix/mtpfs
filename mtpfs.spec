Summary:	FUSE filesystem for MTP devices
Name:		mtpfs
Version:	1.1
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://www.adebenham.com/files/mtp/%{name}-%{version}.tar.gz
# Source0-md5:	a299cadca336e6945b7275b44c6e8d27
BuildRequires:	fuse-devel
BuildRequires:	glib-devel
BuildRequires:	libmtp-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MTPfs is a FUSE filesystem that supports reading and writing from any
MTP device (as supported by libmtp).

%prep
%setup -q

%build
%configure \
	--disable-mad
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mtpfs

