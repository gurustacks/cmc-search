const puppeteer = require('puppeteer-extra')
const StealthPlugin = require('puppeteer-extra-plugin-stealth')
puppeteer.use(StealthPlugin())
const request = require('request');

(async () => {
    
        async function startSearch() {

            const proxy_urls = ['http://falcon.proxyrotator.com:51337/?apiKey=dUBVXtLRSC35xuGZzbfeNh6rc2sKE8Jy&userAgent=true,cookies=true&country=US',
                                'http://falcon.proxyrotator.com:51337/?apiKey=dUBVXtLRSC35xuGZzbfeNh6rc2sKE8Jy&userAgent=true,cookies=true&country=NL',
                                'http://falcon.proxyrotator.com:51337/?apiKey=dUBVXtLRSC35xuGZzbfeNh6rc2sKE8Jy&userAgent=true,cookies=true&country=DE',
                                'http://falcon.proxyrotator.com:51337/?apiKey=dUBVXtLRSC35xuGZzbfeNh6rc2sKE8Jy&userAgent=true,cookies=true&country=UK',
                                'http://falcon.proxyrotator.com:51337/?apiKey=dUBVXtLRSC35xuGZzbfeNh6rc2sKE8Jy&userAgent=true,cookies=true&country=FR',
                                'http://falcon.proxyrotator.com:51337/?apiKey=dUBVXtLRSC35xuGZzbfeNh6rc2sKE8Jy&userAgent=true,cookies=true&country=IT',
                                'http://falcon.proxyrotator.com:51337/?apiKey=dUBVXtLRSC35xuGZzbfeNh6rc2sKE8Jy&userAgent=true,cookies=true&country=ES',
                                'http://falcon.proxyrotator.com:51337/?apiKey=dUBVXtLRSC35xuGZzbfeNh6rc2sKE8Jy&userAgent=true,cookies=true&country=CA',
                                'http://falcon.proxyrotator.com:51337/?apiKey=dUBVXtLRSC35xuGZzbfeNh6rc2sKE8Jy&userAgent=true,cookies=true&country=AT',
                                'http://falcon.proxyrotator.com:51337/?apiKey=dUBVXtLRSC35xuGZzbfeNh6rc2sKE8Jy&userAgent=true,cookies=true&country=SE'];
            


            //const proxy = proxy_urls[Math.floor(Math.random() * proxy_urls.length)]
            const proxy = 'https://199.189.86.111:9800'
            request(proxy, function (error, response, body) {
                if (!error && response.statusCode == 200) {
                    console.log(JSON.parse(body).proxy + " " + JSON.parse(body).randomUserAgent);
                    doCMCSearch(JSON.parse(body).proxy, JSON.parse(body).randomUserAgent);
                } else {
                    console.log(error);
                }
            });
        
        }

        async function doCMCSearch(proxy,useragent) {

            const browser = await puppeteer.launch({
                headless: false,
                executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                userDataDir: '/Users/barrydaniels/Library/Application Support/Google/Chrome/Default',
                args: ['--proxy-server='+proxy]
            });

            console.log('browser launched with proxy: '+proxy + " and useragent: "+useragent);
            const page = await browser.newPage();
            //await page.setExtraHTTPHeaders({ referer: 'https://www.google.com' });
            //await page.setUserAgent(useragent);
            
            try {
                await page.goto('https://httpbin.org/headers', {timeout: 180000});
            } catch(err) {
                console.log(err);
            }
            
                        
            // await page.waitForSelector("#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(1) > div > div.sc-111rrsy-0.qbrWo > div:nth-child(6) > div > div.sc-266vnq-1.gffsPR", {timeout: 10000});
            // await page.waitForTimeout(Math.random() * (1000 - 5000) + 1000);
            // await page.click("#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(1) > div > div.sc-111rrsy-0.qbrWo > div:nth-child(6) > div > div.sc-266vnq-1.gffsPR");
            // await page.keyboard.type('M');
            // await page.keyboard.type('A');
            // await page.keyboard.type('T');
            // await page.keyboard.type('I');
            // await page.keyboard.type('C');
            // await page.keyboard.press('Enter');
            // await page.waitForSelector("#__next > div.bywovg-1.fUzJes > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.jKrmxw.container > div > div.sc-16r8icm-0.sc-19zk94m-1.gRSJaB > div.sc-16r8icm-0.dSXRna > div.sc-16r8icm-0.sc-19zk94m-4.iNWJA-d > div > div.pqmllm-2.hLrBVF > button:nth-child(1)", {timeout: 10000});
            // await page.waitForTimeout(Math.random() * (1000 - 5000) + 1000);
            // await page.click("#__next > div.bywovg-1.fUzJes > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.jKrmxw.container > div > div.sc-16r8icm-0.sc-19zk94m-1.gRSJaB > div.sc-16r8icm-0.dSXRna > div.sc-16r8icm-0.sc-19zk94m-4.iNWJA-d > div > div.pqmllm-2.hLrBVF > button:nth-child(1)");
            // await page.waitForTimeout(Math.random() * (10000 - 50000) + 10000);
            
            //await browser.close();

        }

        startSearch();
    


  })();


