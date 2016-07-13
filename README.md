<html>
<head>
	<title>Basic Arduino with Twitter API</title>
</head>
<body>
<p>
	Uses Twitter's Stream API and Ardunio to play a melody every time a there is a tweet that satisfies the parameters. The Tweepy library is used to make this project.
</p>

<p>
	Feel free to play around and change this to suit your own needs. This is only meant to be the beginning for using the Twitter API with the Ardunio. 
</p>


<h3> Using the Code</h3>
<p> Make sure to add your own 
	<ul>
		<li>Consumer Key</li>
		<li>Consumer Secret</li>
		<li>Access Key</li>
		<li>Access Secret</li>
	</ul>
</p>
<p> 
	Check the port that your Arduino is using and add that port to the file 
	ard_twitter.py in line 21
</p>
<p>
	Upload the Arduino code 
</p>
<p>
	Run the python file on command line
</p>
<p> You may need to wait for some time before a melody starts playing. Remember that you will only hear
    the sound when there is a tweet that matches the parameters. To get fast responses try common words or trending 
    phrases.
</p>


</body>
</html>
