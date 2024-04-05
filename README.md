# Capsolver Extension Python

Capsolver Extension Python helps you easily use Capsolver Extension in Botasaurus, Selenium, and Playwright.

You can easily configure Capsolver with an API key without needing to download the Capsolver Extension, update config files, etc.


## Installation

```bash 
python -m pip install capsolver_extension_python
```

## Usage with [Botasaurus Web Scraping Framework](https://github.com/omkarcloud/botasaurus)

```python
from botasaurus import *
from capsolver_extension_python import Capsolver

@browser(
    extensions=[Capsolver(api_key="CAP-MY_KEY", blacklist_enabled=True, blacklist_urls=["https://www.site1.com/", "https://www.site2.com/", "https://www.site3.com/"])], # TODO: Replace with your own CapSolver Key
)  
def solve_captcha(driver: AntiDetectDriver, data):
    driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
    driver.prompt()

solve_captcha()
```

## Love It? [Star It ⭐!](https://github.com/omkarcloud/capsolver-extension-python)

Become one of our amazing stargazers by giving us a star ⭐ on GitHub!

It's just one click, but it means the world to me.

[![Stargazers for @omkarcloud/capsolver-extension-python](https://bytecrank.com/nastyox/reporoster/php/stargazersSVG.php?user=omkarcloud&repo=capsolver-extension-python)](https://github.com/omkarcloud/capsolver-extension-python/stargazers)
