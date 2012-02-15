%global packname  cairoDevice
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.18
Release:          1
Summary:          Cairo-based cross-platform antialiased graphics device driver
Group:            Sciences/Mathematics
License:          GPL
URL:              None
Source0:          http://cran.r-project.org/src/contrib/Archive/cairoDevice/cairoDevice_2.18.tar.gz

%rename R-cran-Cairo
Requires:         R-grDevices 

BuildRequires:    Rmath-devel texlive-collection-latex 
BuildRequires:    R-grDevices 
BuildRequires:    x11-server-xvfb
BuildRequires:    cairo-devel
BuildRequires:    jpeg-devel
BuildRequires:    tiff-devel

%description
Cairo/GTK graphics device driver with output to screen, file (png, svg,
pdf, and ps) or memory (arbitrary GdkDrawable or Cairo context). The
screen device may be embedded into RGtk2 interfaces. Supports all
interactive features of other graphics devices, including
getGraphicsEvent().

%prep
%setup -q -c -n %{packname}

%build

%install
export DISPLAY=:20
Xvfb :20 -screen 0 1x1x24 -ac&
echo $! > Xvfb.pid
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
kill -9 `cat Xvfb.pid`
unset DISPLAY
rm -f Xvfb.pid

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
