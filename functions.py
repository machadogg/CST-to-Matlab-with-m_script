import inspect

# just for debuging purposes


def printdeb():

    line = inspect.currentframe().f_back.f_lineno
    print("Debug pass. Line ", line)

# deletes the dashes from CST


def del_dashes(lista):

    i = 0
    while i < len(lista):  # finds the dashes and delete them
        if '--' in lista[i]:
            del lista[i]
        i += 1
    return lista

# adjust the structure to prepare the final CSV file


def define_Sparam(lis, test):

    k = 0

    # Brings the plots together for the CSV
    # The CST file structure is
    # Frequency        S1,1
    # F1               v1
    # F2               v2
    # Frequency        S2,1
    # F1               v3
    # F2               v4
    # but we need it to be like this
    # Frequency,S11,Frequency,S21
    # F1,v1,F1,v3
    # F2,v2,F2,v4
    # this 'for' loop detects whether we are reading
    # the results from a floquet port (SZmin(1),Zmax(1)) - converts to s11-te or tm, depending on the index
    # or from a waveguide/discrete port (S1,1) - converts to s11, or s12, or s22 or s21

    for i in range(len(lis)):
        if test == 'N':

            if 'SZmin(1),Zmax(1)' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f s21-te'
                    lis[i] = ''
                else:
                    lis[i] = 'f s21-te'
                k += 1

            elif 'SZmax(1),Zmax(1)' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f s11-te'
                    lis[i] = ''
                else:
                    lis[i] = 'f s11-te'
                k += 1

            elif 'SZmax(1),Zmin(1)' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f s12-te'
                    lis[i] = ''
                else:
                    lis[i] = 'f s12-te'
                k += 1

            elif 'SZmin(1),Zmin(1)' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f s22-te'
                    lis[i] = ''
                else:
                    lis[i] = 'f s22-te'
                k += 1

            elif 'SZmin(2),Zmax(2)' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f s21-tm'
                    lis[i] = ''
                else:
                    lis[i] = 'f s21-tm'
                k += 1

            elif 'SZmax(2),Zmax(2)' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f s11-tm'
                    lis[i] = ''
                else:
                    lis[i] = 'f s11-tm'
                k += 1

            elif 'SZmax(2),Zmin(2)' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f s12-tm'
                    lis[i] = ''
                else:
                    lis[i] = 'f s12-tm'
                k += 1

            elif 'SZmin(2),Zmin(2)' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f s22-tm'
                    lis[i] = ''
                else:
                    lis[i] = 'f s22-tm'
                k += 1

            elif 'S1,1' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f s11'
                    lis[i] = ''
                else:
                    lis[i] = 'f s11'
                k += 1
            elif 'S2,1' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f s21'
                    lis[i] = ''
                else:
                    lis[i] = 'f s21'
                k += 1
            elif 'S1,2' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f s12'
                    lis[i] = ''
                else:
                    lis[i] = 'f s12'
                k += 1
            elif 'S2,2' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f s22'
                    lis[i] = ''
                else:
                    lis[i] = 'f s22'
                k += 1
            elif 'Z1,1' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f z11'
                    lis[i] = ''
                else:
                    lis[i] = 'f z11'
                k += 1
            elif 'Z2,1' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f z21'
                    lis[i] = ''
                else:
                    lis[i] = 'f,z21'
                k += 1
            elif 'Z1,2' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f z12'
                    lis[i] = ''
                else:
                    lis[i] = 'f z12'
                k += 1
            elif 'Z2,2' in lis[i]:
                if i > 0:
                    lis[0] = lis[0] + ' f z22'
                    lis[i] = ''
                else:
                    lis[i] = 'f z22'
                k += 1
            elif 'F' in lis[i]:  # If it doesn't match the patterns, generates generic name from CST
                ln = lis[i].split()
                param = ln[3].replace(',', '')
                if i > 0:
                    lis[0] = lis[0] + ' f ' + param
                    lis[i] = ''
                else:
                    lis[i] = 'f ' + param
                k += 1
        else:
            if 'F' in lis[i]:
                ln = lis[i].split()
                param = ln[3].replace(',', '')
                if '_' in lis[i]:
                    param = ln[3].replace('_', '-')
                if i > 0:
                    lis[0] = lis[0] + ' f ' + param
                    lis[i] = ''
                else:
                    lis[i] = 'f ' + param
                k += 1
        # Eliminate the white spaces and puts a comma for the CSV
        if i > 0:
            lis[i] = ','.join(lis[i].split())

    # lis = list(filter(None, lis))
   # print(type(lis[0]))
    # Clears the double blank lines, leaving one. We will need it later!
    for j in range(k):
        if i > 1:

            for i in range(len(lis)):

                if lis[i] == '' and lis[i - 1] == '':
                    del lis[i]
                    break

    del lis[len(lis) - 1]

    lis = adjusting(lis, k - 1)
    #print("k = ", k)
    head = lis[0]

    if 'SZmax(1),Zmax(1)' in head:
        print('yes')
        head = head.replace('SZmax(1),Zmax(1)', 'S_{11}-TE')
    if 'SZmax(1),Zmin(1)' in head:
        head = head.replace('SZmax(1),Zmin(1)', 'S_{12}-TE')
    if 'SZmin(1),Zmax(1)' in head:
        head = head.replace('SZmin(1),Zmax(1)', 'S_{21}-TE')
    if 'SZmin(1),Zmin(1)' in head:
        head = head.replace('SZmin(1),Zmin(1)', 'S_{22}-TE')
    if 'SZmax(2),Zmax(2)' in head:
        head = head.replace('SZmax(2),Zmax(2)', 'S_{11}-TM')
    if 'SZmax(2),Zmin(2)' in head:
        head = head.replace('SZmax(2),Zmin(2)', 'S_{12}-TM')
    if 'SZmin(2),Zmax(2)' in head:
        head = head.replace('SZmin(2),Zmax(2)', 'S_{21}-TM')
    if 'SZmin(2),Zmin(2)' in head:
        head = head.replace('SZmin(2),Zmin(2)', 'S_{22}-TM')
    if '/abs,dB' in head:
        head = head.replace('/abs,dB', '')
    print(head)
    lis[0] = head
    return lis


def adjusting(flis, r):

    list_empties = []
    soma = []

    # Creates a list of the empty lines as they separate the plots

    for n in range(len(flis)):

        if n > 1:

            if flis[n] == '':

                list_empties.append(n)
    list_empties.append(len(flis))

    # print(list_empties)

    # Creates a list with the number of data to be appended

    for n in range(len(list_empties)):
        if n > 0:
            soma.append(list_empties[n] - list_empties[n - 1])

    # print(soma)

    for n in range(r):

        for j in range(1, soma[n]):
            flis[j] = flis[j] + ',' + flis[j + list_empties[n]]

    for n in range(list_empties[0], len(flis)):

        flis[n] = ''

    flis = list(filter(None, flis))

    return flis
