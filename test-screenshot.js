
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
        console.log('ping')
        const box = await preview.boundingBox();
        const slug = await preview.$eval(
            '.slug', node => node.innerText
        )
        console.log(slug)
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