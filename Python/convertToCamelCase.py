def to_camel_case(text):
    words = [str(e) for e in text.replace('_','-').split("-")]
    text = words[0]
    for x in range(1,len(words)):
        text += words[x].capitalize()
    return(text)
    

to_camel_case('')
to_camel_case("the_stealth_warrior")
to_camel_case("The-Stealth-Warrior")
to_camel_case("A-B-C");