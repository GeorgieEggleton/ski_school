# Introduction
Alps Ski School is a fictional ski and snow board school based in the Swiss Alpes. Catering to both Adults and Children of all abilities. The idea behind the project was to create a booking system to allow a user to book the appropriate lesson for either themselves or other members of their family. 

The system will allow the user to save multiple family members details so that on booking a lesson the owner of the site will have the names, ages and abilities of all those book in. 

The user-centric experience means the customer can easily navigate the various lesson types available, select the appropriate lesson, and book themselves in with ease and receive an email confirmation on booking completion. 

![Mockup](/media/ReadMe_images/MockUpScreenshot.png)


### Link to the live site – https://alps-snow-school-4dd405a355b2.herokuapp.com/

# Scope
The project aims to develop an e-commerce website offering customers the ability to book ski and snowboard lessons. The website will be responsive and user-friendly, providing the user with the ability to:

As a Customer:
- Register and Login
- Browse, search and refine available lessons 
- Add lessons to shopping cart
- View remaining spaces on each lesson
- Add students details to specific lesson
- Delete items from shopping cart
- Pay for items securely by using the Stripe payment system
- Save and update personal information
- View previous lessons
- Receive a confirmation email when booking is complete

As an Admin:
- Admins can access the admin dashboard to add available lesson dates / times
- Admins can delete lessons from the system.
- Admins can edit the max- capacity of the lesson.
- Admins can add a new lesson date / time



# Design
The website is designed to be clear and simple to navigate with little fuss so that there is no distraction from getting the important information across. 

Balsamiq was used to create wireframe drawings as a design template to work from throughout the development of this project. 

![Wireframe - Home](/media/ReadMe_images/Wireframe%20-%20HomePage.png)

![Wireframe - Lessons](/media/ReadMe_images/Wireframe%20-%20LessonsPage.png)

![Wireframe - Lesson Details](/media/ReadMe_images/Wireframe%20-%20LessonDetailsPage.png)

![Wireframe - Summary Details](/media/ReadMe_images/Wireframe%20-%20Bag.png)

![Wireframe - Profile Page](/media/ReadMe_images/Wireframe%20-%20profile.png)

## Features
### Favicon
A favicon is used to help the user identify the correct site when they have multiple tabs open. I have used a custom image of a skier.
![Favicon](/media/ReadMe_images/Favicon%20-%20Screenshot.png)

### Home Page
The home page is designed to be a simple sleek site that clearly explains to the user who Alps Snow School are and what they offer. There is a nav menu, search box at the top to allow the user to quickly navigate to the appropriate page for the lessons they are interested in.

Further down are two images with a short introductory paragraph on the two disciplines offered by Alps Snow School, Skiing and Snowboarding.

![homePage](/media/ReadMe_images/HomePage_Screenshot.png)

![homePage](/media/ReadMe_images/HomePage_Screenshot2.png)

### Navigation Menu
The Navigation menu has dropdown options to help the user quickly navigate to each of the lesson types and clearly demonstrate all options available. 
![Navigation Menu](/media/ReadMe_images/NavMenu%20Dropdown.png)


### Footer
The footer on each page contains the contact details and social media links for the company meaning it is quick and easy for the user to find this information at any time if needed no matter what page on the site they are currently on.

![Footer](/media/ReadMe_images/Footer_Screenshot.png)


### Lessons Page
Depending on which options are selected the user will be redirected to the lessons page displaying all lesson options that match their search criteria. The lessons can be searched by Ski / Snowboard, Adult / Child and Beginner / Intermediate / Advanced. 

![Lesson Page](/media/ReadMe_images/lessonsPage%20Screenshot.png)

##### Hero Image
If the user clicks on either the Ski or Snowboard options from the circular images on the home page they will be re-directed to the lessons page showing all lesson options for their chosen discipline. The title in the hero image will update to represent their chosen option. 
![Ski Hero Image](/media/ReadMe_images/SkiHero.png)
![Snowboard Hero Image](/media/ReadMe_images/snowboardHero.png)


### Lessons Details Page
On selecting the desired lesson type the user is directed to the lessons details page. Here shows a further details of the appropriate lesson along with the available dates for that specific lesson. The user can select their desired date and the number of lessons they would like to book and click “Add to Bag”

![Lesson Details Page](/media/ReadMe_images/lessonsDetails%20screenshot.png)

![Lesson Details Page](/media/ReadMe_images/LessonDetails%20screenshot-dateoptions.png)

### Summary Page
Once the user has finished selecting the desired lessons they can click the bag icon in to top corner to go to the summery page. They will need to be Logged in at this stage. If not they will be prompted to do so. Here they can see a summery of all lessons in the bag and add the details of the student attending that lesson. 

![Lesson Details Page](/media/ReadMe_images/SummeryPage%20screenshot.png)

![Lesson Details Page - Add Student](/media/ReadMe_images/AddStudent%20popup%20screenshot.png)


### Checkout
On clicking Checkout the user will be redirected to the strip payment page where they can securely enter their payment details and then click Pay. Once the payment has been successfully processed the user will be redirected to the homepage and success message will display.  

![Checkout](/media/ReadMe_images/StripePayment%20screenshot.png)

![Payment Success](/media/ReadMe_images/Payment%20success%20screenshot.png)

### Custom 404
A custom 404 page is included

![Custom 404](/media/ReadMe_images/404_screenshot.png)


### NewsLetter Signup
Also included in the footer is the newsletter signup box. This is to encourage users to signup for the newsletter in the simplest, quickest way possible so that they are more likely to do it. This is important for future marketing campaigns and ensuring the company is able to make direct contact with potential customers. 

![Newsletter Signup](/media/ReadMe_images/Footer_Screenshot.png)

