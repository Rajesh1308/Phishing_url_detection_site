<h1> Unmasking Phishing URLs : A Machine Learning Approach</h1>
<p>This project is a generally a flask app in which a Machine Learning model is implemented to detect the legitimacy of URLs</p>
<h3>Dataset</h3>
<p>Nearly 11,000 datas are used to train and test this model with SVM algorithm (with RBF kernel).</p>
<p>The following features are extracted from the URLs provided</p>
<ol>
    <li>IP Address</li>
    <li>Length of URL</li>
    <li>Short URL service</li>
    <li>‘@’ symbol</li>
    <li>Double slash Redirection</li>
    <li>Prefix Suffix</li>
    <li>Subdomains</li>
    <li>Response</li>
    <li>Domain Registration Length</li>
    <li>Favicon Icon</li>
    <li>Port</li>
    <li>HTTPS token</li>
    <li>Request URL</li>
    <li>Google Index</li>
    <li>Fraud IP</li>
    <li>Links in tags</li>
    <li>Number of link </li>
    <li>Submitting to email</li>
    <li>Page Rank</li>
    <li>Abnormal URL</li>
    <li>On mouseover</li>
    <li>Right click</li>
    <li>Popup Window</li>
    <li>Iframe</li>
    <li>Age of Domain</li>
</ol>
<p>And some more</p>

<h3>Training and Test Results</h3>
<p>Out of 11,000 datas 80% datas were used to train model and 20% datas were used to test the model.</p>
<p>Many models were used to train the model which include (with accuracy score) </p>

<table>
  <tr>
    <th>Algorithm</th>
    <th>Accuracy Score</th>
  </tr>
  <tr>
    <td>Logistic Regression</td>
    <td>93.75%</td>
  </tr>
  <tr>
    <td>Support Vector Machine (linear kernel)</td>
    <td>91.45%</td>
  </tr>
  <tr>
    <td>Support Vector Machine (RBF kernel)</td>
    <td>94.02%</td>
  </tr>
   <tr>
    <td>Naive Bayes Classifier</td>
    <td>57.48%</td>
  </tr>
    <tr>
    <td>K-Nearest Neighbors </td>
    <td>93.17%</td>
  </tr>
</table>

<p>From this table, we can find that the SVM algorithm with RBF kernel has highest accuracy</p>
<p>Here is the confusion matrix for the test result of 20% data for the model developed using SVM algorithm with RBF kernel</p>

<table>
  <tr>
    <td>True Positive - 874</td>
    <td>False Positive - 83</td>
  </tr>
  <tr>
    <td>False Negative - 49</td>
    <td>True Negative - 1205</td>
  </tr>
</table>

<h3>Try it on your own</h3>
<p>To run this application in your system or PC, you should install git and Python </p>

<p>Once your system is ready with python installed, create a virtual environment (optional but preferred) and clone this repository using the following command</p>
<table>
  <tr>
    <th>git clone https://github.com/Rajesh1308/Phishing_url_detection_site.git</th>
  </tr>
</table>

<p>Then run this command inside the virtual environment in the terminal (or command prompt)</p>
<table>
  <tr>
    <th>pip install -r requirements.txt</th>
  </tr>
</table>
<p>Now all the requirements will be installed in your environment</p>

<p>After this, run gunicorn to host the flasp app in localhost. For this run the following command</p>
<table>
  <tr>
    <th>gunicorn app:app</th>
  </tr>
</table>

<p>Now your site will be running in your localhost and the link for it will be provided in the result.</p>

<h6>Deployed site</h6>
<p>This project is deployed on Render hosting service.</p>
<p>Click <a href="https://phishing-url-detection.onrender.com">here</a> to visit the site and test the URLs.</p>

<h4>Thanks for looking at my projects. Give it a try by clicking on the link provided above.</h4>

