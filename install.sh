mkdir public
mkdir assets

curl -o "./assets/citeproc-style.csl" https://www.zotero.org/styles/iso690-author-date-fr-no-abstract
curl -o "./assets/citeproc-i18n.xml" https://raw.githubusercontent.com/citation-style-language/locales/6b0cb4689127a69852f48608b6d1a879900f418b/locales-fr-FR.xml

node bibliography.js