# Responsiveness 
Media quries have been used throughout the site to optimise it for use on mobile devices. 
![Mobile home](/media/ReadMe_images/mobile_home.png)
![Mobile lessons](/media/ReadMe_images/mobile_lessons.png)
![Mobile lesson details](/media/ReadMe_images/mobile_lessondetails.png)
![Mobile Summary](/media/ReadMe_images/mobile_summary.png)
![Mobile popup](/media/ReadMe_images/mobile%20popup.png)


## Agile Methodologies
The Agile Methodology approach was adopted during the development this website. I used GitHub's KanBan board for this.
User stories were categorized into "Must-Have", "Should-Have", and "Could-Have" features to prioritize the development process. 
While the sites Must-Have functionality is now working there are still a few “Could-Have’s” that I would have liked to include if I had of had more time. 

![KanBan Board](/media/ReadMe_images/Kanban%20screenshot.png)


## Database Schema
Here is the Database Schema for the project :

![Database Schema](/media/ReadMe_images/database_schema.png)

## Technologies Used
#### Languages
- HTML5
- CSS3
- Python
- JavaScript

#### Libraries and Frameworks
- Django
- CrispyForms
- Gunicorn
- Psycopg2
- Google Fonts
- Bootstrap
- JQuery

#### Tools
- GitPod
- GitHub
- Git
- Heroku
- ElephantSQL
- AWS – S3
- SQLite3
- FontAwesome
- Balsamiq
- W3C Validator
- W3C CSS Validator
- Lighthouse
- MailChimp



# Deployment
Initial set-up:
- Repository – Created an new repository on GitHub using Code Institute’s Full Template 
Git – Regular commit messages were used throughout development using the following 
     1. git add .
    2. git commit -m "Commit Message"
    3. git push
- ElephantSQL – Created an instance in Elephant SQL using their free TinyTurtle platform. 
- Heroku – Created a new app in Heroku
- Installed the config vars in the settings tab on Heroku, including the DATABASE_URL, AWS keys, Secret key and STRIPE keys
- Set Heroku up for automatic deployment so it would be linked to the repository and  would update automatically when pushed to GitHub. 
- Migrated the database to ElephantSQL
- AWS -Set up bucket, user and user groups on S3 and IAM on AWS website.
- Create AWS Access keys 
- Install Boto3 and Django storages. Freeze to requirements.txt. 
- Add storages to installed apps in Settings.py. 
- Add settings.py code for S3 dpending on whether USE_AWS is in the environment. 
- Add config vars to Heroku with USE_AWS set to true. 
- Add all images needed to the relevant bucket on AWS.



# Testing

![Testing-Desktop Menu](/media/ReadMe_images/testing_desktop_menu.png)
![Testing-Mobile Menu](/media/ReadMe_images/testing_mobile_menu.png)
![Testing-Footer](/media/ReadMe_images/testing_footer.png)
![Testing-Registration](/media/ReadMe_images/testing_registration.png)
![Testing-Lesson Details](/media/ReadMe_images/testing_lesson_details.png)
![Testing-Summary](/media/ReadMe_images/testing_summery.png)

# Business Plan, Marketing & SEO 

Alps Snow School was designed and implemented to meet a gap in the snow sport tuition market. While conducting market research I found that a lot of the existing snow sport schools did not have options to book lessons online and a lot of the information was hard to find and over complicated.  

The idea with Alps Snow School was to make the lesson booking process as simple as possible and allow the user to book and register their family members onto a lesson without having to contact the school directly.  

In order to market Alps Snow School a number of different routes will be used.  

  

Social Media channels will be used as a great way to boost and increase engagement with the business. A combination of organic and paid social media advertising will be used to promote the facebook business page to a targeted audience.  

![Facebook Buisness](/media/ReadMe_images/Facebook_business_Screenshot.png)

A newsletter signup box is included in the footer of all pages to encourage users to signup meaning the company is able to make direct contact with potential customers to tell them about important news and future offers.  

![Mailshot Example](/media/ReadMe_images/Mailshot_Screenshot%20.png)

Inclusion of site.xml file and robots.txt. file. 

The robots.txt file is required by google to tell it which sections of the website should be ignored when the google spiders crawl the website to decide on where it should place within the google pages on search result. I have included my robots.txt file in the root directory, as directed in tutorials.  

I ran a site.xml file on ' https://www.xml-sitemaps.com/' and have included this in the root directory, as specified in tutorials. 

Meta Tags 

I have included detailed meta tags in the <head> of the html with a combination of long tails and short tail keywords relevant to my site. 

## CREDITS
I derived a lot of inspiration for the project from the Boutique Ado walkthrough project, provided by Code institute. 

I used the following tutorial to add the Mailchip signUp box - https://testdriven.io/blog/django-mailchimp/

Images have been sourced from various locations including my own collection and google images. I have ensured any images taken from Google have free commercial rights. 




# Known Bugs
### Form Validation
If age is over 16 an error should be thrown to not allow booking to a child lesson 

### Chrome 
On testing in Chorme after deployment and number of bugs were found. These include:-
Jquery is not working in Chrome. This means that the "Add Student" dropdown feature is not stopping the user signing the same student up for multiple lesson. I spent a significant amount of time trying to fix this with the help of a Code Institute tutor but they had not seen this issue before and were unable to assist. 
Newsletter - The newsleeter signup form is not working in chrome. 

### Styling
The styling as not as polished as I would like. Unfortunately I ran out of time to do anything further with this. 
-	Home page paragrapgh text is too small on Mobile devices
-	There is a small point between the desktop and the mobile view where there text is the wrong size, I believe this only happens in DevTools responsive mode when pulling the screen size in. On all mobile devices I have tested it displays correctly. 

