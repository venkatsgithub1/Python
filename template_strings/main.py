from string import Template


def main():
    str1 = "Tom Haverford says {0} will be a huge {1} while also working in " \
           "{2}".format('Rent-a-Swag', 'success', 'Parks and rec')

    print(str1)

    # using template strings
    templ = Template('Bert Macklin is ${org} agent, wears cool ${acc}')

    string_2 = templ.substitute(org='FBI', acc='shades')

    print(string_2)

    # we can use dictionary to substitute.
    dict_1 = {
        'org': 'FBI',
        'acc': 'shades'
    }

    string_3 = templ.substitute(dict_1)
    print(string_3)


if __name__ == '__main__':
    main()
