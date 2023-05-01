#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-httpuv
Version  : 1.6.9
Release  : 89
URL      : https://cran.r-project.org/src/contrib/httpuv_1.6.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/httpuv_1.6.9.tar.gz
Summary  : HTTP and WebSocket Server Library
Group    : Development/Tools
License  : CC-BY-4.0 GPL-2.0+ MIT
Requires: R-httpuv-lib = %{version}-%{release}
Requires: R-httpuv-license = %{version}-%{release}
Requires: R-R6
Requires: R-Rcpp
Requires: R-later
Requires: R-promises
BuildRequires : R-R6
BuildRequires : R-Rcpp
BuildRequires : R-later
BuildRequires : R-promises
BuildRequires : buildreq-R
BuildRequires : pkgconfig(zlib)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
HTTP and WebSocket requests directly from within R. It is primarily
    intended as a building block for other packages, rather than making it
    particularly easy to create complete web applications using httpuv alone.
    httpuv is built on top of the libuv and http-parser C libraries, both of
    which were developed by Joyent, Inc. (See LICENSE file for libuv and
    http-parser license information.)

%package lib
Summary: lib components for the R-httpuv package.
Group: Libraries
Requires: R-httpuv-license = %{version}-%{release}

%description lib
lib components for the R-httpuv package.


%package license
Summary: license components for the R-httpuv package.
Group: Default

%description license
license components for the R-httpuv package.


%prep
%setup -q -n httpuv
cd %{_builddir}/httpuv

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676394273

%install
export SOURCE_DATE_EPOCH=1676394273
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-httpuv
cp %{_builddir}/httpuv/src/http-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/R-httpuv/1a00a507fb89bb0018c092d6835077d541e76dc2 || :
cp %{_builddir}/httpuv/src/libuv/LICENSE %{buildroot}/usr/share/package-licenses/R-httpuv/848f7398f89046426a7ba23cb56cd3c93c030c64 || :
cp %{_builddir}/httpuv/src/libuv/LICENSE-docs %{buildroot}/usr/share/package-licenses/R-httpuv/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/httpuv/DESCRIPTION
/usr/lib64/R/library/httpuv/INDEX
/usr/lib64/R/library/httpuv/LICENSE
/usr/lib64/R/library/httpuv/Meta/Rd.rds
/usr/lib64/R/library/httpuv/Meta/demo.rds
/usr/lib64/R/library/httpuv/Meta/features.rds
/usr/lib64/R/library/httpuv/Meta/hsearch.rds
/usr/lib64/R/library/httpuv/Meta/links.rds
/usr/lib64/R/library/httpuv/Meta/nsInfo.rds
/usr/lib64/R/library/httpuv/Meta/package.rds
/usr/lib64/R/library/httpuv/NAMESPACE
/usr/lib64/R/library/httpuv/NEWS.md
/usr/lib64/R/library/httpuv/R/httpuv
/usr/lib64/R/library/httpuv/R/httpuv.rdb
/usr/lib64/R/library/httpuv/R/httpuv.rdx
/usr/lib64/R/library/httpuv/demo/daemon-echo.R
/usr/lib64/R/library/httpuv/demo/echo.R
/usr/lib64/R/library/httpuv/demo/json-server.R
/usr/lib64/R/library/httpuv/help/AnIndex
/usr/lib64/R/library/httpuv/help/aliases.rds
/usr/lib64/R/library/httpuv/help/httpuv.rdb
/usr/lib64/R/library/httpuv/help/httpuv.rdx
/usr/lib64/R/library/httpuv/help/paths.rds
/usr/lib64/R/library/httpuv/html/00Index.html
/usr/lib64/R/library/httpuv/html/R.css
/usr/lib64/R/library/httpuv/tests/testthat.R
/usr/lib64/R/library/httpuv/tests/testthat/apps/content/data.txt
/usr/lib64/R/library/httpuv/tests/testthat/apps/content/exclude/index.html
/usr/lib64/R/library/httpuv/tests/testthat/apps/content/exclude/subdir/index.html
/usr/lib64/R/library/httpuv/tests/testthat/apps/content/index.html
/usr/lib64/R/library/httpuv/tests/testthat/apps/content/mtcars.csv
/usr/lib64/R/library/httpuv/tests/testthat/apps/content/subdir/index.html
/usr/lib64/R/library/httpuv/tests/testthat/apps/content_1/index.html
/usr/lib64/R/library/httpuv/tests/testthat/helper-app.R
/usr/lib64/R/library/httpuv/tests/testthat/sample_app.R
/usr/lib64/R/library/httpuv/tests/testthat/test-app.R
/usr/lib64/R/library/httpuv/tests/testthat/test-frame-completion.R
/usr/lib64/R/library/httpuv/tests/testthat/test-http-parse.R
/usr/lib64/R/library/httpuv/tests/testthat/test-static-paths.R
/usr/lib64/R/library/httpuv/tests/testthat/test-traffic.R
/usr/lib64/R/library/httpuv/tests/testthat/test-utils.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/httpuv/libs/httpuv.so
/usr/lib64/R/library/httpuv/libs/httpuv.so.avx2
/usr/lib64/R/library/httpuv/libs/httpuv.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-httpuv/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb
/usr/share/package-licenses/R-httpuv/1a00a507fb89bb0018c092d6835077d541e76dc2
/usr/share/package-licenses/R-httpuv/848f7398f89046426a7ba23cb56cd3c93c030c64
