const puppeteer = require('puppeteer-extra')
const StealthPlugin = require('puppeteer-extra-plugin-stealth')
puppeteer.use(StealthPlugin())
const AdblockerPlugin = require('puppeteer-extra-plugin-adblocker')
puppeteer.use(AdblockerPlugin())
const UserAgent = require("user-agents");



(async () => {
    
    for(let i = 0; i < 10; i++) {

        const browser = await puppeteer.launch({
            headless: false,
            executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
            userDataDir: '/Users/barrydaniels/Library/Application Support/Google/Chrome/Default',
            
        });
        
        const page = await browser.newPage();
        await page.setUserAgent(new UserAgent().toString());
        try {
            await page.goto('https://www.coinmarketcap/', {timeout: 180000});
        } catch(err) {
            console.log(err);
        }
        
        console.log(await browser.userAgent());
        await page.waitForSelector("#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(1) > div > div.sc-111rrsy-0.qbrWo > div:nth-child(6) > div > div.sc-266vnq-1.gffsPR");
        await page.waitForTimeout(Math.random() * (1000 - 5000) + 1000);
        await page.click("#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(1) > div > div.sc-111rrsy-0.qbrWo > div:nth-child(6) > div > div.sc-266vnq-1.gffsPR");
        await page.keyboard.type('E');
        await page.keyboard.type('V');
        await page.keyboard.type('R');
        await page.keyboard.press('Enter');
        await page.waitForSelector("#__next > div.bywovg-1.fUzJes > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.jKrmxw.container > div > div.sc-16r8icm-0.sc-19zk94m-1.gRSJaB > div.sc-16r8icm-0.dSXRna > div.sc-16r8icm-0.sc-19zk94m-4.iNWJA-d > div > div.pqmllm-2.hLrBVF > button:nth-child(1)");
        await page.waitForTimeout(Math.random() * (1000 - 5000) + 1000);
        await page.click("#__next > div.bywovg-1.fUzJes > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.jKrmxw.container > div > div.sc-16r8icm-0.sc-19zk94m-1.gRSJaB > div.sc-16r8icm-0.dSXRna > div.sc-16r8icm-0.sc-19zk94m-4.iNWJA-d > div > div.pqmllm-2.hLrBVF > button:nth-child(1)");
        await page.waitForTimeout(Math.random() * (10000 - 50000) + 10000);
        await browser.close();

    }

  })();


