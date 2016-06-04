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
#%{_libdir}/libQt53D.so.5.*
%{_libdir}/libQt53DQuick.so.5.*
%{_libdir}/libQt53DQuick.so.5
%{_libdir}/qt5/qml/Qt3D/
#%{_qt5_bindir}/qglinfo


%files devel
%defattr(-,root,root,-)
#%{_libdir}/libQt53D.so
#%{_libdir}/libQt53D.prl
%{_libdir}/libQt53DQuick.so
%{_libdir}/libQt53DQuick.prl
#%{_includedir}/qt5/Qt3D/
%{_includedir}/qt5/Qt3DQuick
#%{_libdir}/pkgconfig/Qt53D.pc
%{_libdir}/pkgconfig/Qt53DQuick.pc
#%{_libdir}/cmake/Qt53D/
%{_libdir}/cmake/Qt53DQuick/
#%{_datadir}/qt5/mkspecs/modules/qt_lib_3d.pri
#%{_datadir}/qt5/mkspecs/modules/qt_lib_3d_private.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_3dquick.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_3dquick_private.pri


