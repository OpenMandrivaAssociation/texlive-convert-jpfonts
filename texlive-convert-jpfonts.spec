%global tl_name convert-jpfonts
%global tl_revision 73551

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Convert half-width Japanese to full-width beautifully
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/convert-jpfonts
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/convert-jpfonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/convert-jpfonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This style file is designed for converting Japanese half-width
characters to full-width characters beautifully. This is useful when
alphabet characters don't render properly in a Japanese font.

