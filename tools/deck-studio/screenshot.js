'use strict';
// Screenshot selected slides of a built deck.html via Chrome Headless Shell.
// Usage: node screenshot.js <deck.html> <outdir> <idx,idx,...>
const path = require('path');
const fs = require('fs');
const puppeteer = require('/home/hatch/workspace/video-kit/opus55/explainer-kinetic/node_modules/puppeteer-core');

const EXE = '/home/hatch/workspace/video-kit/node_modules/.remotion/chrome-headless-shell/linux64/chrome-headless-shell-linux64/chrome-headless-shell';
const [htmlPath, outDir, idxArg] = process.argv.slice(2);
const idxs = idxArg.split(',').map(Number);

(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await puppeteer.launch({
    executablePath: EXE,
    args: ['--no-sandbox', '--disable-gpu', '--force-color-profile=srgb', '--font-render-hinting=none'],
    defaultViewport: { width: 1280, height: 720 }
  });
  const page = await browser.newPage();
  page.on('pageerror', e => console.log('[pageerror]', e.message));
  await page.goto('file://' + path.resolve(htmlPath), { waitUntil: 'networkidle0', timeout: 60000 }).catch(async () => {
    await page.goto('file://' + path.resolve(htmlPath), { waitUntil: 'load' });
  });
  await page.evaluate(() => Promise.race([document.fonts.ready, new Promise(r => setTimeout(r, 3000))]));
  await page.evaluate(() => {
    document.getElementById('hud').style.display = 'none';
    document.getElementById('progress').style.display = 'none';
    document.getElementById('stage').style.transform = 'scale(1)';
  });
  for (const i of idxs) {
    await page.evaluate(k => window.__deck.goto(k), i);
    await page.evaluate(() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))));
    const out = path.join(outDir, 'slide-' + String(i + 1).padStart(2, '0') + '.png');
    await page.screenshot({ path: out });
    console.log('shot', out);
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
