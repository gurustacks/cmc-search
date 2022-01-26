const chrome = require('chrome-aws-lambda');
const puppeteer = require('puppeteer-core');


exports.handler = async function(event, context, callback) {

    const browser = await puppeteer.launch({
        args: chrome.args,
        executablePath: process.env.CHROME_EXECUTABLE_PATH || await chrome.executablePath,
        headless: chrome.headless,
    });
    
    const page = await browser.newPage();
    
    response = await page.goto('https://ipinfo.io/json');
    url = page.url();
    ip = await page.evaluate(() => {
        json_data =  document.querySelector('body').innerText;
        ip = JSON.parse(json_data).ip;
        return ip;
    });

    
    await browser.close();

    return {
        statusCode: 200,
        body: JSON.stringify({
            url: url,
            ip: ip
        })
    }

}