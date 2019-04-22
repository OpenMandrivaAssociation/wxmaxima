%define Name	wxMaxima

Name:		      wxmaxima
Version:	      19.04.3
Release:	      1
Summary:	      An interface for the computer algebra system Maxima
Group:		      Sciences/Mathematics
License:	      GPLv2+
URL:		      https://wxmaxima-developers.github.io/wxmaxima/index.html
Source:		      https://github.com/wxMaxima-developers/wxmaxima/archive/Version-%{version}/%{name}-%{version}.tar.gz
Requires:	      maxima
BuildRequires:	      pkgconfig(libxml-2.0)
BuildRequires:	      wxgtku3.0-devel
BuildRequires:	      imagemagick
BuildRequires:	      desktop-file-utils

Suggests:	jsmath-fonts

%description
wxMaxima is a cross-platform graphical front-end for the computer
algebra system Maxima based on wxWidgets. It provides nice display
of mathematical output and easy access to Maxima functions through
menus and dialogs.

%files -f %{Name}.lang
%doc README COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{Name}.desktop
%{_datadir}/%{Name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*
%{_mandir}/man1/%{name}.1.*
%{_datadir}/info/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/bash-completion/completions/%{name}

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-Version-%{version}

%build
%configure \
	--enable-printing \
        --enable-unicode-glyphs
%make_build

%install
%make_install

# locales
%find_lang %{Name}

# icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert data/wxmaxima.png -scale 48x48 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert data/wxmaxima.png -scale 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert data/wxmaxima.png -scale 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

# .desktop
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
