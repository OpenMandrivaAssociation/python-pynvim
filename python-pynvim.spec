Name:		python-pynvim
Version:	0.5.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pynvim/pynvim-%{version}.tar.gz
Summary:	Python client to neovim
URL:		https://pypi.org/project/pynvim/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Python client to neovim

%prep
%autosetup -p1 -n pynvim-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/pynvim
%{py_sitedir}/neovim
%{py_sitedir}/pynvim-*.*-info
