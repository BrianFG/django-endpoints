digits_words = ["", "one", "two", "three", "four", "five",
                "six", "seven", "eight", "nine", "ten", "eleven",
                "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen"] 
 
tens_words = ["", "", "twenty", "thirty", "forty", "fifty",
              "sixty", "seventy", "eighty", "ninety"] 
 
thousands_words = ["", "thousand", "million", "billion", "trillion",
                   "quadrillion", "quintillion", "sextillion", "septillion",
                   "octillion", "nonillion", "decillion"]

    
def hundreds_to_words(n): 
    digits = n % 10 
    tens = n % 100 // 10
    hundreds = n % 1000 // 100
    words = list()
    if hundreds > 0:
        words.append(digits_words[hundreds])
        words.append("hundred")
    if tens > 1:
        words.append(tens_words[tens])
        if digits > 0:
            words.append(digits_words[digits])
    elif n%100 > 0:
        words.append(digits_words[n%100])
    return words


def number_to_words(num): 
    if num == 0: return ['zero']
    words = list()
    thousands = 0 
    while(num > 0): 
        remainder = num % 1000 
        num = num // 1000 
        if remainder > 0: 
            if thousands > 0:
                words.insert(0, thousands_words[thousands])
            words = hundreds_to_words(remainder)  + words
        thousands += 1 
    return words
