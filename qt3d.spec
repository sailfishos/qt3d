%define _qtmodule_snapshot_version 5.0.0-beta1
Name:       qt5-qt3d
Summary:    Qt 3D
Version:    5.0.0~beta1
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
#Source0:    %{name}-%{version}.tar.xz
Source0:    qt3d-opensource-src-%{_qtmodule_snapshot_version}.tar.xz
Patch0:     remove-egl.patch
Patch1:     0007-Fix-assimp-build-on-uncommon-architectures.patch
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  qt5-qtnetwork-devel
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

%package qt3dquick
Summary:        Qt Quick 3D - core library
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description qt3dquick
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Quick 3D core library

%package qt3dquick-devel
Summary:        Qt Quick 3D - core development headers
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description qt3dquick-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Quick 3D core development headers


%package plugin-imageformat-tga
Summary:        Qt Quick 3D - TGA image format plugin
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description plugin-imageformat-tga
This package contains the TGA image format plugin

%package plugin-sceneformat-ai
Summary:        Qt Quick 3D - all-inclusive scene format plugin
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description plugin-sceneformat-ai
This package contains the all-inclusive scene format plugin

%package plugin-sceneformat-bezier
Summary:        Qt Quick 3D - bezier scene format plugin
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description plugin-sceneformat-bezier
This package contains the bezier scene format plugin


%package -n qt5-qtdeclarative-import-qt3d-shapes
Summary:        Qt Quick 3D - declarative Qt3D shapes import
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-qt3d-shapes
This package contains the Qt3D shapes import for QtDeclarative

%package -n qt5-qtdeclarative-import-qt3d
Summary:        Qt Quick 3D - declarative Qt3D import
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-qt3d
This package contains the Qt3D import for QtDeclarative


#### Build section

%prep
%setup -q -n qt3d-opensource-src-%{_qtmodule_snapshot_version}
%patch0 -p1
%patch1 -p1
%build
export QTDIR=/usr/share/qt5
%qmake CONFIG+=package
make %{?_smp_flags}

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


#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%post qt3dquick
/sbin/ldconfig
%postun qt3dquick
/sbin/ldconfig


#### File section

%files
%defattr(-,root,root,-)
%{_libdir}/libQt3D.so.5
%{_libdir}/libQt3D.so.5.*
%{_bindir}/qglinfo
%{_libdir}/cmake/Qt53D/
%{_libdir}/cmake/Qt53DQuick/

%files devel
%defattr(-,root,root,-)
%{_libdir}/libQt3D.so
%{_libdir}/libQt3D.prl
%{_includedir}/qt5/Qt3D/
%{_libdir}/pkgconfig/Qt3D.pc
#%{_datadir}/qt5/mkspecs/features/qt3dquick.prf
%{_datadir}/qt5/mkspecs/modules/qt_3dquick.pri

%files qt3dquick
%defattr(-,root,root,-)
%{_libdir}/libQt3DQuick.so.5
%{_libdir}/libQt3DQuick.so.5.*


%files qt3dquick-devel
%defattr(-,root,root,-)
%{_libdir}/libQt3DQuick.so
%{_libdir}/libQt3DQuick.prl
%{_includedir}/qt5/Qt3DQuick/
%{_libdir}/pkgconfig/Qt3DQuick.pc
#%{_datadir}/qt5/mkspecs/features/qt3d.prf
%{_datadir}/qt5/mkspecs/modules/qt_3d.pri

#%files plugin-imageformat-tga
#%defattr(-,root,root,-)
#%{_libdir}/qt5/plugins/imageformats/libqtga.so

%files plugin-sceneformat-ai
%defattr(-,root,root,-)
#%{_libdir}/qt5/plugins/sceneformats/libqsceneai.so

%files plugin-sceneformat-bezier
%defattr(-,root,root,-)
#%{_libdir}/qt5/plugins/sceneformats/libqscenebezier.so

%files -n qt5-qtdeclarative-import-qt3d-shapes
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt3D/Shapes/

%files -n qt5-qtdeclarative-import-qt3d
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt3D/qmldir
%{_libdir}/qt5/imports/Qt3D/plugins.qmltypes
%{_libdir}/qt5/imports/Qt3D/library.xml
%{_libdir}/qt5/imports/Qt3D/libqthreedqmlplugin.so

#### No changelog section, separate $pkg.changes contains the history

