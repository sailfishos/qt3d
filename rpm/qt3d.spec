Name:       qt5-qt3d
Summary:    Qt 3D
Version:    0.0~git731.0158ce783
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel >= 5.9.5
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtconcurrent-devel
BuildRequires:  qt5-qtnetwork-devel
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
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-devel = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt 3D development files

%package tool-qgltf
Summary:    Qt3D GL Transmission Format tool
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description tool-qgltf
This package contains the Qt3D GL Transmission Format tool.

%package import
Summary:    Qt3D QML Module
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import
This package contains the Qt3D QML module

%package import-scene2d
Summary:    QtQuick.Scene2D QML Module
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-scene2d
This package contains the QtQuick.Scene2D QML module.

%package import-scene3d
Summary:    QtQuick.Scene3D QML Module
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-scene3d
This package contains the QtQuick.Scene3D QML module.

%package plugin-geometryloader-default
Summary:    Qt3D default geometry loader plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-geometryloader-default
This package contains the Qt3D default geometry loader plugin.

%package plugin-geometryloader-gltf
Summary:    Qt3D glTF geometry loader plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-geometryloader-gltf
This package contains the Qt3D GL Transmission Format geometry loader plugin.

%package plugin-render-scene2d
Summary:    Qt3D Scene 2D render plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-render-scene2d
This package contains the Qt3D Scene 2D render plugin.

%package plugin-sceneparser-assimp
Summary:    Qt3D Assimp import scene parser plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-sceneparser-assimp
This package contains the Qt3D Open Asset Import Library scene parser plugin.

%package plugin-sceneparser-gltf-import
Summary:    Qt3D glTF import scene parser plugin.
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-sceneparser-gltf-import
This package contains the Qt3D GL Transmission Format import scene parser plugin.

%package plugin-sceneparser-gltf-export
Summary:    Qt3D glTF export scene parser plugin.
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-sceneparser-gltf-export
This package contains the Qt3D GL Transmission Format export scene parser plugin.


%prep
%setup -q -n %{name}-%{version}

%build
export QTDIR=/usr/share/qt5
touch .git
%qmake5
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
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


%post
/sbin/ldconfig
%postun
/sbin/ldconfig



%files
%defattr(-,root,root,-)
%{_libdir}/libQt53D*.so.*
#%{_qt5_bindir}/qglinfo

%files devel
%defattr(-,root,root,-)
%{_libdir}/libQt53D*.so
%{_libdir}/libQt53D*.prl
%{_includedir}/qt5/Qt3D*/
%{_includedir}/qt5/Qt3DQuick
%{_libdir}/pkgconfig/Qt53D*.pc
%{_libdir}/pkgconfig/Qt53DQuick.pc
%{_libdir}/cmake/Qt53D*/
%{_datadir}/qt5/mkspecs/modules/qt_lib_3d*.pri
%dir %{_libdir}/qt5/plugins/geometryloaders
%dir %{_libdir}/qt5/plugins/renderplugins
%dir %{_libdir}/qt5/plugins/sceneparsers

%files tool-qgltf
%defattr(-,root,root,-)
%{_libdir}/qt5/bin/qgltf

%files import
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/Qt3D/

%files import-scene2d
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/Scene2D/

%files import-scene3d
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/Scene3D/

%files plugin-geometryloader-default
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/geometryloaders/libdefaultgeometryloader.so


%files plugin-geometryloader-gltf
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/geometryloaders/libgltfgeometryloader.so


%files plugin-render-scene2d
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/renderplugins/libscene2d.so


%files plugin-sceneparser-assimp
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sceneparsers/libassimpsceneimport.so


%files plugin-sceneparser-gltf-import
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sceneparsers/libgltfsceneexport.so


%files plugin-sceneparser-gltf-export
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sceneparsers/libgltfsceneimport.so
