#igpay is a function. If you want to use this function type igpay() and in the parathesis a word of your choosing
#This function evaluates if the word starts with a vowel. If not it goes to the else.
#This will allow you to translate your words into piglatin
word = input('Enter a word: ') 
vowels = 'aeiouAEIOU'
if word[0] in vowels:
    print(word + 'way')
else:
    print(word[1:] + word[0] + 'ay')