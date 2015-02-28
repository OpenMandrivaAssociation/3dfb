Summary: 3d File Manager
Name:    3dfb
Version: 0.6.1
Release: 5
Source0: http://freefr.dl.sourceforge.net/sourceforge/dz3d/%{name}-%{version}.tar.gz
Patch0: 3dfb-0.6.1-gcc41.patch
License: GPL
Group: File tools
Url: https://sourceforge.net/projects/dz3d/
BuildRequires: pkgconfig(glut)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(glu)

%description
3dFB is a 3d File Manager. 2d file managers work nicely, but with 3d you
can display much more information. The aim of this project is to make a
viable, workable, 3d file manager that is not a hog on resources and can
actually be usable.

%prep
%setup -q
%patch0 -p1

%build
export LDFLAGS="%{ldflags} -lGLU -lglut"

%configure2_5x
%make

%install
%makeinstall_std


%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS PROGRAMMER.README README WISHLIST
%{_bindir}/%name


