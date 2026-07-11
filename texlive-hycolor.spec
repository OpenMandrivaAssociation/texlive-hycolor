%global tl_name hycolor
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.10
Release:	%{tl_revision}.1
Summary:	Implements colour for packages hyperref and bookmark
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hycolor
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hycolor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hycolor.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hycolor.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the code for the color option that is used by
packages hyperref and bookmark. It is not intended as package for the
user.

