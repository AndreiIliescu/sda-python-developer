test = "String din modulul a"

def find_index(to_search, target):
    # enumerate ne va returna din lista ['primul elem'] -> (0, 'primul elem')
    for index, value in enumerate(to_search):
        if value == target:
            return index

    return -1

# Codul din if se va executa doar daca rulam acest fisier direct
# Daca este importat in alta parte, nu se executa
if __name__ == '__main__':
    print('Hello din modulul_a')
    print(find_index(["Gym", "Math"], "Gym"))
