*** Settings ***
Library    sqa_web_portal.lib.keywords_library.DriverKeywords

*** Test Cases ***
TestCustomeLib1
    [Documentation]         a testing of keywords_library
    [tags]                  firefox
    Open Browser            firefox
    Go to url               https://paiza.io/en/languages/python3
    click to element        xpath:/html/body/div[1]/div[5]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a
    wait for                8
    type string             print("hello world from firefox")
    wait for                1
    click to element        xpath://*[@id="top-component"]/div[3]/div/span[1]/div/button[1]/span
    wait for                6
    close browser


*** Test Cases ***
TestCustomeLib2
    [Documentation]         a testing of keywords_library
    [tags]                  chrome
    Open Browser            chrome
    Go to url               https://paiza.io/en/languages/python3
    click to element        xpath:/html/body/div[1]/div[5]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a
    wait for                5
    type string             print("hello world from chrome")
    wait for                1
    click to element        xpath://*[@id="top-component"]/div[3]/div/span[1]/div/button[1]/span
    wait for                5
    close browser


*** Test Cases ***
TestCustomeLib3
    [Documentation]         open google
    [tags]                  chrome
    Open Browser            chrome
    Go to url               https://google.com
    close browser