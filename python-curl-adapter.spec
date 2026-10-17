%define module curl_adapter

Name:		python-curl-adapter
Version:	1.2.3
Release:	1
Summary:	requests adapter that picks pycurl or curl_cffi
License:	MIT
Group:		Development/Python
URL:		https://github.com/el1s7/curl-adapter
Source0:	https://files.pythonhosted.org/packages/source/c/curl-adapter/%{module}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pip)

%description
HTTP adapter for requests. It can send the request through pycurl or through
curl_cffi so the TLS handshake matches a browser.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
