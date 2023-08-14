# Cosmocope generator

GitHub repository template to deploy generated export with [Cosma](https://github.com/graphlab-fr/cosma).

For each commit on branch "master", a new export is generated and deploy by GitHub action script (`/.github/workflows/main.yml`) on "gh-pages" branch. You need to configure GitHub Pages to deploy "gh-pages" branch.

Add records (markdown files) on directory `/docs`.

## Bibliography

Add your Zotero public group URL on file `/bibliography.js`. Then execute command `sh install.sh` to download and generate bibliographic files. Cosma use these files to add bibliographies and quotes on records content. See manual https://cosma.arthurperret.fr/user-manual.html#citations-and-bibliographies.

You can also ignore bibliography: delete line `node bibliography.js` from `/install.sh` and `prestart` from npm scripts from `/package.json`.

## Commands

```bash
npm start # generate cosmoscope
npm run add # add new record
```
