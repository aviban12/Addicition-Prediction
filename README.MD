Problem statement : Develop a machine learning algorithm to predict drug addiction probability based on different features.
<pre>
Approach:
	Data Preprocessing 
		1 - Sort the entire data on the basis of year
		2 - Create different list :
			 List1 - In LocationDesc column mark unique index for every new value.
			 List2 - Extract words which are related to intoxication from Greater_Risk_Question , Description manually.
			 List3 - In Sex column mark "Male" as 1 , "Female" as 2 and invalid or nan data as 0.
			 List4 - In SatisfactionType column mark unique index for every value. 
		3 - In GeoLocation column  seprate longitude and latitude and create two list
			 List5 - Longitude 
			 List6 - Latitude
		4 - In Question Code column remove alphabatic data from each code.
</pre>
<pre>
	Feature Extraction :
		1 -  Count number of words related to intoxication in Greater_Risk_Question column and Description.
		     Assumption - If a person consuming different type of drug then probability may increase to be addicted.
		2 -  Save all the preprocessed data , extracted data and store in a csv file.
	Algorithm Applied:
		1 - Linear Regression gives an accuracy of 68.53 on the provided test cases.
		2 - RandomForesetRegressor gives an accuracy of 93.58 on the provided test cases.
</pre>
<pre>
Feature Engineering:
	   Feature engineering is the process of using domain knowledge of the data to create features that make machine learning algorithms work.
	   In the given dataset their are two type of data 
		1 - Text Data
		2 - Numeric Data
	  From text data we are determining the count of drug a person is cosuming and how much amount of drug he is consuming. Greater the number of count of drug and sample size greater will be the possibility of addiction.
</pre>
<pre>
IDE Used :
	Pycharm Edu
Operating System :
	Linux (ubuntu 18.04)
Tools Used :
	Numpy
	Pandas
	TextBlob
	re
Exceution : Exeute Run.py file using python3 Run.py command on Linux.
</pre>



