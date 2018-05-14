import pandas as pd

time_sent = ["Monday : Doctor's Appointment at 2:45pm." ,
			"Tuesday : Dentist's Appointment at 11:30am.",
			"Wednesday : At 7:00pm , Basketball match.",
			"Thursday : Go home at 9:00pm.",
			"Friday : Football match at 12:15am."   
			]
## all these can be applied using Regex also

df = pd.DataFrame(time_sent , columns = ["text"])

## operations using pandas dataframe 
print (df["text"].str.len())
## splitting 
print (df["text"].str.split(" "))
## finding no of tokens in each list
print (df["text"].str.split().str.len())
## checking whether a string contains a pattern
print (df["text"].str.contains("Appointment"))
print (df["text"].str.contains(" is "))
## counting a occurance of pattern
print (df["text"].str.count("at"))
## finding an occurance
print (df["text"].str.findall(r'at'))



