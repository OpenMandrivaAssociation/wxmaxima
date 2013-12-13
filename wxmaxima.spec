%define Name	wxMaxima

Name:		      wxmaxima
Version:	      13.04.2
Release:	      1
Summary:	      An interface for the computer algebra system Maxima
Group:		      Sciences/Mathematics
License:	      GPLv2+
URL:		      http://wxmaxima.sourceforge.net/
Source:		      http://prdownloads.sourceforge.net/%{name}/%{Name}-%{version}.tar.gz
Requires:	      maxima
BuildRequires:	      pkgconfig(libxml-2.0)
BuildRequires:	      wxgtku-devel
BuildRequires:	      imagemagick
BuildRequires:	      desktop-file-utils

Suggests:	jsmath-fonts

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

%files -f %{Name}.lang
%doc README COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{Name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png


