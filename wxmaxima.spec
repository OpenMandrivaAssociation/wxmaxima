%define name	wxmaxima
%define version 11.08.0
%define release %mkrel 1
%define Name	wxMaxima

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	An interface for the computer algebra system Maxima
Group:		Sciences/Mathematics
License:	GPLv2+
URL:		http://wxmaxima.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{name}/%{Name}-%{version}.tar.gz
Source1: %Name.desktop
Source2: wxmaxima-ru.po.bz2
Requires:	maxima
Buildrequires:	libxml2-devel
Buildrequires:	wxgtku-devel
Buildrequires:	imagemagick
Buildrequires:	desktop-file-utils

%if %mdkver > 201010
Suggests:	jsmath-fonts
%endif

BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
wxMaxima is a cross-platform graphical front-end for the computer
algebra system Maxima based on wxWidgets. It provides nice display
of mathematical output and easy access to Maxima functions through
menus and dialogs.

%prep 
%setup -q -n %{Name}-%{version}

bzcat %SOURCE2 >locales/ru.po

#build new ru locale
msgfmt locales/ru.po -o locales/ru.mo

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
#perl -pi -e 's,wxmaxima.png,%{name},g' %{buildroot}%{_datadir}/applications/*

# menu 
install -D -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

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

