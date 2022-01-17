const chrome = require('chrome-aws-lambda');
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());
const UserAgent = require("user-agents");

exports.handler = async function(event, context, callback) {

    const browser = await puppeteer.launch({
        args: chrome.args,
        executablePath: process.env.CHROME_EXECUTABLE_PATH || await chrome.executablePath,
        headless: chrome.headless,
    });
    
    const page = await browser.newPage();
    await page.setUserAgent(new UserAgent().toString());
    const useragent = await page.evaluate(() => navigator.userAgent); 
    
    response = await page.goto('https://ipinfo.io/json');
    url = await page.url();
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
            useragent: useragent,
            ip: ip
        })
    }

}