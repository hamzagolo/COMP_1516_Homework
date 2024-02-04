# Author: Marvin Neoh
# Date: 4th February 2023

countries_and_capitals = (
    ['Afghanistan', 'Kabul'], ['Albania', 'Tirana (Tirane)'], ['Algeria', 'Algiers'], ['Andorra', 'Andorra la Vella'],
    ['Angola', 'Luanda'], ['Antigua and Barbuda', "Saint John's"], ['Argentina', 'Buenos Aires'],
    ['Armenia', 'Yerevan'], ['Australia', 'Canberra'], ['Austria', 'Vienna'], ['Azerbaijan', 'Baku'],
    ['Bahamas', 'Nassau'], ['Bahrain', 'Manama'], ['Bangladesh', 'Dhaka'], ['Barbados', 'Bridgetown'],
    ['Belarus', 'Minsk'], ['Belgium', 'Brussels'], ['Belize', 'Belmopan'], ['Benin', 'Porto Novo'],
    ['Bhutan', 'Thimphu'], ['Bolivia', 'Sucre'], ['Bosnia and Herzegovina', 'Sarajevo'], ['Botswana', 'Gaborone'],
    ['Brazil', 'Brasilia'], ['Brunei', 'Bandar Seri Begawan'], ['Bulgaria', 'Sofia'], ['Burkina Faso', 'Ouagadougou'],
    ['Burundi', 'Gitega'], ['Cambodia', 'Phnom Penh'], ['Cameroon', 'Yaounde'], ['Canada', 'Ottawa'],
    ['Cape Verde', 'Praia'], ['Central African Republic', 'Bangui'], ['Chad', "N'Djamena"], ['Chile', 'Santiago'],
    ['China', 'Beijing'], ['Colombia', 'Bogota'], ['Comoros', 'Moroni'],
    ['Congo, Democratic Republic of the', 'Kinshasa'], ['Congo, Republic of the', 'Brazzaville'],
    ['Costa Rica', 'San Jose'], ["Cote d'Ivoire (Ivory Coast)", 'Yamoussoukro'], ['Croatia', 'Zagreb'],
    ['Cuba', 'Havana'], ['Cyprus', 'Nicosia'], ['Czech Republic (Czechia)', 'Prague'], ['Denmark', 'Copenhagen'],
    ['Djibouti', 'Djibouti'], ['Dominica', 'Roseau'], ['Dominican Republic', 'Santo Domingo'], ['East Timor', 'Dili'],
    ['Ecuador', 'Quito'], ['Egypt', 'Cairo'], ['El Salvador', 'San Salvador'], ['England', 'London'],
    ['Equatorial Guinea', 'Malabo'], ['Eritrea', 'Asmara'], ['Estonia', 'Tallinn'], ['Eswatini (Swaziland)', 'Mbabana'],
    ['Ethiopia', 'Addis Ababa'], ['Federated States of Micronesia', 'Palikir'], ['Fiji', 'Suva'],
    ['Finland', 'Helsinki'], ['France', 'Paris'], ['Gabon', 'Libreville'], ['Gambia', 'Banjul'], ['Georgia', 'Tbilisi'],
    ['Germany', 'Berlin'], ['Ghana', 'Accra'], ['Greece', 'Athens'], ['Grenada', "Saint George's"],
    ['Guatemala', 'Guatemala City'], ['Guinea', 'Conakry'], ['Guinea-Bissau', 'Bissau'], ['Guyana', 'Georgetown'],
    ['Haiti', 'Port au Prince'], ['Honduras', 'Tegucigalpa'], ['Hungary', 'Budapest'], ['Iceland', 'Reykjavik'],
    ['India', 'New Delhi'], ['Indonesia', 'Jakarta'], ['Iran', 'Tehran'], ['Iraq', 'Baghdad'], ['Ireland', 'Dublin'],
    ['Israel', 'Jerusalem'], ['Italy', 'Rome'], ['Jamaica', 'Kingston'], ['Japan', 'Tokyo'], ['Jordan', 'Amman'],
    ['Kazakhstan', 'Nur-Sultan'], ['Kenya', 'Nairobi'], ['Kiribati', 'Tarawa Atoll'], ['Kosovo', 'Pristina'],
    ['Kuwait', 'Kuwait City'], ['Kyrgyzstan', 'Bishkek'], ['Laos', 'Vientiane'], ['Latvia', 'Riga'],
    ['Lebanon', 'Beirut'], ['Lesotho', 'Maseru'], ['Liberia', 'Monrovia'], ['Libya', 'Tripoli'],
    ['Liechtenstein', 'Vaduz'], ['Lithuania', 'Vilnius'], ['Luxembourg', 'Luxembourg'], ['Madagascar', 'Antananarivo'],
    ['Malawi', 'Lilongwe'], ['Malaysia', 'Kuala Lumpur'], ['Maldives', 'Male'], ['Mali', 'Bamako'],
    ['Malta', 'Valletta'], ['Marshall Islands', 'Majuro'], ['Mauritania', 'Nouakchott'], ['Mauritius', 'Port Louis'],
    ['Mexico', 'Mexico City'], ['Moldova', 'Chisinau'], ['Monaco', 'Monaco'], ['Mongolia', 'Ulaanbaatar'],
    ['Montenegro', 'Podgorica'], ['Morocco', 'Rabat'], ['Mozambique', 'Maputo'], ['Myanmar (Burma)', 'Nay Pyi Taw'],
    ['Namibia', 'Windhoek'], ['Nauru', 'No official capital'], ['Nepal', 'Kathmandu'], ['Netherlands', 'Amsterdam'],
    ['New Zealand', 'Wellington'], ['Nicaragua', 'Managua'], ['Niger', 'Niamey'], ['Nigeria', 'Abuja'],
    ['North Korea', 'Pyongyang'], ['North Macedonia (Macedonia)', 'Skopje'], ['Northern Ireland', 'Belfast'],
    ['Norway', 'Oslo'], ['Oman', 'Muscat'], ['Pakistan', 'Islamabad'], ['Palau', 'Melekeok'], ['Panama', 'Panama City'],
    ['Papua New Guinea', 'Port Moresby'], ['Paraguay', 'Asuncion'], ['Peru', 'Lima'], ['Philippines', 'Manila'],
    ['Poland', 'Warsaw'], ['Portugal', 'Lisbon'], ['Qatar', 'Doha'], ['Romania', 'Bucharest'], ['Russia', 'Moscow'],
    ['Rwanda', 'Kigali'], ['Saint Kitts and Nevis', 'Basseterre'], ['Saint Lucia', 'Castries'],
    ['Saint Vincent and the Grenadines', 'Kingstown'], ['Samoa', 'Apia'], ['San Marino', 'San Marino'],
    ['Sao Tome and Principe', 'Sao Tome'], ['Saudi Arabia', 'Riyadh'], ['Scotland', 'Edinburgh'], ['Senegal', 'Dakar'],
    ['Serbia', 'Belgrade'], ['Seychelles', 'Victoria'], ['Sierra Leone', 'Freetown'], ['Singapore', 'Singapore'],
    ['Slovakia', 'Bratislava'], ['Slovenia', 'Ljubljana'], ['Solomon Islands', 'Honiara'], ['Somalia', 'Mogadishu'],
    ['South Africa', 'Pretoria, Bloemfontein, Cape Town'], ['South Korea', 'Seoul'], ['South Sudan', 'Juba'],
    ['Spain', 'Madrid'], ['Sri Lanka', 'Colombo'], ['Sudan', 'Khartoum'], ['Suriname', 'Paramaribo'],
    ['Sweden', 'Stockholm'], ['Switzerland', 'Bern'], ['Syria', 'Damascus'], ['Taiwan', 'Taipei'],
    ['Tajikistan', 'Dushanbe'], ['Tanzania', 'Dodoma'], ['Thailand', 'Bangkok'], ['Togo', 'Lome'],
    ['Tonga', "Nuku'alofa"], ['Trinidad and Tobago', 'Port of Spain'], ['Tunisia', 'Tunis'], ['Turkey', 'Ankara'],
    ['Turkmenistan', 'Ashgabat'], ['Tuvalu', 'Funafuti'], ['Uganda', 'Kampala'], ['Ukraine', 'Kiev'],
    ['United Arab Emirates', 'Abu Dhabi'], ['United Kingdom', 'London'], ['United States', 'Washington D.C.'],
    ['Uruguay', 'Montevideo'], ['Uzbekistan', 'Tashkent'], ['Vanuatu', 'Port Vila'], ['Vatican City', 'Vatican City'],
    ['Venezuela', 'Caracas'], ['Vietnam', 'Hanoi'], ['Wales', 'Cardiff'], ['Yemen', "Sana'a"], ['Zambia', 'Lusaka'],
    ['Zimbabwe', 'Harare']
)

