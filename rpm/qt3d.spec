Name:       qt5-qt3d
Summary:    Qt 3D
Version:    5.5
Release:    1
License:    LGPLv2.1 with exception or GPLv3
URL:        https://github.com/sailfishos/qt3d
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel >= 5.6.0
BuildRequires:  qt5-qtgui-devel >= 5.6.0
BuildRequires:  qt5-qtopengl-devel >= 5.6.0
BuildRequires:  qt5-qtnetwork-devel >= 5.6.0
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt 3D library


%package devel
Summary:        Qt Quick 3D - development files
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-devel = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt 3D development files


%prep
%setup -q -n %{name}-%{version}

%build
export QTDIR=/usr/share/qt5
touch .git
%qmake5
%make_build

%install
%qmake_install
# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la

# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_includedir}/qt5/Qt

%fdupes %{buildroot}/%{_includedir}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libQt53DCore.so.5*
%{_libdir}/libQt53DInput.so.5*
%{_libdir}/libQt53DOpenAL.so.5*
%{_libdir}/libQt53DRenderer.so.5*
%{_libdir}/libQt53DQuick.so.5*
%{_libdir}/libQt53DQuickRenderer.so.5*
%{_libdir}/qt5/qml/Qt3D/
%{_libdir}/qt5/qml/QtQuick/Scene3D

%files devel
%{_libdir}/libQt53DCore.so
%{_libdir}/libQt53DInput.so
%{_libdir}/libQt53DOpenAL.so
%{_libdir}/libQt53DRenderer.so
%{_libdir}/libQt53DQuick.so
%{_libdir}/libQt53DQuickRenderer.so
%{_libdir}/libQt53DCore.prl
%{_libdir}/libQt53DInput.prl
%{_libdir}/libQt53DOpenAL.prl
%{_libdir}/libQt53DQuick.prl
%{_libdir}/libQt53DQuickRenderer.prl
%{_libdir}/libQt53DRenderer.prl
%{_includedir}/qt5/Qt3DCore
%{_includedir}/qt5/Qt3DInput
%{_includedir}/qt5/Qt3DOpenAL
%{_includedir}/qt5/Qt3DRenderer
%{_includedir}/qt5/Qt3DQuick
%{_includedir}/qt5/Qt3DQuickRenderer
%{_libdir}/pkgconfig/Qt53DCore.pc
%{_libdir}/pkgconfig/Qt53DInput.pc
%{_libdir}/pkgconfig/Qt53DOpenAL.pc
%{_libdir}/pkgconfig/Qt53DQuick.pc
%{_libdir}/pkgconfig/Qt53DQuickRenderer.pc
%{_libdir}/pkgconfig/Qt53DRenderer.pc
%{_libdir}/cmake/Qt53DCore/
%{_libdir}/cmake/Qt53DInput/
%{_libdir}/cmake/Qt53DOpenAL/
%{_libdir}/cmake/Qt53DRenderer/
%{_libdir}/cmake/Qt53DQuick/
%{_libdir}/cmake/Qt53DQuickRenderer/
%{_datadir}/qt5/mkspecs/modules/qt_lib_3dcore*.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_3dinput*.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_3dopenal*.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_3dquick*.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_3drenderer*.pri

