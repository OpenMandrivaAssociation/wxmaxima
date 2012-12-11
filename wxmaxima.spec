%define name	wxmaxima
%define version 12.04.0
%define release %mkrel 1
%define Name	wxMaxima

Name:		      %{name}
Version:	      %{version}
Release:	      %{release}
Summary:	      An interface for the computer algebra system Maxima
Group:		      Sciences/Mathematics
License:	      GPLv2+
URL:		      http://wxmaxima.sourceforge.net/
Source:		      http://prdownloads.sourceforge.net/%{name}/%{Name}-%{version}.tar.gz
Requires:	      maxima
BuildRequires:	      libxml2-devel
BuildRequires:	      wxgtku-devel
BuildRequires:	      imagemagick
BuildRequires:	      desktop-file-utils
BuildRoot:	      %{_tmppath}/%{name}-%{version}

%if %mdkver > 201010
Suggests:	jsmath-fonts
%endif

%description
wxMaxima is a cross-platform graphical front-end for the computer
algebra system Maxima based on wxWidgets. It provides nice display
of mathematical output and easy access to Maxima functions through
menus and dialogs.

%prep 
%setup -q -n %{Name}-%{version}

%build
%configure2_5x \
	--enable-printing \
        --enable-unicode-glyphs
%make

%install
rm -rf %{buildroot}

%makeinstall
%find_lang %{Name}
# icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert data/wxmaxima.png -scale 48x48 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert data/wxmaxima.png -scale 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert data/wxmaxima.png -scale 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

#xdg
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -D -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 644 data/wxmaxima.png %{buildroot}%{_datadir}/pixmaps/wxmaxima.png

# correct icon name in menu entry
#perl -pi -e 's,maxima.png,%{name},g' %{buildroot}%{_datadir}/applications/*

desktop-file-install --vendor="" \
    --remove-category="Application" \
    --remove-category="Utility" \
    --remove-category="X-Red-Hat-Base" \
    --remove-category="X-Red-Hat-Base-Only" \
    --add-category="GTK" \
    --add-category="Science" \
    --add-category="Math" \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/*

%if %mdkversion < 200900
%post 
%{update_menus}
%{update_icon_cache hicolor}
%endif

%if %mdkversion < 200900
%postun 
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%clean
rm -rf %{buildroot}

%files -f %{Name}.lang
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{Name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png


%changelog
* Tue May 01 2012 Cristobal Lopez Silla <tobal@mandriva.org> 12.04.0-1mdv2012.0
+ Revision: 794849
- update to new version and rewrite spec

* Mon Oct 03 2011 Александр Казанцев <kazancas@mandriva.org> 11.08.0-1
+ Revision: 702560
- new version 11.08
- add full ru translate and desktop with translated part

* Fri Jul 15 2011 Paulo Andrade <pcpa@mandriva.com.br> 11.04.0-1
+ Revision: 690071
- Update to latest upstream release

* Tue Nov 23 2010 Jani Välimaa <wally@mandriva.org> 0.8.6-2mdv2011.0
+ Revision: 599936
- suggest jsmath-fonts for better Greek characters and math symbols output

* Sat Nov 20 2010 Jani Välimaa <wally@mandriva.org> 0.8.6-1mdv2011.0
+ Revision: 599211
- new version 0.8.6

* Mon Nov 15 2010 Jani Välimaa <wally@mandriva.org> 0.8.5-2mdv2011.0
+ Revision: 597646
- fix desktop file (wrong icon name)

* Thu Apr 29 2010 Frederik Himpe <fhimpe@mandriva.org> 0.8.5-1mdv2010.1
+ Revision: 541061
- update to new version 0.8.5

* Wed Dec 16 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.4-1mdv2010.1
+ Revision: 479582
- update to new version 0.8.4

* Sat Aug 29 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.3a-1mdv2010.1
+ Revision: 422257
- Update to new version 0.8.3a
- Remove some Red Hat categories from desktop file

* Thu Jun 04 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.2-1mdv2010.0
+ Revision: 382898
- update to new version 0.8.2

* Fri Feb 06 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.1-1mdv2009.1
+ Revision: 338277
- update to new version 0.8.1

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sat Dec 06 2008 Frederik Himpe <fhimpe@mandriva.org> 0.8.0-1mdv2009.1
+ Revision: 311179
- Update to new version 0.8.0

* Thu Aug 21 2008 Frederik Himpe <fhimpe@mandriva.org> 0.7.6-1mdv2009.0
+ Revision: 274694
- update to new version 0.7.6

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.7.4-4mdv2009.0
+ Revision: 262183
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.7.4-3mdv2009.0
+ Revision: 256477
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.4-1mdv2008.1
+ Revision: 160925
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 05 2007 Adam Williamson <awilliamson@mandriva.org> 0.7.3-2mdv2008.0
+ Revision: 80506
- reduce menu categories as per frederik

* Tue Sep 04 2007 Adam Williamson <awilliamson@mandriva.org> 0.7.3-1mdv2008.0
+ Revision: 79569
- need to do the icon name correction before the desktop-file-install to pass build tests...
- fix various category issues in xdg menu entry (#33119)
- drop old menu entry
- fd.o icons
- fix cut-n-paste-o in description
- use Fedora license policy
- small spec clean
- new release 0.7.3

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.1-1mdv2008.0
+ Revision: 47275
- update to new version 0.7.1


* Wed Dec 20 2006 Götz Waschk <waschk@mandriva.org> 0.6.5-3mdv2007.0
+ Revision: 100707
- Import wxmaxima

* Wed Dec 20 2006 Götz Waschk <waschk@mandriva.org> 0.6.5-3mdv2007.1
- use the right configure macro

* Fri Sep 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.5-2mdv2007.0
- buildrequires desktop-file-utils

* Wed Jun 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.5-1mdv2007.0
- contributed by PierreLag <pierre DOT lag AT gmail.com>

