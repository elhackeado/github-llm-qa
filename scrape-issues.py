from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def scrape_github_issues(repository_url):
    # Initialize Chrome WebDriver (make sure you have chromedriver installed and in your PATH)
    driver = webdriver.Chrome()

    # Open the GitHub repository issues page
    driver.get(repository_url + '/issues')

    # Wait for page to load
    driver.implicitly_wait(10)

    # Store issue details
    issues_data = []

    while True:
        # Find all issue elements and collect their URLs
        issue_elements = driver.find_elements(By.CSS_SELECTOR, '.js-navigation-container .Box-row')
        issue_urls = [issue_element.find_element(By.CSS_SELECTOR, '.js-navigation-open').get_attribute('href') for issue_element in issue_elements]

        # Iterate over issue URLs and extract information
        for issue_url in issue_urls:
            # Visit individual issue page
            driver.get(issue_url)
            issue_number = issue_url.split("/")[-1]

            # Switch to the "Conversation" tab to get the issue details
            # conversation_tab = driver.find_element(By.XPATH, "//a[contains(@data-tab-item, 'conversation-tab')]")
            # conversation_tab.click()

            # Extract issue details from the conversation tab
            issue_title = driver.find_element(By.CSS_SELECTOR, '.js-issue-title').text
            title = issue_title
            print(issue_number, title)
            
            try:
                issue_details_element = driver.find_element(By.CSS_SELECTOR, '.js-comment-body')
                issue_details = issue_details_element.text
            except NoSuchElementException:
                issue_details = ""

            issues_data.append({'title': title, 'number': issue_number, 'url': issue_url, 'details': issue_details})

            # Navigate back to the list of issues page
        driver.quit()
        return issues_data

        # Check if there is a next page
        # try:
        #     next_button = driver.find_element(By.XPATH, "//a[contains(@class, 'next_page')]")
        #     if next_button.get_attribute("disabled"):
        #         break  # Exit loop if next button is disabled
        #     else:
        #         next_button.click()  # Click next button to go to next page
        #         # Wait for page to load
        #         driver.implicitly_wait(10)
        # except NoSuchElementException:
        #     break  # Exit loop if next button is not found

    # Close the WebDriver
    # driver.quit()

    # return issues_data

if __name__ == "__main__":
    repository_url = input("Enter GitHub repository URL (e.g., https://github.com/username/repository): ")
    issues = scrape_github_issues(repository_url)
    for issue in issues:
        # print(f"Issue #{issue['number']}: {issue['title']} - {issue['details']} - {issue['url']}")
        file_name = "issues/"+issue['number']+".txt"
        with open(file_name, "w") as file:
          file.write(f"Issue number is \"{issue['number']}\"\nIssue URL link is \"{issue['url']}\"\nIssue title is \"{issue['title']}\"\nFollowing are the issue details {issue['details']}\n")
    