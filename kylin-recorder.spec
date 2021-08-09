%define debug_package %{nil}
Name:           kylin-recorder
Version:        1.2.23
Release:        1
Summary:        kylin-recorder
License:        GPL-3.0 License
URL:            https://github.com/UbuntuKylin/kylin-recorder
Source0:        %{name}-%{version}.tar.gz
patch0:         0001-modify-kylin-recorder-running-errors.patch

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: zlib-devel
BuildRequires: libX11-devel
BuildRequires: libcrystalhd-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: libXext-devel
BuildRequires: lame-devel
BuildRequires: gsettings-qt-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: ffmpeg-devel
BuildRequires: mpv-libs-devel
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-bad-free-devel
BuildRequires: gstreamer1-plugins-good
BuildRequires: kf5-kwindowsystem-devel


Requires: ffmpeg
Requires: gstreamer1
Requires: gstreamer1-plugins-bad-free
Requires: gstreamer1-plugins-good

%description
kylin-recording

%prep

%setup -q
%patch0 -p1
%build

export PATH=%{_qt5_bindir}:$PATH
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} ..
%{make_build}
popd 

%install
pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd 

%files
%doc debian/changelog
%license  debian/copyright 
%{_bindir}/kylin-recorder
%{_datadir}/applications/kylin-recorder.desktop
%{_datadir}/pixmaps/recording_128.svg 
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/kylin-recorder/translations/*

%changelog
* Thu Aug 19 2021 peijiankang <peijiankang@kylinos.cn> - 1.2.23-1
- Init kylin-recorder package for openEuler
