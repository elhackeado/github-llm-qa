from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def scrape_github_discussions(repository_url):
    # Initialize Chrome WebDriver (make sure you have chromedriver installed and in your PATH)
    driver = webdriver.Chrome()

    # Open the GitHub repository discussions page
    driver.get(repository_url + '/discussions?discussions_q=is%3Aopen+is%3Aanswered')

    # Wait for page to load
    driver.implicitly_wait(10)

    # Store discussion details
    discussions_data = []

    while True:
        # Find all discussion elements and collect their URLs
        discussion_elements = driver.find_elements(By.CSS_SELECTOR, '.list-style-none .Box-row')
        # list-style-none flex-1 mt-sm-n3
        # print(discussion_elements)
        discussion_urls = [discussion_element.find_element(By.CSS_SELECTOR, '.markdown-title').get_attribute('href') for discussion_element in discussion_elements]
        # markdown-title discussion-Link--secondary Link--primary Link f4 wb-break-word d-inline-block v-align-middle mr-1
        # Iterate over discussion URLs and extract information
        # print(discussion_urls)
        for discussion_url in discussion_urls:
            # Visit individual discussion page
            driver.get(discussion_url)
            discussion_number = discussion_url.split("/")[-1]

            # Extract discussion details from the conversation tab
            discussion_title = driver.find_element(By.CSS_SELECTOR, '.js-issue-title').text
            title = discussion_title
            print(discussion_number, title)
            
            # try:
            discussion_details = driver.find_element(By.CSS_SELECTOR, '.js-comment-body').text
            # print("DETAILS", discussion_details)
            # TimelineItem js-comment-container js-nested-comment-container js-targetable-element ml-0 pb-2 pl-3 discussion-nested-comment-timeline-item discussion-primer-next-nested-comment-timeline-item width-full color-bg-success timeline-child-comment-answer-border
            # discussion_details = discussion_details_element.text
            # discussion_answer = driver.find_element(By.CSS_SELECTOR, ".d-block.color-fg-default.comment-body.markdown-body.js-comment-body").text
            discussion_answer = driver.find_element(By.CSS_SELECTOR, "[aria-label='Marked as Answer'] .js-comment-body").text
            # print("=================================")
            # # print(driver.find_element(By.CSS_SELECTOR, ".color-bg-success").text)
            # print("ANSWER", discussion_answer)
            # print(discussion_answer)
               
            # except NoSuchElementException:
            #     discussion_details = ""

            discussions_data.append({'title': title, 'number': discussion_number, 'url': discussion_url, 'details': discussion_details, 'answer': discussion_answer})

            # Navigate back to the list of discussions page
        driver.quit()
        return discussions_data

if __name__ == "__main__":
    repository_url = input("Enter GitHub repository URL (e.g., https://github.com/username/repository): ")
    discussions = scrape_github_discussions(repository_url)
    for discussion in discussions:
        # print(f"discussion #{discussion['number']}: {discussion['title']} - {discussion['details']} - {discussion['url']}")
        file_name = "documents/"+discussion['number']+".txt"
        with open(file_name, "w") as file:
          file.write(f"discussion number is \"{discussion['number']}\"\ndiscussion URL link is \"{discussion['url']}\"\ndiscussion title is \"{discussion['title']}\"\nI want to know that {discussion['details']}. The correct answer is, {discussion['answer']}")
    