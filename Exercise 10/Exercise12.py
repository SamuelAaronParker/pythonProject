#‘ThisIsAReallyLongStringThatIsFunToConvert’
#'1. PascalCase to snake_case
#''‘this_is_a_really_long_string_that_is_fun_to_convert’
#'2. snake_case to PascalCase
#3. Is one an anagram of the other?
#* “wholesome python activity”
#* “Woven Polytheistic Mat Toy”#
#Task 1
pascal = "ThisIsAReallyLongStringThatIsFunToConvert"
snake_case_s = ''.join(['_'+i.lower() if i.isupper() else i for i in pascal]).lstrip('_')
print(snake_case_s)

#Task 2
snake = "this_is_a_really_long_string_that_is_fun_to_convert"
x=snake.split("_")
res=[]
for i in x:
    i=i.title()
    res.append(i)
res="".join(res)
print(str(res))
