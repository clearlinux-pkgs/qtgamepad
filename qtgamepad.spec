#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtgamepad
Version  : 5.13.1
Release  : 15
URL      : https://download.qt.io/official_releases/qt/5.13/5.13.1/submodules/qtgamepad-everywhere-src-5.13.1.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.13/5.13.1/submodules/qtgamepad-everywhere-src-5.13.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: qtgamepad-lib = %{version}-%{release}
Requires: qtgamepad-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : qtbase-staticdev
BuildRequires : systemd-dev

%description
Qt Gamepad
A Qt 5 module that adds support for getting events from gamepad devices on multiple platforms.

%package dev
Summary: dev components for the qtgamepad package.
Group: Development
Requires: qtgamepad-lib = %{version}-%{release}
Provides: qtgamepad-devel = %{version}-%{release}
Requires: qtgamepad = %{version}-%{release}

%description dev
dev components for the qtgamepad package.


%package lib
Summary: lib components for the qtgamepad package.
Group: Libraries
Requires: qtgamepad-license = %{version}-%{release}

%description lib
lib components for the qtgamepad package.


%package license
Summary: license components for the qtgamepad package.
Group: Default

%description license
license components for the qtgamepad package.


%prep
%setup -q -n qtgamepad-everywhere-src-5.13.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1568396350
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtgamepad
cp LICENSE.GPL %{buildroot}/usr/share/package-licenses/qtgamepad/LICENSE.GPL
cp LICENSE.LGPLv3 %{buildroot}/usr/share/package-licenses/qtgamepad/LICENSE.LGPLv3
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtGamepad/5.13.1/QtGamepad/private/qgamepadbackend_p.h
/usr/include/qt5/QtGamepad/5.13.1/QtGamepad/private/qgamepadbackendfactory_p.h
/usr/include/qt5/QtGamepad/5.13.1/QtGamepad/private/qgamepadbackendplugin_p.h
/usr/include/qt5/QtGamepad/5.13.1/QtGamepad/private/qtgamepad-config_p.h
/usr/include/qt5/QtGamepad/QGamepad
/usr/include/qt5/QtGamepad/QGamepadKeyNavigation
/usr/include/qt5/QtGamepad/QGamepadManager
/usr/include/qt5/QtGamepad/QtGamepad
/usr/include/qt5/QtGamepad/QtGamepadDepends
/usr/include/qt5/QtGamepad/QtGamepadVersion
/usr/include/qt5/QtGamepad/qgamepad.h
/usr/include/qt5/QtGamepad/qgamepadkeynavigation.h
/usr/include/qt5/QtGamepad/qgamepadmanager.h
/usr/include/qt5/QtGamepad/qtgamepad-config.h
/usr/include/qt5/QtGamepad/qtgamepadglobal.h
/usr/include/qt5/QtGamepad/qtgamepadversion.h
/usr/lib64/cmake/Qt5Gamepad/Qt5GamepadConfig.cmake
/usr/lib64/cmake/Qt5Gamepad/Qt5GamepadConfigVersion.cmake
/usr/lib64/cmake/Qt5Gamepad/Qt5Gamepad_QEvdevGamepadBackendPlugin.cmake
/usr/lib64/libQt5Gamepad.prl
/usr/lib64/libQt5Gamepad.so
/usr/lib64/pkgconfig/Qt5Gamepad.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_gamepad.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_gamepad_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Gamepad.so.5
/usr/lib64/libQt5Gamepad.so.5.13
/usr/lib64/libQt5Gamepad.so.5.13.1
/usr/lib64/qt5/plugins/gamepads/libevdevgamepad.so
/usr/lib64/qt5/qml/QtGamepad/libdeclarative_gamepad.so
/usr/lib64/qt5/qml/QtGamepad/plugins.qmltypes
/usr/lib64/qt5/qml/QtGamepad/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtgamepad/LICENSE.GPL
/usr/share/package-licenses/qtgamepad/LICENSE.LGPLv3
