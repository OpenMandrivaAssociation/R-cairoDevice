%global packname  cairoDevice
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.19
Release:          1
Summary:          Cairo-based cross-platform antialiased graphics device driver
Group:            Sciences/Mathematics
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-grDevices 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-grDevices 
BuildRequires:    cairo-devel
BuildRequires:    glib2-devel
BuildRequires:    gtk2-devel
BuildRequires:    jpeg-devel
BuildRequires:    tiff-devel
BuildRequires:    x11-server-xvfb
%rename R-cran-cairoDevice

%description
Cairo/GTK graphics device driver with output to screen, file (png, svg,
pdf, and ps) or memory (arbitrary GdkDrawable or Cairo context). The
screen device may be embedded into RGtk2 interfaces. Supports all
interactive features of other graphics devices, including

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
