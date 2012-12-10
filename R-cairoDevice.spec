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


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.19-1
+ Revision: 775025
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.18-2
+ Revision: 774835
- Do the proper Provides/Obsoletes or previous R packages.

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.18-1
+ Revision: 774654
- Rebuild with R2spec.
- Update and rebuild with R2spec

* Sat Sep 11 2010 Funda Wang <fwang@mandriva.org> 1.4.5-3mdv2011.0
+ Revision: 577196
- rebuild

* Thu Jan 14 2010 Funda Wang <fwang@mandriva.org> 1.4.5-2mdv2010.1
+ Revision: 491115
- rebuild for new jpeg

* Fri Dec 25 2009 Jérôme Brenier <incubusss@mandriva.org> 1.4.5-1mdv2010.1
+ Revision: 482226
- new version 1.4.5

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Aug 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.3-1mdv2009.0
+ Revision: 270296
- update to new version 1.4-3

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Fri Feb 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.5-2mdv2008.1
+ Revision: 176956
- remove requires on libR.so

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.5-1mdv2008.1
+ Revision: 169883
- fix Url
- add missing buildrequires
- add source and spec file
- Created package structure for R-cran-Cairo.

