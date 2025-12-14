import re

decision_ref_re = re.compile(r'<a\s+href="/decision/(?P<id>[^\?]+)')

#
# Regexps pour le bloc titre
#
title_re = re.compile(
	r'<h1>\s*'
	r'(?P<day>\d{1,2})\s+'
	r'(?P<month>[^\d<]+?)\s+'
	r'(?P<year>\d{4})<br>\s*'
	r'Cour\s+de\s+cassation<br>\s*'
	r'Pourvoi\s+n°\s*'
	r'(?P<number>[\d\-.]+)\s*</h1>',
	re.UNICODE | re.IGNORECASE | re.DOTALL,
)

#
# Regexps pour le "header"
#
# Le bloc "header" est de la forme:
#
#<div class="decision-header">
# <p class="h4-like">Troisième chambre civile
#                          -
#              Formation restreinte RNSM/NA
#                      </p>
#                              <p class="h4-like h4-like--emphase">
#                      </p>
#          <p>ECLI:FR:CCASS:2024:C310675</p>
#        </div>
#
header_re = re.compile(r'<div\s+class="decision-header">(?P<header>.*?)</div>', re.DOTALL)
chambre_re = re.compile(
	r'(?P<chambre>'
	r'Chambre\scommerciale\sfinancière\set\séconomique'
	r'|Chambre\scriminelle'
	r'|Chambre\ssociale'
	r'|Deuxième\schambre\scivile'
	r'|Première\schambre\scivile'
	r'|Première\sprésidence\s\(Ordonnance\)'
	r'|Troisième\schambre\scivile'
	r')', re.UNICODE
)
publication_re = re.compile(r'(?P<publication>Publié au Bulletin|Publié au Rapport)')
formation_re = re.compile(r'[-‐–—]\s*(?P<formation>Formation[^<]+)')
ecli_re = re.compile(r"<p>(?P<ecli>ECLI:.*?)</p>")
solution_re = re.compile(r'^\s*(?P<solution>CASSATION|REJET|IRRECEVABILITÉ|DÉSISTEMENT)\s*<br>', re.MULTILINE)
texts_re = re.compile(r'Vu\s+(?:les?\s+)?(?P<texts>articles?[^<]+)\s*:\s*<br>', re.IGNORECASE)
