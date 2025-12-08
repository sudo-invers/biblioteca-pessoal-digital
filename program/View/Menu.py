class Menu():

    def optionsMenu(totalOptions: int):

        menuLine = "|-   -   -   -   -   -   -   -  |"

        optionLine = "|                               |"

        iterable = 2 + totalOptions

        while iterable > 0:
            if iterable == totalOptions + 2 or iterable == 1:
                print(menuLine)
            else:
                print(optionLine)

            iterable = iterable - 1