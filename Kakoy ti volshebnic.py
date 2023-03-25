Mother=input()
Father=input()
if Mother=='грязнокровка' and Father=='грязнокровка':
    print('грязнокровка')
else:
    if Mother=='полукровка' and Father=='полукровка':
        print('полукровка')
    else:
        if Mother=='чистокровка' and Father=='чистокровка':
            print('чистокровка')
        else:
            if Mother=='грязнокровка' and Father=='полукровка':
                print('полукровка')
            else:
                if Mother=='грязнокровка' and Father=='чистокровка':
                    print('полукровка')
                else:
                    if Mother=='полукровка' and Father=='грязнокровка':
                        print('полукровка')
                    else:
                        if Mother=='полукровка' and Father=='чистокровка':
                            print('полукровка')
                        else:
                            if Mother=='чистокровка' and Father=='грязнокровка':
                                print('полукровка')
                            else:
                                if Mother=='чистокровка' and Father=='полукровка':
                                    print('полукровка')
                                else:
                                    print('ошибка')