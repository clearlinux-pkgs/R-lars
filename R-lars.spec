#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lars
Version  : 1.3
Release  : 49
URL      : https://cran.r-project.org/src/contrib/lars_1.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lars_1.3.tar.gz
Summary  : Least Angle Regression, Lasso and Forward Stagewise
Group    : Development/Tools
License  : GPL-2.0
Requires: R-lars-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
sequence with the cost of a single least squares
		fit. Least angle regression and infinitesimal forward
		stagewise regression are related to the lasso, as
		described in the paper below.

%package lib
Summary: lib components for the R-lars package.
Group: Libraries

%description lib
lib components for the R-lars package.


%prep
%setup -q -c -n lars
cd %{_builddir}/lars

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649948708

%install
export SOURCE_DATE_EPOCH=1649948708
rm -rf %{buildroot}
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lars
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lars
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lars
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc lars || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lars/DESCRIPTION
/usr/lib64/R/library/lars/INDEX
/usr/lib64/R/library/lars/Meta/Rd.rds
/usr/lib64/R/library/lars/Meta/data.rds
/usr/lib64/R/library/lars/Meta/features.rds
/usr/lib64/R/library/lars/Meta/hsearch.rds
/usr/lib64/R/library/lars/Meta/links.rds
/usr/lib64/R/library/lars/Meta/nsInfo.rds
/usr/lib64/R/library/lars/Meta/package.rds
/usr/lib64/R/library/lars/NAMESPACE
/usr/lib64/R/library/lars/R/lars
/usr/lib64/R/library/lars/R/lars.rdb
/usr/lib64/R/library/lars/R/lars.rdx
/usr/lib64/R/library/lars/data/diabetes.RData
/usr/lib64/R/library/lars/help/AnIndex
/usr/lib64/R/library/lars/help/aliases.rds
/usr/lib64/R/library/lars/help/lars.rdb
/usr/lib64/R/library/lars/help/lars.rdx
/usr/lib64/R/library/lars/help/paths.rds
/usr/lib64/R/library/lars/html/00Index.html
/usr/lib64/R/library/lars/html/R.css
/usr/lib64/R/library/lars/ratfor/delcol.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lars/libs/lars.so
/usr/lib64/R/library/lars/libs/lars.so.avx2
/usr/lib64/R/library/lars/libs/lars.so.avx512
