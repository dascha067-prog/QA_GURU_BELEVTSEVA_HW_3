def test_github_open(driver):
    url = "https://github.com/"
    driver.get(url)
    assert "GitHub" in driver.title
    assert driver.current_url == url
