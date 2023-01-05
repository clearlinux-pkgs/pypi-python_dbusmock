#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-python_dbusmock
Version  : 0.28.7
Release  : 33
URL      : https://files.pythonhosted.org/packages/c2/69/5d31a5c186a78bd0887d0ac81556d8a1d89b9ee4fed6cf046978dcdc51a3/python-dbusmock-0.28.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/c2/69/5d31a5c186a78bd0887d0ac81556d8a1d89b9ee4fed6cf046978dcdc51a3/python-dbusmock-0.28.7.tar.gz
Summary  : Mock D-Bus objects
Group    : Development/Tools
License  : LGPL-3.0 LGPL-3.0+
Requires: pypi-python_dbusmock-license = %{version}-%{release}
Requires: pypi-python_dbusmock-python = %{version}-%{release}
Requires: pypi-python_dbusmock-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(dbus_python)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Remove-dbus-requirement.patch

%description
![CI status](https://github.com/martinpitt/python-dbusmock/actions/workflows/tests.yml/badge.svg)

%package license
Summary: license components for the pypi-python_dbusmock package.
Group: Default

%description license
license components for the pypi-python_dbusmock package.


%package python
Summary: python components for the pypi-python_dbusmock package.
Group: Default
Requires: pypi-python_dbusmock-python3 = %{version}-%{release}

%description python
python components for the pypi-python_dbusmock package.


%package python3
Summary: python3 components for the pypi-python_dbusmock package.
Group: Default
Requires: python3-core
Provides: pypi(python_dbusmock)
Requires: pypi(dbus_python)

%description python3
python3 components for the pypi-python_dbusmock package.


%prep
%setup -q -n python-dbusmock-0.28.7
cd %{_builddir}/python-dbusmock-0.28.7
%patch1 -p1
pushd ..
cp -a python-dbusmock-0.28.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672933887
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-python_dbusmock
cp %{_builddir}/python-dbusmock-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-python_dbusmock/f45ee1c765646813b442ca58de72e20a64a7ddba || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-python_dbusmock/f45ee1c765646813b442ca58de72e20a64a7ddba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
