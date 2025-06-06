%global wxver 3.2

Name:		wxmaxima
Version:	25.04.0
Release:	1
Summary:	An interface for the computer algebra system Maxima
Group:		Sciences/Mathematics
License:	GPLv2+
URL:		https://wxmaxima-developers.github.io/wxmaxima/
Source0:	https://github.com/wxMaxima-developers/wxmaxima/archive/Version-%{version}/%{name}-Version-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	gettext
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	wxgtku%{wxver}-devel

Requires:	maxima
Requires:	jsmath-fonts

%description
wxMaxima is a cross-platform graphical front-end for the computer
algebra system Maxima based on wxWidgets. It provides nice display
of mathematical output and easy access to Maxima functions through
menus and dialogs.

%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/doc/%{name}/*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/wxMaxima
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/*wxMaxima.png
%{_iconsdir}/hicolor/*/apps/*wxMaxima.svg
%{_metainfodir}/*.appdata.xml
%{_mandir}/man1/%{name}.1.*
%{_mandir}/de/man1/%{name}.1.*

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-Version-%{version}

%build
%cmake \
	-DWXM_INTERPROCEDURAL_OPTIMIZATION:BOOL=ON \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

# icons
for d in 16 32 48 64 72 128 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps
	convert data/io.github.wxmaxima_developers.wxMaxima.svg -scale ${d}x${d} %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done

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

# locales
%find_lang %{name} --all-name

