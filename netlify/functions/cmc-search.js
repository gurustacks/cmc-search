const chrome = require('chrome-aws-lambda');
const puppeteer = require('puppeteer-core');


exports.handler = async function(event, context) {

    const browser = await puppeteer.launch({
        args: chrome.args,
        executablePath: process.env.CHROME_EXECUTABLE_PATH || await chrome.executablePath,
        headless: chrome.headless,
        ignoreSSLErrors: chrome.ignoreSSLErrors
    });
    
    const page = await browser.newPage();

    try {
        await page.goto('https://ipinfo.io/json');
    } catch(err) {
        console.log("Failed opening page with error:" + err);
    }
    
    await page.waitForTimeout(50000);

    // await page.waitForSelector("#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(1) > div > div.sc-111rrsy-0.qbrWo > div:nth-child(6) > div > div.sc-266vnq-1.gffsPR");
    // await page.click("#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(1) > div > div.sc-111rrsy-0.qbrWo > div:nth-child(6) > div > div.sc-266vnq-1.gffsPR");
    // await page.keyboard.type('L');
    // await page.keyboard.type('I');
    // await page.keyboard.type('N');
    // await page.keyboard.type('K');
    // await page.keyboard.press('Enter');
    // await page.waitForSelector("#__next > div.bywovg-1.fUzJes > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.jKrmxw.container > div > div.sc-16r8icm-0.sc-19zk94m-1.gRSJaB > div.sc-16r8icm-0.dSXRna > div.sc-16r8icm-0.sc-19zk94m-4.iNWJA-d > div > div.pqmllm-2.hLrBVF > button:nth-child(1)");
    // await page.click("#__next > div.bywovg-1.fUzJes > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.jKrmxw.container > div > div.sc-16r8icm-0.sc-19zk94m-1.gRSJaB > div.sc-16r8icm-0.dSXRna > div.sc-16r8icm-0.sc-19zk94m-4.iNWJA-d > div > div.pqmllm-2.hLrBVF > button:nth-child(1)");
    // url = await page.url();
    // title = await page.title();
    // await page.waitTimeout(50000);
    // await browser.close();

    return {
        statusCode: 200,
        body: JSON.stringify({
            url: url,
            title: title
        })
    }

}