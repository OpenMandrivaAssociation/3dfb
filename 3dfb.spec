%define name 3dfb
%define version 0.6.1
%define release %mkrel 2

Summary: 3dFB is a 3d File Manager
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://freefr.dl.sourceforge.net/sourceforge/dz3d/%{name}-%{version}.tar.gz
Patch0: 3dfb-0.6.1-gcc41.patch
License: GPL
Group: File tools
Url: https://sourceforge.net/projects/dz3d/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mesaglut-devel, glib2-devel

%description
3dFB is a 3d File Manager. 2d file managers work nicely, but with 3d you
can display much more information. The aim of this project is to make a
viable, workable, 3d file manager that is not a hog on resources and can
actually be usable.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS PROGRAMMER.README README WISHLIST
%{_bindir}/%name

