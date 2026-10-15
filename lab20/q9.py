special_chars = {"!", "@", "#", "$", "%", "&", "*"}

while True:
    password = input("Enter password: ")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    errors = [] #to add the errors create a new empty list

    # Step 1: Check password length
    if len(password) < 8:     #like isse user ko pata chal jaayega ki password ka length 8 se bada hi hona chahiye
        errors.append("Password must contain at least 8 characters")

    # Step 2: Check each character
    for ch in password: #characters are being checked so better use it in the same for loop if if karke you can easily do na

        if ch.isupper():
            has_upper = True

        if ch.islower():
            has_lower = True

        if ch.isdigit():
            has_digit = True

        if ch in special_chars:
            has_special = True
    #for loop ke bahar hai ye lol ?
    # Step 3: Check flags       #usi me include karne ke bajaye use se likha hai hamne the flag thing which we talking
    if not has_upper:          #we have used not operator here / like if nhi hai upper then append kar
        errors.append("Password must contain an uppercase letter")

    if not has_lower:
        errors.append("Password must contain a lowercase letter")

    if not has_digit:
        errors.append("Password must contain a digit")

    if not has_special:
        errors.append("Password must contain a special character")

    # Step 4: Check spaces
    if " " in password:      #error wale ke saath we are doing because " " anyways we dont need so it will come in error
        errors.append("Password must not contain spaces")

    # Step 5: Check the word 'password' in any case
    if "password" in password.lower():   #password.lower use kar rahe hai hamtaaki sirf password word dekh le ham
        errors.append("Password must not contain the word 'password'")

    # Step 6: Display errors or accept password
    if errors:    #it means if errors me kuch items hai , like khaaali nhi hai ( TRUE) hai
        print("Password is invalid. Fix these errors:")

        for error in errors: #errors ki list me each element is considered as error and usko print karo with "-"
            print("-", error)

        print()

    else: #error nhi hai matlab password to accepted hai so print accepted
        print("Password accepted")
        break #password mil kya to loop chodd do na






#