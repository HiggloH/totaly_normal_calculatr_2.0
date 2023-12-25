import sys
import calculator
import logger

#Key codes för input
exit_key: str = "exit"
reset_key: str = "reset"
print_log: str = "print log"
debug: str = "debug"

debug_bool = False

while True:
    _input = input("Skriv din uttryck: ")

    #Kollar efter key codes i inputen
    if _input == exit_key:
        print("Stänger av")
        sys.exit()
    elif _input == reset_key:
        logger.reset()
        print("Återställer log")
    elif _input == print_log:
        logger.print_file()
    elif _input == debug:
        if debug_bool:
            print("Debug är av aktiverat")
            debug_bool = False
        else:
            print("Debug är aktivt")
            debug_bool = True
    else:
        if debug_bool:
            svar = calculator.main(_input)
            calculator.clear_remove()

            if svar is None:
                print("Error, svart är None")
                logger.log(_input, "Error, svaret är none")
            else:
                print(svar)
                logger.log(_input, svar)
        else:
            try:
                svar = calculator.main(_input)
                calculator.clear_remove()

                if svar is None:
                    print("Error, svart är None")
                    logger.log(_input, "Error, svaret är none")
                else:
                    print(svar)
                    logger.log(_input, svar)
            except ValueError:
                print("Något gick fel")
