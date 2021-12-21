/*

# generate card previews

requires running jekyll to load previews.html, which puppeteer take screenshots of. 

generates files in reverse date order, so running should backfill until first existing file found.

to re-generate, delete existing files. 

*/
const chromium = require('puppeteer');
const fs = require("fs");
const path = require("path");

(async () => {
    const browser = await chromium.launch({});

    const page = await browser.newPage();
    await page.setViewport({ width: 1200, height: 100000 }); 
    await page.goto('http://localhost:4000/blog/previews/')
    await page.waitForSelector('.preview');

    const previews = await page.$$('.preview')
    for (const preview of previews) {
        const box = await preview.boundingBox();
        const slug = await preview.$eval(
            '.slug', node => node.innerText
        )
        console.log(slug)
        var path = `./assets/cards/${slug}.png`
        if (fs.existsSync(path)) { 
            console.log(path + " exists! Exiting.")
            process.exit(0);
        } 
        await page.screenshot({
            path: `./assets/cards/${slug}.png`,
            type: "png",
            clip: { x: box['x'], y: box['y'], 
                    width: box['width'], height: box['height'] }
        });

        console.log('pong')
    }

    await browser.close();
})();
