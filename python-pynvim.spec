%define module pynvim

Name:		python-pynvim
Version:	0.6.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Python client to neovim
URL:		https://pypi.org/project/pynvim/
License:	Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

# Duplicate package detected 2025/04/25 after 6.0
%rename python-neovim

%description
Python client to neovim

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%doc README.md
%license LICENSE
%{_bindir}/%{module}-python
%{py_sitedir}/neovim
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
