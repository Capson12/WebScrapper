from selenium import webdriver
url = 'https://www.youtube.com/channel/UCNa2KVKJOADkMNYvWLaqjZQ'
browser = webdriver.Chrome()
browser.get(url)

browser.find_elemnet_by_xpath('/html/body/link[9]').click
