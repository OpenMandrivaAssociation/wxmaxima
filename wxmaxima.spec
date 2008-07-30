%define name	wxmaxima
%define version 0.7.4
%define release %mkrel 3
%define Name	wxMaxima

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	An interface for the computer algebra system Maxima
Group:		Sciences/Mathematics
License:	GPLv2+
URL:		http://wxmaxima.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{name}/%{Name}-%{version}.tar.gz
Requires:	maxima
Buildrequires:	libxml2-devel
Buildrequires:	wxgtku-devel
Buildrequires:	ImageMagick
Buildrequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
wxMaxima is a cross-platform graphical front-end for the computer
algebra system Maxima based on wxWidgets. It provides nice display
of mathematical output and easy access to Maxima functions through
menus and dialogs.

%prep 
%setup -q -n %{Name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall
%find_lang %{Name}
# icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert wxmaxima.png -scale 48x48 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert wxmaxima.png -scale 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert wxmaxima.png -scale 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

#xdg
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

# correct icon name in menu entry
perl -pi -e 's,maxima.png,%{name},g' %{buildroot}%{_datadir}/applications/*

desktop-file-install --vendor="" \
    --remove-category="Application" \
    --remove-category="Utility" \
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

