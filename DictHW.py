#WH create dict of movies_db / web series
# 5 movies/web series

movies_db={}

key1="Border"
Border_movie_actors=["Sunny Deol","Suniel Shetty","Akshaye Khanna","Jackie Shroff","Tabu"]

key2="Border 2"
Border2_movie_actors=["Sunny Deol", "Varun Dhawan", "Diljit Dosanjh","Ahan Shetty","Medha Rana"]

key3="Raja Shivaji"
Rajashivaji_movie_actors=["Riteish Deshmukh","Genelia Deshmukh","Rahyl Riteish Deshmukh ","Sanjay Dutt","Abhishek Bachchan","Vidya Balan","Mahesh Manjreka","Salman Khan"]

key4="Tanhaji"
Tanhaji_movie_actors=["Ajay Devgn","Sunny Deol","Saif Ali Khan","Kajol","Sharad Kelkar"]

key5="Bajirao Mastani"
BajiraoMastani_movie_actors=["Ranveer Singh","Deepika Padukone","Priyanka Chopra","Sunny Deol"]

movies_db[key1]=Border_movie_actors
movies_db[key2]=Border2_movie_actors
movies_db[key3]=Rajashivaji_movie_actors
movies_db[key4]=Tanhaji_movie_actors
movies_db[key5]=BajiraoMastani_movie_actors

# print(movies_db)

# for key in movies_db:
#     print(key,movies_db[key])

# for key in movies_db:
#     print(key)

# for key,actors in movies_db.items():
#     for actore in actors:
#         if "Sunny Deol" in actors:
#             print(key)  

# for key,actors in movies_db.items():
#     if "Sunny Deol" in actors:
#             print(key)    

#find the count of actor/actress names per movies whose name having 15 characters
# count_dic={}
# for movie,actors in movies_db.items():
#     count=0
#     for actore in actors:
#         if len(actore)>=15:
#             count+=1
#         count_dic[movie]=count
# print(count_dic)

# #find frequency of every actors/actress name in your data base
freq={}
# for mname,cast in movies_db.items():
#     # print(mname,len(cast))
#     for actore in cast:
#         # print(actore)
#         # if actore in freq:
#         #     freq[actore] +=1
#         # else:
#         #     freq[actore] = 1
# #     # for actores in movies_db.values():
# #     #     print(actores)
# print(freq)

for cast in movies_db.values():
    for actore in cast:
        count=0
        for cast2 in movies_db.values():
            if actore in cast2:
                count +=1
        freq[actore]=count
print(freq)

#find the frequency of every character in given string
# s="i love python programming"
# dict={}
# for cha1 in s:
#     count=0
#     for cha2 in s:
#         if cha1==cha2:
#             count+=1
#     dict[cha1]=count
# print(dict)

# for cha in s:
#     key=cha
#     value=s.count(cha)
#     dict[key]=value
# print(dict)


# for ch in s:
#     if ch in dict:
#         dict[ch]=dict[ch]+1
#     else:
#         dict[ch]=1
# # print(dict)
