#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-httpuv
Version  : 1.3.6.2
Release  : 28
URL      : https://cran.r-project.org/src/contrib/httpuv_1.3.6.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/httpuv_1.3.6.2.tar.gz
Summary  : HTTP and WebSocket Server Library
Group    : Development/Tools
License  : GPL-3.0 MIT
Requires: R-httpuv-lib
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : clr-R-helpers

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

%description lib
lib components for the R-httpuv package.


%prep
%setup -q -c -n httpuv

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523308599

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523308599
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library httpuv
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library httpuv
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library httpuv
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library httpuv|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/httpuv/NEWS
/usr/lib64/R/library/httpuv/R/httpuv
/usr/lib64/R/library/httpuv/R/httpuv.rdb
/usr/lib64/R/library/httpuv/R/httpuv.rdx
/usr/lib64/R/library/httpuv/demo/daemon-echo.R
/usr/lib64/R/library/httpuv/demo/echo.R
/usr/lib64/R/library/httpuv/help/AnIndex
/usr/lib64/R/library/httpuv/help/aliases.rds
/usr/lib64/R/library/httpuv/help/httpuv.rdb
/usr/lib64/R/library/httpuv/help/httpuv.rdx
/usr/lib64/R/library/httpuv/help/paths.rds
/usr/lib64/R/library/httpuv/html/00Index.html
/usr/lib64/R/library/httpuv/html/R.css
/usr/lib64/R/library/httpuv/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/httpuv/libs/httpuv.so
/usr/lib64/R/library/httpuv/libs/httpuv.so.avx2
/usr/lib64/R/library/httpuv/libs/httpuv.so.avx512
