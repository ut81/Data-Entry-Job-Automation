# Data-Entry-Job-Automation

In this project, i've automated fill the data in google form that is scrapped from a website.

# requirements
    1. you need to install BeautifulSoup
    2. install Chrome
    3. download chromedriver
    4. install & setup selenium


# steps to run :
  1. You can see your browser headers by going to this website:  http://myhttpheader.com/
  
  You'll need to pass along some headers in order for the request to return the actual website HTML. At minimum you'll need to give your "User-Agent" and "Accept-     Language" values in the request header.


  
  
  ![image](https://user-images.githubusercontent.com/126648429/222072288-147b3a03-f510-48e6-82b7-a4eecc722e0b.png)


                                                           
  2. you need to provide the path  of chromedriver.exe in chrome_driver_path.

  3. Go to https://docs.google.com/forms/ and create your own form:
  
  ![image](https://user-images.githubusercontent.com/126648429/222069236-5334f7d6-0cbc-44f6-8015-84d1e3274b0d.png)

  

  4. Add 3 questions to the form, make all questions "short-answer":
 
  ![image](https://user-images.githubusercontent.com/126648429/222069509-911f09fc-71a4-4ced-a63b-fdffe0d057b0.png)
  
  
  5.Click send and copy the link address of the form. You will need to use this in your program.
  
  ![image](https://user-images.githubusercontent.com/126648429/222069760-8c191b60-5e98-4d7b-8128-efa5de4f523d.png)
  
  5. Paste it into google_form_link in python script.
  
  6. Finally, run Data_Entry_Job_Automation.py
  

  
  


