// Copies the PWA files into www/ so Capacitor can bundle them.
import {cpSync, rmSync, mkdirSync} from 'node:fs';
rmSync('www', {recursive: true, force: true});
mkdirSync('www', {recursive: true});
for (const f of ['index.html', 'manifest.webmanifest']) cpSync(f, `www/${f}`);
cpSync('icons', 'www/icons', {recursive: true});
cpSync('img', 'www/img', {recursive: true});
console.log('www ready');
