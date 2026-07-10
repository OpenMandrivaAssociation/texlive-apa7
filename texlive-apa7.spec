%global tl_name apa7
%global tl_revision 63974

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.16
Release:	%{tl_revision}.1
Summary:	Format documents in APA style (7th edition)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/apa7
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apa7.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apa7.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apa7.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class formats documents in APA style (7th Edition). It provides a
full set of facilities in four different output modes (journal-like
appearance, double-spaced manuscript, double-spaced student manuscript,
LaTeX-like document). The class can mask author identity for copies for
use in masked peer review. The class is a development of the apa6 class.