countries = (
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
    'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria',
    'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad',
    'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the',
    'Costa Rica', "Cote d'Ivoire (Ivory Coast)", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic (Czechia)', 'Denmark',
    'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'England',
    'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini (Swaziland)', 'Ethiopia', 'Federated States of Micronesia',
    'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala',
    'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran',
    'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo',
    'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
    'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania',
    'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar (Burma)',
    'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea',
    'North Macedonia (Macedonia)', 'Northern Ireland', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama',
    'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda',
    'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
    'Sao Tome and Principe', 'Saudi Arabia', 'Scotland', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore',
    'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain',
    'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand',
    'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
    'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City',
    'Venezuela', 'Vietnam', 'Wales', 'Yemen', 'Zambia', 'Zimbabwe'
)

capitals = (
    'Kabul', 'Tirana (Tirane)', 'Algiers', 'Andorra la Vella', 'Luanda', "Saint John's", 'Buenos Aires', 'Yerevan',
    'Canberra', 'Vienna', 'Baku', 'Nassau', 'Manama', 'Dhaka', 'Bridgetown', 'Minsk', 'Brussels', 'Belmopan',
    'Porto Novo', 'Thimphu', 'Sucre', 'Sarajevo', 'Gaborone', 'Brasilia', 'Bandar Seri Begawan', 'Sofia', 'Ouagadougou',
    'Gitega', 'Phnom Penh', 'Yaounde', 'Ottawa', 'Praia', 'Bangui', "N'Djamena", 'Santiago', 'Beijing', 'Bogota',
    'Moroni', 'Kinshasa', 'Brazzaville', 'San Jose', 'Yamoussoukro', 'Zagreb', 'Havana', 'Nicosia', 'Prague',
    'Copenhagen', 'Djibouti', 'Roseau', 'Santo Domingo', 'Dili', 'Quito', 'Cairo', 'San Salvador', 'London', 'Malabo',
    'Asmara', 'Tallinn', 'Mbabana', 'Addis Ababa', 'Palikir', 'Suva', 'Helsinki', 'Paris', 'Libreville', 'Banjul',
    'Tbilisi', 'Berlin', 'Accra', 'Athens', "Saint George's", 'Guatemala City', 'Conakry', 'Bissau', 'Georgetown',
    'Port au Prince', 'Tegucigalpa', 'Budapest', 'Reykjavik', 'New Delhi', 'Jakarta', 'Tehran', 'Baghdad', 'Dublin',
    'Jerusalem', 'Rome', 'Kingston', 'Tokyo', 'Amman', 'Nur-Sultan', 'Nairobi', 'Tarawa Atoll', 'Pristina',
    'Kuwait City', 'Bishkek', 'Vientiane', 'Riga', 'Beirut', 'Maseru', 'Monrovia', 'Tripoli', 'Vaduz', 'Vilnius',
    'Luxembourg', 'Antananarivo', 'Lilongwe', 'Kuala Lumpur', 'Male', 'Bamako', 'Valletta', 'Majuro', 'Nouakchott',
    'Port Louis', 'Mexico City', 'Chisinau', 'Monaco', 'Ulaanbaatar', 'Podgorica', 'Rabat', 'Maputo', 'Nay Pyi Taw',
    'Windhoek', 'No official capital', 'Kathmandu', 'Amsterdam', 'Wellington', 'Managua', 'Niamey', 'Abuja',
    'Pyongyang', 'Skopje', 'Belfast', 'Oslo', 'Muscat', 'Islamabad', 'Melekeok', 'Panama City', 'Port Moresby',
    'Asuncion', 'Lima', 'Manila', 'Warsaw', 'Lisbon', 'Doha', 'Bucharest', 'Moscow', 'Kigali', 'Basseterre', 'Castries',
    'Kingstown', 'Apia', 'San Marino', 'Sao Tome', 'Riyadh', 'Edinburgh', 'Dakar', 'Belgrade', 'Victoria', 'Freetown',
    'Singapore', 'Bratislava', 'Ljubljana', 'Honiara', 'Mogadishu', 'Pretoria, Bloemfontein, Cape Town', 'Seoul',
    'Juba', 'Madrid', 'Colombo', 'Khartoum', 'Paramaribo', 'Stockholm', 'Bern', 'Damascus', 'Taipei', 'Dushanbe',
    'Dodoma', 'Bangkok', 'Lome', "Nuku'alofa", 'Port of Spain', 'Tunis', 'Ankara', 'Ashgabat', 'Funafuti', 'Kampala',
    'Kiev', 'Abu Dhabi', 'London', 'Washington D.C.', 'Montevideo', 'Tashkent', 'Port Vila', 'Vatican City', 'Caracas',
    'Hanoi', 'Cardiff', "Sana'a", 'Lusaka', 'Harare'
)


