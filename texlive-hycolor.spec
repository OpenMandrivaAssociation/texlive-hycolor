Name:		texlive-hycolor
Version:	53584
Release:	1
Summary:	Implements colour for packages hyperref and bookmark
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hycolor
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hycolor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hycolor.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hycolor.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the code for the color option that is
used by packages hyperref and bookmark. It is not intended as
package for the user.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hycolor
%{_texmfdistdir}/tex/latex/hycolor
%doc %{_texmfdistdir}/doc/latex/hycolor

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
