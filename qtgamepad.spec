#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtgamepad
Version  : 5.15.2
Release  : 21
URL      : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtgamepad-everywhere-src-5.15.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtgamepad-everywhere-src-5.15.2.tar.xz
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


%package examples
Summary: examples components for the qtgamepad package.
Group: Default
Requires: qtgamepad-dev = %{version}-%{release}

%description examples
examples components for the qtgamepad package.


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
%setup -q -n qtgamepad-everywhere-src-5.15.2
cd %{_builddir}/qtgamepad-everywhere-src-5.15.2

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
export SOURCE_DATE_EPOCH=1630806437
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtgamepad
cp %{_builddir}/qtgamepad-everywhere-src-5.15.2/LICENSE.GPL %{buildroot}/usr/share/package-licenses/qtgamepad/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qtgamepad-everywhere-src-5.15.2/LICENSE.LGPLv3 %{buildroot}/usr/share/package-licenses/qtgamepad/d8c5ba35d57eceb2e56ace166048cb901a2d12ed
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtGamepad/5.15.2/QtGamepad/private/qgamepadbackend_p.h
/usr/include/qt5/QtGamepad/5.15.2/QtGamepad/private/qgamepadbackendfactory_p.h
/usr/include/qt5/QtGamepad/5.15.2/QtGamepad/private/qgamepadbackendplugin_p.h
/usr/include/qt5/QtGamepad/5.15.2/QtGamepad/private/qtgamepad-config_p.h
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

%files examples
%defattr(-,root,root,-)
/usr/share/qt5/examples/gamepad/gamepad.pro
/usr/share/qt5/examples/gamepad/keyNavigation/keyNavigation.pro
/usr/share/qt5/examples/gamepad/keyNavigation/main.cpp
/usr/share/qt5/examples/gamepad/keyNavigation/qml.qrc
/usr/share/qt5/examples/gamepad/keyNavigation/qml/main.qml
/usr/share/qt5/examples/gamepad/mouseItem/main.cpp
/usr/share/qt5/examples/gamepad/mouseItem/mouseItem.pro
/usr/share/qt5/examples/gamepad/mouseItem/qml.qrc
/usr/share/qt5/examples/gamepad/mouseItem/qml/main.qml
/usr/share/qt5/examples/gamepad/simple/android/AndroidManifest.xml
/usr/share/qt5/examples/gamepad/simple/gamepadmonitor.cpp
/usr/share/qt5/examples/gamepad/simple/gamepadmonitor.h
/usr/share/qt5/examples/gamepad/simple/main.cpp
/usr/share/qt5/examples/gamepad/simple/simple.pro

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Gamepad.so.5
/usr/lib64/libQt5Gamepad.so.5.15
/usr/lib64/libQt5Gamepad.so.5.15.2
/usr/lib64/qt5/plugins/gamepads/libevdevgamepad.so
/usr/lib64/qt5/qml/QtGamepad/libdeclarative_gamepad.so
/usr/lib64/qt5/qml/QtGamepad/plugins.qmltypes
/usr/lib64/qt5/qml/QtGamepad/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtgamepad/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qtgamepad/d8c5ba35d57eceb2e56ace166048cb901a2d12ed
