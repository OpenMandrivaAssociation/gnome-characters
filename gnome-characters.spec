%global appname org.gnome.Characters
%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-characters
Version:	3.30.0
Release:	1
Summary:	Character map application for GNOME
# Files from gtk-js-app are licensed under 3-clause BSD.
# Other files are GPL 2.0 or later.
License:	BSD and GPLv2+
URL:		https://wiki.gnome.org/Design/Apps/CharacterMap
Group:		Graphical desktop/GNOME
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

# This package uses GtkWidget template, which was added in Gjs 1.43.3.
BuildRequires:	pkgconfig(gjs-1.0) >= 1.43.3
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	gobject-introspection-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libunistring-devel
BuildRequires:	meson
Requires:	gjs >= 1.43.3

# This package contains libunistring modules from Gnulib.  If a recent
# enough version of libunistring is installed on the system, it will
# be used instead.  However, as of today, the libunistring package in
# F22 is older and we try to avoid unnecessary dependency.

# BuildRequires:	   libunistring-devel
Provides:	bundled(gnulib)

%description
Characters is a simple utility application to find and insert unusual
characters.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
find $RPM_BUILD_ROOT -name '*.la' -delete

desktop-file-install --dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{appname}


%files -f %{appname}.lang
%doc NEWS
%license COPYING COPYINGv2
%{_bindir}/%{name}
%{_datadir}/dbus-1/services/%{appname}.BackgroundService.service
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}-symbolic.svg
%{_datadir}/icons/hicolor/symbolic/apps/gnome-characters-symbolic.svg
%{_datadir}/%{appname}
%{_datadir}/gnome-shell/search-providers/%{appname}.search-provider.ini
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_libdir}/%{appname}