def how_many_countries():
    """
    Returns the number of countries in the list "countries"
    :return: Number of countries, int
    """

    return len(countries)


def get_name_of_longest_country():
    """
    Returns the name of the longest country from the list "countries"
    :return: Name of longest country, str
    """
    longest_country = countries[0]

    for country in countries:
        if len(country) > len(longest_country):
            longest_country = country

    return longest_country


def get_number_of_capitals_containing(substring):
    """
    Returns the number of capitals that contain inputted substring
    :param substring: a chain of letters, str
    :return: number of capitals, int
    """

    number_of_capitals = 0

    for capital in capitals:
        if substring.lower() in capital or substring.capitalize() in capital:
            number_of_capitals += 1

    return number_of_capitals


def get_countries_and_capitals_that_start_with_the_same_letter():
    """
    Returns a list of countries and capitals that have the same starting letter
    :return: List of countries and capitals, list
    """
    countries_and_capitals_with_same_starting_letter = []

    for country, capital in countries_and_capitals:
        if country[0] == capital[0]:    # checks the first letter of both the country and the capital
            countries_and_capitals_with_same_starting_letter.append(f"{country} - {capital}")

    return countries_and_capitals_with_same_starting_letter


def get_capital_of(country):
    """
    Returns the capital of the given country
    :param country: Name of a country, str
    :return: Capital of a country, str
    """
    country = country.capitalize()

    if country in countries:
        # Finds the index of the given country and uses it to access the same country in the countries_and_capitals
        # list, then access the capital in the returned list
        return countries_and_capitals[countries.index(country)][1]
    else:
        return "No such country"


