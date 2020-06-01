*** Settings ***
Library         sqa_mobile_app.lib.common_keywords.DriverKeywords
Variables       ../../lib/common_vars.py
Variables       ../../lib/ui_locator/locator.py
Test Setup                  Initialize
Test Teardown               Tear Down


*** Variables ***
${deviceName}
${platformName}
${platformVersion}
${appPackage}
${app}
${screenshot_path}
${LOGIN_TIMEOUT}            5


*** Keywords ***
Initialize
    Log To Console          \n
    Log Executor Info
    Set Driver              platform_name=${platformName}
    ...                     platform_version=${platformVersion}
    ...                     device_name=${deviceName}
    ...                     app=${app}
    ...                     app_package=${appPackage}


Tear Down
    Run Keyword If Test Failed           Take Screenshot              ${screenshot_path}/Failure_

# Note: for the negative login cases, we covered in the API testing,
# so in this TDS, one negative login case will be added to login case on each
# platform for testing error message.


*** Test Cases ***
Demo_Login_Func_1
    [Documentation]         Test Admin user login to mobile app. \n
    ...                     \n
    ...                     **Description**: \n
    ...                         Login to mobile app with Admin user. \n
    ...                     \n
    ...                     **Objective**: \n
    ...                         Verify that Admin user can login to mobile app. \n
    ...                     \n
    ...                     **Procedure**: \n
    ...                         -   Open mobile app. \n
    ...                         -   Input valid admin username to username field. \n
    ...                         -   Input valid admin password to password field. \n
    ...                         -   Press Login button. \n
    ...                     \n
    ...                     **Expected results**: Login screen will be switched to home page. \n
    ...                     \n
    ...                     **REQ**: REQ-Demo-0.1-001

    [tags]                  level=Integration
    ...                     min_version=1.0
    ...                     max_version=None
    ...                     mode=auto
    ...                     epic:Mobile App
    ...                     feature:Demo Function
    ...                     story:Login

    Remove Value From Element               ${LOGIN_SCREEN_USERNAME_FIELD}
    Type String To Element                  ${LOGIN_SCREEN_USERNAME_FIELD}      ${ADMIN_USERNAME}
    Remove Value From Element               ${LOGIN_SCREEN_PASSWORD_FIELD}
    Type String To Element                  ${LOGIN_SCREEN_PASSWORD_FIELD}      ${ADMIN_PASSWORD}
    Click To Element                        ${LOGIN_SCREEN_LOGIN_BUTTON}
    Wait For                                ${LOGIN_TIMEOUT}
    ${RESULT}                               Check Text Present                  Dashboard
    Should Be True                          ${RESULT}
