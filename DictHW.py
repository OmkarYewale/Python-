#WH create dict of movies_db / web series
# 5 movies/web series

movies_db={}

key1="Border"
Border_movie_actors=["Sunny Deol","Suniel Shetty","Akshaye Khanna","Jackie Shroff","Tabu","Rakhee Gulzal","Pooja Bhatt","Puneet Issar","Sudesh Berry"]

key2="Border 2"
Border2_movie_actors=["Sunny Deol", "Varun Dhawan", "Diljit Dosanjh","Ahan Shetty","Medha Rana","Sonam Bajwa","Mona Singh","Anya Singh"]

key3="Raja Shivaji"
Rajashivaji_movie_actors=["Riteish Deshmukh","Genelia Deshmukh","Rahyl Riteish Deshmukh ","Sanjay Dutt","Abhishek Bachchan","Vidya Balan","Bhagyashree","Mahesh Manjreka","Salman Khan","Sachin Khedekar","Fardeen Khan","Amole Gupte","Boman Irani","Jitendra Joshi","Ashok Samarth"]

key4="Tanhaji"
Tanhaji_movie_actors=["Ajay Devgn","Saif Ali Khan","Kajol","Sharad Kelkar","Padmavati Rao","Luke Kenny","Neha Sharma","Shashank Shende","Devdatta Nage","Ajinkya Deo"]

key5="Bajirao Mastani"
BajiraoMastani_movie_actors=["Ranveer Singh","Deepika Padukone","Priyanka Chopra"," Tanvi Azmi","Milind Soman","Mahesh Manjrekar","Aditya Panchol","Raza Murad","Vaibbhav Tatwawdi"]

movies_db[key1]=Border_movie_actors
movies_db[key2]=Border2_movie_actors
movies_db[key3]=Rajashivaji_movie_actors
movies_db[key4]=Tanhaji_movie_actors
movies_db[key5]=BajiraoMastani_movie_actors

# print(movies_db)

for key in movies_db:
    print(key,movies_db[key])