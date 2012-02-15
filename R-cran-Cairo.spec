%define modulename Cairo
%define realver 1.4-5
%define r_library %{_libdir}/R/library
%define _requires_exceptions libR.so

Summary:	A cairo bindings for R
Name:		R-cran-%{modulename}
Version:	%(echo %realver|tr '-' '.')
Release:	%mkrel 3
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
BuildRequires:	libcairo-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package provides a Cairo graphics device that can be 
use to create high-quality vector (PDF, PostScript and SVG) 
and bitmap output (PNG,JPEG,TIFF), and high-quality rendering 
in displays (X11 and Win32). Since it uses the same back-end 
for all output, copying across formats is WYSIWYG.Files are 
created without the dependence on X11 or other external programs.
This device supports alpha channel (semi-transparent drawing) and 
resulting images can contain transparent and semi-transparent regions.
It is ideal for use in server environemnts (file output) and as a 
replacement for other devices that don't have Cairo's capabilities 
such as alpha support or anti-aliasing.Backends are modular such that 
any subset of backends is supported.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{r_library}

# (tpg) install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# (tpg) provided by R-base
rm -rf %{buildroot}%{_libdir}/R/library/R.css

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/R/library/%{modulename}
