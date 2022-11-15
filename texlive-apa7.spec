Name:		texlive-apa7
Version:	63974
Release:	1
Summary:	Format documents in APA style (7th edition)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/apa7
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa7.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa7.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa7.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class formats documents in APA style (7th Edition). It
provides a full set of facilities in four different output
modes (journal-like appearance, double-spaced manuscript,
double-spaced student manuscript, LaTeX-like document). The
class can mask author identity for copies for use in masked
peer review. The class is a development of the apa6 class.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/apa7
%{_texmfdistdir}/tex/latex/apa7
%doc %{_texmfdistdir}/doc/latex/apa7

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
