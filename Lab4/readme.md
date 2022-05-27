<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 6

Conversion time: 1.719 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β33
* Fri May 27 2022 16:29:51 GMT-0700 (PDT)
* Source doc: Week4_LA
* Tables are currently converted to HTML tables.
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 6.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



```
BSCCS2003: Week-4 Lab Assignment
```



    In this assignment, you have to create a web application, using flask. We list below the instructions to be followed in preparing and submitting the solution. 


    General instructions: 


    • Submit a single .zip file containing all your submission files and folders, the name of which should be “_&lt;_roll <span style="text-decoration:underline;">n</span>umber_>_.zip”. E.g.: _21f1000000.zip _


    • The folder structure inside the zip file should be as follows: 


        – The Python program must be written inside a file named “app.py”. This file must reside inside the root directory of submission. 


        – All the HTML files should be kept inside a folder named “templates” and the images or CSS files (if any) should be kept in “static” folder and this “static” folder must reside inside the root directory of submission. 


        – You are not required to submit the data.csv file. 


    • You should not keep any code inside the scope of the condition “ if <span style="text-decoration:underline;">n</span>ame == ‘ <span style="text-decoration:underline;">m</span>ain ’ ” except run() call. 


    • Allowed Python packages: jinja2, matplotlib, flask, or any standard Python3 package. 


    • The web pages should be HTML5 compliant, e.g., the file should begin with the declaration _&lt;_!DOCTYPE html_>_. 


    • You will be given as input, a CSV file named _data.csv _that contains the marks of some students in few courses. The fields of the CSV file are given below. You have to write the application assuming that the CSV file is residing in the current working directory (same as app.py) and the name of the CSV file is data.csv. 


<table>
  <tr>
   <td>Student ID 
   </td>
   <td>Course ID 
   </td>
   <td>Marks
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
</table>



    Problem Statement: 


    • Using a standard flask template, you have to create an application that displays an index page as the first webpage. The index page should have an HTML form with two radio buttons: one with the label “Student ID” and the other with the label “Course ID”. It must also have an input text field to enter the ID and a button with label “Submit”, as shown in Figure 1. The HTML form should be same as mentioned below: 


    &lt;form method="POST" action="/" id = "data-form"> 


        &lt;input type="radio" name="ID" value="student_id" /> 


        &lt;label>Student ID&lt;/label> 


        &lt;input type="radio" name="ID" value="course_id" /> 


        &lt;label>Course ID&lt;/label> 


        &lt;input type="text" name="id_value" /> 


        &lt;input type="submit" value="Submit" /> 


    &lt;/form>


    • Suppose the radio button for student ID is selected and the user enters a student ID in the input text field as shown in Figure 2. Then, on clicking the “Submit” button, the application should send a POST request to the application’s URI = “/” and must extract marks of the specific student, for each course, from the input CSV file. It must display a table titled “Student Details”, having columns with headers: “Student ID”, “Course ID” and “Marks”. The table should also display the total marks of that student in the last row. It must also display a link to navigate back to the HTML form, as shown in the Figure 3. 


    The HTML for the table which displays the student details should look like the following. Its id should be “student-details-table”. 


    &lt;table border = "2" id = "student-details-table"> 


        &lt;tr> 


            &lt;th>Student Id&lt;/th> 


            &lt;th>Course Id&lt;/th> 


            &lt;th>Marks&lt;/th> 


        &lt;/tr> 


        &lt;tr> 


            &lt;td>student_id_data&lt;/td> 


            &lt;td>course_id_data&lt;/td> 


            &lt;td>marks_data&lt;/td> 


        &lt;/tr> 


        ... 


        ... 


        ... 


        &lt;tr> 


            &lt;td>student_id_data&lt;/td> 


            &lt;td>course_id_data&lt;/td> 


            &lt;td>marks_data&lt;/td> 


        &lt;/tr> 


        &lt;tr> 


            &lt;td colspan = "2" style="text-align:center"> Total Marks &lt;/td> 


            &lt;td>total_marks_data&lt;/td> 


        &lt;/tr> 


    &lt;/table> 


    Note: student <span style="text-decoration:underline;">i</span>d <span style="text-decoration:underline;">d</span>ata, course <span style="text-decoration:underline;">i</span>d <span style="text-decoration:underline;">d</span>ata, marks <span style="text-decoration:underline;">d</span>ata, total <span style="text-decoration:underline;">m</span>arks <span style="text-decoration:underline;">d</span>ata should be populated according to the data extracted from the CSV file. 


    • Suppose the radio button for course ID is selected and the user enters a course ID in the input text field as shown in Figure 4. Then, on clicking the “Submit” button, the application should send a POST request to the application’s URI = “/” and must find the highest and the average marks for that course and display it in a table. The title of the table must be “Course Details” and the column headers must be “Average Marks” and “Maximum Marks” as shown in Figure 5. The page must also display the histogram of marks for the given course ID as shown. It must also display a link to navigate back to the HTML form. The HTML for the table which displays the course details should look like the following. Its id should be “course-details-table”. 


    &lt;table border = "2" id = "course-details-table"> 


        &lt;tr> 


        &lt;th>Average Marks&lt;/th> 


        &lt;th>Maximum Marks&lt;/th> 


        &lt;/tr> 


        &lt;tr> 


        &lt;td>average_marks&lt;/td> 


                            Page 2


        &lt;td>maximum_marks&lt;/td> 


        &lt;/tr> 


    &lt;/table> 


    Note: average <span style="text-decoration:underline;">m</span>arks, maximum <span style="text-decoration:underline;">m</span>arks should be populated accordingly. 


    • The application should display an error message if there is a deviation from the expected input. For instance, suppose the radio button for student ID is selected, and the user enters a course ID or any other invalid text in the input text field or leaves it empty, then a message as shown in Figure 6 must be displayed. It must also display a link to navigate back to the HTML form. 



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")
Figure 1: Form 


    

<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")
Figure 2: Student input in form 


                            Page 3


    

<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")
Figure 3: Student Details 


    

<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")
Figure 4: Course input in form 


                            Page 4



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")
Figure 5: Course Details 



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")
Figure 6: Warning message 


                            Page 5
