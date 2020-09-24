#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : msgpack
Version  : 1.0.0
Release  : 15
URL      : https://files.pythonhosted.org/packages/e4/4f/057549afbd12fdd5d9aae9df19a6773a3d91988afe7be45b277e8cee2f4d/msgpack-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e4/4f/057549afbd12fdd5d9aae9df19a6773a3d91988afe7be45b277e8cee2f4d/msgpack-1.0.0.tar.gz
Summary  : MessagePack (de)serializer.
Group    : Development/Tools
License  : Apache-2.0
Requires: msgpack-license = %{version}-%{release}
Requires: msgpack-python = %{version}-%{release}
Requires: msgpack-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# MessagePack for Python
[![Build Status](https://travis-ci.org/msgpack/msgpack-python.svg?branch=master)](https://travis-ci.org/msgpack/msgpack-python)
[![Documentation Status](https://readthedocs.org/projects/msgpack-python/badge/?version=latest)](https://msgpack-python.readthedocs.io/en/latest/?badge=latest)

%package license
Summary: license components for the msgpack package.
Group: Default

%description license
license components for the msgpack package.


%package python
Summary: python components for the msgpack package.
Group: Default
Requires: msgpack-python3 = %{version}-%{release}

%description python
python components for the msgpack package.


%package python3
Summary: python3 components for the msgpack package.
Group: Default
Requires: python3-core
Provides: pypi(msgpack)

%description python3
python3 components for the msgpack package.


%prep
%setup -q -n msgpack-1.0.0
cd %{_builddir}/msgpack-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583174735
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/msgpack
cp %{_builddir}/msgpack-1.0.0/COPYING %{buildroot}/usr/share/package-licenses/msgpack/175e59be229a5bedc6be93e958a970385bb04a62
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/msgpack/175e59be229a5bedc6be93e958a970385bb04a62

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
