%define		module	odict
Summary:	Ordered dictionary
Name:		python-odict
Version:	1.5.0
Release:	2
License:	Python
Group:		Libraries/Python
URL:		http://slimit.org/
Source0:	http://pypi.python.org/packages/source/o/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	43d4b2d5775245c6f11df12a09c7bfdb
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dictionary in which the insertion order of items is preserved (using
an internal double linked list). In this implementation replacing an
existing item keeps it at its original position

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%if %{with tests}
# Tests are broken upstream and also require unpackaged python-interlude
# Uncomment when fixed upstream
#%{__python} setup.py test -m odict.tests
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.rst README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}*.egg-info