def get_list_of_countries_with_this_many_letters_in_name(num_letters):
    """
    Returns a list of countries with the given number of letters
    :param num_letters: NUmber of letters, int
    :return: List of countries, list
    """
    list_of_countries = []

    for country in countries:
        if len(country) == num_letters:
            list_of_countries.append(country)

    return list_of_countries


def get_capitals_and_countries_that_begin_and_end_with_same_letter():
    """
    Returns a list of capitals and countries that begin and end with the same letter
    :return: List of capitals and countries, list
    """
    list_of_countries, list_of_capitals = [], []

    for country, capital in countries_and_capitals:

        if country[0].lower() == country[-1]:
            list_of_countries.append(country)
        if capital[0].lower() == capital[-1]:
            list_of_capitals.append(capital)

    return list_of_countries + list_of_capitals


def print_countries_in_reverse_alphabetical_order():
    """
    Prints the countries in reverse alphabetical order
    :return: List of countries. list
    """

    return countries[::-1]


def main():
    # print(how_many_countries())
    #print(get_name_of_longest_country())
    #print(get_number_of_capitals_containing('e'))
    #print(get_number_of_capitals_containing('z'))
    #print(get_number_of_capitals_containing("'"))
    #print(get_number_of_capitals_containing('an'))
    #print(get_countries_and_capitals_that_start_with_the_same_letter())
    #print(get_capital_of('canada'))
    #print(get_capital_of('nEW zeaLAND'))
    #print(get_capital_of('xyz'))
    #print(get_list_of_countries_with_this_many_letters_in_name(11))
    #print(get_list_of_countries_with_this_many_letters_in_name(15))
    #print(get_capitals_and_countries_that_begin_and_end_with_same_letter())
    #print(print_countries_in_reverse_alphabetical_order())
    pass

if __name__ == "__main__":
    main()
