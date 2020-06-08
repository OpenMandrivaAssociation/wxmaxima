%define Name	wxMaxima

Name:		wxmaxima
Version:	20.06.6
Release:	1
Summary:	An interface for the computer algebra system Maxima
Group:		Sciences/Mathematics
License:	GPLv2+
URL:		https://wxmaxima-developers.github.io/wxmaxima/index.html
Source:		https://github.com/wxMaxima-developers/wxmaxima/archive/Version-%{version}/%{name}-Version-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	gettext
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	wxgtku3.0-devel

Requires:	maxima
Requires:	jsmath-fonts

%description
wxMaxima is a cross-platform graphical front-end for the computer
algebra system Maxima based on wxWidgets. It provides nice display
of mathematical output and easy access to Maxima functions through
menus and dialogs.

%files -f %{name}.lang
%doc README COPYING
%{_bindir}/%{name}
%{_datadir}/%{Name}
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*
%{_datadir}/applications/%{name}.desktop
%%{_metainfodir}/%{name}.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{bash_completionsdir}/%{name}
%{_mandir}/man1/%{name}.1.*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-Version-%{version}
%autopatch -p1

%build
%cmake
%make_build

%install
%make_install -C build

# icons
for d in 16 32 48
do
	install -dm 0755  %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps
	convert Doxygen/wxmaxima.png -scale ${d}x${d} %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
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

# fix name
mv %{buildroot}%{_datadir}/applications/io.github.wxmaxima_developers.wxMaxima.desktop \
	%{buildroot}%{_datadir}/applications/%{name}.desktop
mv %{buildroot}%{_metainfodir}/io.github.wxmaxima_developers.wxMaxima.appdata.xml \
	%{buildroot}%{_metainfodir}/%{name}.appdata.xml

# locales
%find_lang %{name} --all-name
