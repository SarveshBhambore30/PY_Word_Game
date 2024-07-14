#---------------------------------------------------------------------------------------
# Code Developed By : Sarvesh B.
#---------------------------------------------------------------------------------------
#1. Create wordlist of all possible 5 letter words.
#2. Generate fucntion that will pick any word which will be the word for the day.
#3. Allow user 5 attempt to guess the word.
#4. If user able to identify the correct word Congratulate the User.
#5. Else Show the user correct Answer.
#----------------------------------------------------------------------------------------
import random 

def arr_of_word_list():
    with open("word_list.txt", "r") as Word_list:
        lines = Word_list.read().split(',')
    return lines 

def choose_random_word(word_list):
    word_pos = random.randint(0,len(word_list))
    return word_list[word_pos]

def check_word_length(word_for_the_day,user_words):
    res=len(user_words)==len(word_for_the_day)
    return res

def check_isdigit(user_words):
    res= any(chr.isdigit()for chr in user_words)
    return res

def is_Correcct_Word(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i

    return -1

def main():
    word_list=arr_of_word_list()
    word_for_the_day=choose_random_word(word_list)
    word_for_the_day=word_for_the_day.replace('"', "")
    #print("Word for the Day : {}".format(word_for_the_day))
    max_trials=5
    trials=0
    for word in range(trials,max_trials):
        user_words= input("Trial {} of {} - Enter Word : ".format(word+1,max_trials))
        cwl=check_word_length(word_for_the_day,str(user_words))
        cd=check_isdigit(user_words)
        if(cwl==True and cd==False):
            result = is_Correcct_Word(word_for_the_day,user_words)
            if result==-1:
                print("In-correct Guess!!")
            else:
                print("Congratulations, you've guessed the word {} correctly!!!".format(user_words))
                break
        else:
            print("Please provide the valid input!!")
            continue
    
        if (word==max_trials):
            print("Sorry, you've reached the Maximum number of trails. the correct answer of the day was {}".format(word_for_the_day))


if __name__ == "__main__":
    main()
