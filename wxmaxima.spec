%define name	wxmaxima
%define version 0.7.1
%define release %mkrel 1
%define Name	wxMaxima

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    An interface for the computer algebra system Maxima
Group:		    Sciences/Mathematics
License:	    GPL
Url:		    http://wxmaxima.sourceforge.net/
Source:		    http://prdownloads.sourceforge.net/%{name}/%{Name}-%{version}.tar.bz2
Requires:	    maxima
Buildrequires:	libxml2-devel
Buildrequires:	wxgtku-devel
Buildrequires:	ImageMagick
Buildrequires:	desktop-file-utils
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
wxMaxima is a cross-platform graphical front-end for the computer
algebra system Maxima based on wxWidgets. It provides nice display
of mathematical output and easy access to Maxima functions through
menus and dialogs.wxMaxima is a wxWidgets GUI for the computer algebra system
Maxima

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
mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert maxima-new.png -geometry 48x48 %{buildroot}%{_liconsdir}/%{name}.png
convert maxima-new.png -geometry 32x32 %{buildroot}%{_iconsdir}/%{name}.png
convert maxima-new.png -geometry 16x16 %{buildroot}%{_miconsdir}/%{name}.png

# menu migration style
mkdir -p %{buildroot}%{_menudir}
cat > %{buildroot}%{_menudir}/%{name} <<EOF
?package(%{name}): needs="X11" \
    section="Sciences/Mathematics" \
    title="wxMaxima" \
    longtitle="An interface for the computer algebra system Maxima" \
    command="%{_bindir}/%{name}" \
    icon="%{name}.png" \
    xdg="true"
EOF

#xdg
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
    --remove-category="Application" \
    --add-category="GTK" \
    --add-category="X-MandrivaLinux-MoreApplications-Sciences-Mathematics" \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/*

%post 
%{update_menus}

%postun 
%{clean_menus}

%clean
rm -rf %{buildroot}

%files -f %{Name}.lang
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_menudir}/%{name}
%{_datadir}/%{Name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


