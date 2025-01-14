Name:           kylin-recorder
Version:        1.3.0
Release:        4
Summary:        kylin-recorder
License:        GPL-3.0-or-later
URL:            https://github.com/UbuntuKylin/kylin-recorder
Source0:        %{name}-%{version}.tar.gz
Patch01:        0001-add-user-guide-for-kylin-recorder.patch

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
%patch01 -p1

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
%{_datadir}/kylin-user-guide/data/guide/kylin-recorder

%changelog
* Wed Mar 22 2023 peijiankang <peijiankang@kylinos.cn> - 1.3.0-4
- fix user-guide for kylin-recorder in English

* Mon Mar 06 2023 peijiankang <peijiankang@kylinos.cn> - 1.3.0-3
- add user-guide for kylin-recorder

* Mon Feb 06 2023 peijiankang <peijiankang@kylinos.cn> - 1.3.0-2
- add build debuginfo and debugsource

* Mon Oct 24 2022 tanyulong<tanyulong@kylinos.cn> - 1.3.0-1
- update upstream version 1.3.0

* Wed May 18 2022 tanyulong<tanyulong@kylinos.cn> - 1.2.23-3
- Improve the project according to the requirements of compliance improvement

* Tue Sep 14 2021 douyan <douyan@kylinos.cn> - 1.2.23-2
- fix title bar issue

* Thu Aug 19 2021 peijiankang <peijiankang@kylinos.cn> - 1.2.23-1
- Init kylin-recorder package for openEuler
