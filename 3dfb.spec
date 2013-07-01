%define name 3dfb
%define version 0.6.1
%define release 2

Summary: 3d File Manager
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://freefr.dl.sourceforge.net/sourceforge/dz3d/%{name}-%{version}.tar.gz
Patch0: 3dfb-0.6.1-gcc41.patch
License: GPL
Group: File tools
Url: https://sourceforge.net/projects/dz3d/
BuildRequires: pkgconfig(glut)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(xmu)

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
%makeinstall_std


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS PROGRAMMER.README README WISHLIST
%{_bindir}/%name



%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.6.1-2mdv2011.0
+ Revision: 664787
- rebuild

* Thu Jun 04 2009 Funda Wang <fwang@mandriva.org> 0.6.1-1mdv2011.0
+ Revision: 382611
- New version 0.6.1

* Wed Jan 02 2008 Thierry Vignaud <tv@mandriva.org> 0.5.6-3mdv2008.1
+ Revision: 140917
- fix mesa BR
- import 3dfb


* Mon Oct 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.5.6-3mdk
- remove dot ended
- mkrel 

* Mon Jul 12 2004 Olivier Blin <blino@mandrake.org> 0.5.6-2mdk
- fix BuildRequires, remove redundant requires

* Sun Jul 11 2004 Franck Villaume <fvill@freesurf.fr> 0.5.6-1mdk
- 0.5.6
- fix buildrequires
 
* Wed Jun 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.5.5-2mdk
- Rebuild

* Thu May 27 2004 Antoine Ginies <aginies@n2.mandrakesoft.com> 0.5.5-1mdk
- release 0.5.5
