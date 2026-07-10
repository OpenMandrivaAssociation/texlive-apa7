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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class formats documents in APA style (7th Edition). It provides a
full set of facilities in four different output modes (journal-like
appearance, double-spaced manuscript, double-spaced student manuscript,
LaTeX-like document). The class can mask author identity for copies for
use in masked peer review. The class is a development of the apa6 class.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/apa7
%dir %{_datadir}/texmf-dist/source/latex/apa7
%dir %{_datadir}/texmf-dist/tex/latex/apa7
%dir %{_datadir}/texmf-dist/doc/latex/apa7/samples
%dir %{_datadir}/texmf-dist/tex/latex/apa7/config
%doc %{_datadir}/texmf-dist/doc/latex/apa7/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/apa7/apa7.pdf
%doc %{_datadir}/texmf-dist/doc/latex/apa7/samples/Figure1.pdf
%doc %{_datadir}/texmf-dist/doc/latex/apa7/samples/bibliography.bib
%doc %{_datadir}/texmf-dist/doc/latex/apa7/samples/longsample.pdf
%doc %{_datadir}/texmf-dist/doc/latex/apa7/samples/longsample.tex
%doc %{_datadir}/texmf-dist/doc/latex/apa7/samples/shortsample.pdf
%doc %{_datadir}/texmf-dist/doc/latex/apa7/samples/shortsample.tex
%doc %{_datadir}/texmf-dist/source/latex/apa7/apa7.dtx
%doc %{_datadir}/texmf-dist/source/latex/apa7/apa7.ins
%{_datadir}/texmf-dist/tex/latex/apa7/apa7.cls
%{_datadir}/texmf-dist/tex/latex/apa7/config/APA7american.txt
%{_datadir}/texmf-dist/tex/latex/apa7/config/APA7british.txt
%{_datadir}/texmf-dist/tex/latex/apa7/config/APA7czech.txt
%{_datadir}/texmf-dist/tex/latex/apa7/config/APA7dutch.txt
%{_datadir}/texmf-dist/tex/latex/apa7/config/APA7endfloat.cfg
%{_datadir}/texmf-dist/tex/latex/apa7/config/APA7english.txt
%{_datadir}/texmf-dist/tex/latex/apa7/config/APA7french.txt
%{_datadir}/texmf-dist/tex/latex/apa7/config/APA7german.txt
%{_datadir}/texmf-dist/tex/latex/apa7/config/APA7greek.txt
%{_datadir}/texmf-dist/tex/latex/apa7/config/APA7hungarian.txt
%{_datadir}/texmf-dist/tex/latex/apa7/config/APA7ngerman.txt
%{_datadir}/texmf-dist/tex/latex/apa7/config/APA7spanish.txt
%{_datadir}/texmf-dist/tex/latex/apa7/config/APA7turkish.txt
