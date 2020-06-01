*** Settings ***
Library         sqa_web_portal.lib.common_keywords.DriverKeywords
Library         DateTime
Variables       ../../lib/common_vars.py
Variables       ../../lib/ui_locator/locator.py
Test Setup                  Initialize
Test Teardown               Tear Down


*** Variables ***
${browser}                  firefox
${headless}                 False
${Date}=                    Get Current Date                result_format=%H-%M-%S
${screenshot_path}


*** Keywords ***
Initialize
    Log To Console          \n
    Log Executor Info
    Establish Browser       browser=${browser}           headless=${headless}
    Go To URL               ${ROOT_URL}


Tear Down
    Run Keyword If Test Failed           Take Screenshot              ${screenshot_path}/Failure_
    Close Browser

# Note: for the negative login cases, we covered in the API testing,
# so in this TDS, one negative login case will be added to login case on each
# platfrom for testing error message.


*** Test Cases ***
MVPCommon_Login_Func_1
    [Documentation]         Test admin user login to web portal successfully. \n
    ...                     \n
    ...                     **Description**: \n
    ...                         Login to web port with admin account. \n
    ...                     \n
    ...                     **Objective**: \n
    ...                         Verify that admin user can login to web portal. \n
    ...                     \n
    ...                     **Procedure**: \n
    ...                         -   Access web portal. \n
    ...                         -   Input admin username to username field. \n
    ...                         -   Input admin password to password field. \n
    ...                         -   Click Login button. \n
    ...                     \n
    ...                     **Expected results**: Login screen will be switched to home page. \n
    ...                     \n
    ...                     **REQ**: REQ-Demo-0.1-001

    [tags]                  level=Integration
    ...                     min_version=1.0
    ...                     max_version=None
    ...                     mode=auto
    ...                     epic:Web Portal
    ...                     feature:Demo Function
    ...                     story:Login

    ${RESULT}                           Send String To Element              ${LOGIN_PAGE_USERNAME_FIELD}              ${ADMIN_USERNAME}
    Should Be True                      ${RESULT}
    ${RESULT}                           Send String To Element              ${LOGIN_PAGE_PASSWORD_FIELD}              ${ADMIN_PASSWORD}
    Should Be True                      ${RESULT}
    Click To Element                    ${LOGIN_PAGE_LOGIN_BUTTON}
    Wait For                            3
    #  Check the page is navigated to Overview.
    ${RESULT}                           Check Text Present                  admin
    Should Be True                      ${RESULT}
